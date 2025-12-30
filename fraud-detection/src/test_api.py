import requests
import json

# Local server
BASE_URL = "http://localhost:8000"

def test_single_prediction():
    # Example transaction features (replace with actual feature values)
    sample_transaction = {
        "features": [0] * 30  # Replace with actual feature values
    }
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=sample_transaction
    )
    return response.json()

def test_batch_predictions():
    # The API expects a list of transactions directly, not wrapped in a "transactions" key
    sample_transactions = [
        {"features": [0] * 30},
        {"features": [0] * 30}
    ]
    
    response = requests.post(
        f"{BASE_URL}/predict_batch",
        json=sample_transactions  # Send the list directly
    )
    return response.json()

if __name__ == "__main__":
    # Test single prediction
    print("Testing single prediction:")
    result = test_single_prediction()
    print(json.dumps(result, indent=2))
    
    # Test batch prediction
    print("\nTesting batch predictions:")
    results = test_batch_predictions()
    print(json.dumps(results, indent=2))