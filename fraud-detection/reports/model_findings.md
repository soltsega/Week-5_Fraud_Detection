# Fraud Detection Model - Final Report
**Date**: 2025-12-30

## Model Performance
- **Threshold**: 0.8
- **Precision**: 0.80
- **Recall**: 0.40
- **F1-Score**: 0.53
- **Average Precision**: 0.85

## Key Findings
1. **Top Fraud Indicators**:
   - Low values of V14 (most significant)
   - Low values of V12
   - Low values of V10

2. **Model Behavior**:
   - Best at identifying clear fraud cases
   - More conservative in borderline cases
   - Balances between catching fraud and minimizing false alarms

## Recommendations
1. **For Production**:
   - Use threshold = 0.8 as a starting point
   - Monitor false negative rate in production
   - Consider A/B testing different thresholds

2. **For Future Improvements**:
   - Collect more labeled fraud cases
   - Add more features if available
   - Consider anomaly detection for unknown fraud patterns

## Usage Example
```python
# Load model
import joblib
model = joblib.load("models/fraud_detection_xgboost_final.pkl")

# Make prediction
prob_fraud = model.predict_proba(transaction_features)[:, 1]
is_fraud = prob_fraud >= 0.8
```