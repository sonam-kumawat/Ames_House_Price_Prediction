import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
import joblib
from sklearn.datasets import fetch_openml

# Load Ames Housing dataset
data = fetch_openml(data_id=42165, as_frame=True)
df = data.frame

# Select 10 important features + target
features = ['LotArea','OverallQual','OverallCond','YearBuilt','YearRemodAdd',
            'MasVnrArea','BsmtFinSF1','TotalBsmtSF','GrLivArea','GarageCars']
X = df[features]
y = df['SalePrice']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build pipeline: scaler + XGBoost
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', XGBRegressor())
])

# Train model
pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, 'model.pkl')
print("Model trained and saved as model.pkl")
