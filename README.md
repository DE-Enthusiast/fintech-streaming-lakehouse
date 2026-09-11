# fintech-streaming-lakehouse
Production-grade FinTech streaming lakehouse built on Databricks Serverless, Delta Lake, Auto Loader, Unity Catalog Volumes, and AI/BI Dashboards.


# High-Frequency FinTech Streaming Lakehouse & Fraud Intelligence

[![Databricks](https://img.shields.io/badge/Databricks-Serverless-FF3621?logo=databricks&logoColor=white)](https://databricks.com/)
[![Apache Spark](https://img.shields.io/badge/Apache_Spark-Structured_Streaming-E25A1C?logo=apachespark&logoColor=white)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta_Lake-ACID-00ADD8?logo=delta&logoColor=white)](https://delta.io/)
[![Unity Catalog](https://img.shields.io/badge/Unity_Catalog-Governed-0078D4)](https://www.databricks.com/product/unity-catalog)

An end-to-end streaming data pipeline engineered on Databricks Serverless Compute. The solution continuously lands synthetic credit card transactions into Unity Catalog Volumes, processes micro-batches using Apache Spark Structured Streaming with event-time watermarking, and serves analytical aggregates to a real-time Databricks AI/BI Dashboard.

---

## Architecture Flow

```mermaid
flowchart LR
    A[Mock Stream Producer] -->|JSON Micro-Batches| B[Unity Catalog Volume: /landing_files]
    B -->|Auto Loader cloudFiles| C[(Bronze: raw_transactions)]
    C -->|Watermarking & Quality Flags| D[(Silver: cleaned_transactions)]
    D -->|Clustered Aggregations| E[(Gold: fraud_analytics)]
    E --> F[Databricks AI/BI Dashboard]
