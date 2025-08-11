# fraud-detection-pipeline

Goal: Detect fraudulent transactions in near real-time using Databricks, MLflow, and Azure Functions.
Architecture
Data Ingestion
Batch: Historical transactions (CSV files from Azure Blob Storage) → Databricks Delta Lake (Bronze)
Streaming: Simulated transaction stream from Azure Event Hubs → Databricks Delta Live Tables (Bronze)
Data Transformation
Silver Layer: Cleaned and validated transactions using Great Expectations
Gold Layer: Aggregated features for ML model
Model Training & Logging
Train an Isolation Forest model in Databricks
Log model with MLflow for versioning & reproducibility
Real-time Scoring
Deploy model in Azure Functions REST API
API accepts new transaction JSON and returns fraud score
Monitoring & Quality
Data quality rules with Great Expectations
Simple fraud detection metrics (precision, recall, etc.)
