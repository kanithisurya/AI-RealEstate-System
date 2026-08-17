import joblib
from pathlib import Path
from huggingface_hub import hf_hub_download
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "Models"

model_path = hf_hub_download(
    repo_id="YOUR_USERNAME/ai-realestate-house-price-model",
    filename="house_price_model.pkl"
)

model = joblib.load(model_path)

scaler = joblib.load(MODEL_DIR / "scaler.pkl")
encoders = joblib.load(MODEL_DIR / "encoders.pkl")
