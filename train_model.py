import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import IsolationForest

mlflow.set_experiment("/Shared/fraud_detection")

# Load data
df = pd.read_parquet("/mnt/delta/gold_features")

X = df.drop("label", axis=1)
y = df["label"]

with mlflow.start_run():
    model = IsolationForest(contamination=0.01, random_state=42)
    model.fit(X)

    mlflow.sklearn.log_model(model, "fraud_model")
    mlflow.log_param("contamination", 0.01)
