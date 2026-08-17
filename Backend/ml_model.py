import joblib
from pathlib import Path
from huggingface_hub import hf_hub_download

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "Models"

# Download large model to Vercel's writable /tmp directory
model_path = hf_hub_download(
    repo_id="kanithisurya/ai-realestate-house-price-model",
    filename="house_price_model.pkl",
    cache_dir="/tmp/huggingface"
)

# Load model
model = joblib.load(model_path)

# Load smaller files from the project
scaler = joblib.load(MODEL_DIR / "scaler.pkl")
encoders = joblib.load(MODEL_DIR / "encoders.pkl")
