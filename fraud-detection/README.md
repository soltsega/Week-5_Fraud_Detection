# Fraud Detection for E-commerce and Banking Transactions

This project focuses on building machine learning models to detect fraudulent transactions in both e-commerce and banking domains. The solution includes data analysis, feature engineering, model training, and explainability components.

## Project Structure

```
fraud-detection/
├── .github/
│   └── workflows/          # GitHub Actions workflows
├── data/                   # Data directory (gitignored)
│   ├── raw/                # Original datasets
│   └── processed/          # Processed and feature-engineered data
├── notebooks/              # Jupyter notebooks for analysis and modeling
├── src/                    # Source code
├── tests/                  # Unit tests
├── models/                 # Saved model artifacts (gitignored)
├── scripts/                # Utility scripts
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fraud-detection
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Jupyter kernel**
   ```bash
   python -m ipykernel install --user --name=fraud-detection
   ```

5. **Download the datasets**
   - Place the following files in the `data/raw/` directory:
     - `Fraud_Data.csv`
     - `IpAddress_to_Country.csv`
     - `creditcard.csv`

## Usage

1. **Exploratory Data Analysis**
   - `notebooks/eda-fraud-data.ipynb`: Analysis of e-commerce transaction data
   - `notebooks/eda-creditcard.ipynb`: Analysis of credit card transaction data

2. **Feature Engineering**
   - `notebooks/feature-engineering.ipynb`: Creating and transforming features

3. **Modeling**
   - `notebooks/modeling.ipynb`: Training and evaluating models
   - `notebooks/shap-explainability.ipynb`: Model interpretation using SHAP

## Project Timeline

- **Interim-1 Submission**: Sunday, 21 Dec 2025
- **Interim-2 Submission**: Sunday, 28 Dec 2025
- **Final Submission**: Tuesday, 30 Dec 2025

## Team

- **Tutors**:
  - Kerod
  - Mahbubah
  - Filimon

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
