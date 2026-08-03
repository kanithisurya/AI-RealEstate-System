import joblib

model = joblib.load("Models/house_price_model.pkl")
encoders = joblib.load("Models/encoders.pkl")
scaler = joblib.load("Models/scaler.pkl")
print(encoders.keys())