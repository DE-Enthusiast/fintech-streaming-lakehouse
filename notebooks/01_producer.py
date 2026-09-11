%sql
-- Replace 'workspace' with your active catalog name if different
USE CATALOG workspace;

CREATE SCHEMA IF NOT EXISTS fintech_bronze;
CREATE SCHEMA IF NOT EXISTS fintech_silver;
CREATE SCHEMA IF NOT EXISTS fintech_gold;

-- Create Managed Volumes inside fintech_bronze
CREATE VOLUME IF NOT EXISTS fintech_bronze.landing_files;
CREATE VOLUME IF NOT EXISTS fintech_bronze.checkpoints;



--CELL 2 

import json
import os
import random
import time
import uuid
from datetime import datetime, timezone

VOLUME_PATH = "/Volumes/workspace/fintech_bronze/landing_files/transactions/"
os.makedirs(VOLUME_PATH, exist_ok=True)

CATEGORIES = ["dining", "groceries", "electronics", "crypto_exchange", "fuel"]

def generate_record():
    is_fraud = random.random() < 0.05
    return {
        "txn_id": f"txn_{uuid.uuid4()}",
        "card_id": f"card_{random.randint(1000, 9999)}",
        "cust_id": f"cust_{random.randint(100, 1500)}",
        "amount": round(random.uniform(1500.0, 8500.0), 2) if is_fraud else round(random.uniform(5.0, 150.0), 2),
        "merchant_cat": "crypto_exchange" if is_fraud else random.choice(CATEGORIES),
        "country": "NG" if is_fraud else "US",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

print("Streaming micro-batches into Unity Catalog Volume...")
for batch_idx in range(5):
    records = [generate_record() for _ in range(25)]
    file_path = os.path.join(VOLUME_PATH, f"batch_{batch_idx}_{int(time.time())}.json")
    
    # Native POSIX write works seamlessly in Volumes
    with open(file_path, "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
            
    print(f"Landed batch {batch_idx + 1}/5 -> {file_path}")
    time.sleep(2)
