import json
import joblib
import azure.functions as func
import mlflow.sklearn

# Load model from MLflow
model_uri = "models:/fraud_model/Production"
model = mlflow.sklearn.load_model(model_uri)

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        transaction = req.get_json()
        features = [[transaction["amount"], transaction["merchant_id"], transaction["customer_id"]]]
        prediction = model.predict(features)[0]
        return func.HttpResponse(json.dumps({"fraud_prediction": int(prediction)}), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
