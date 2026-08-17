import os

# Vercel allows writing to /tmp
os.environ["HF_HOME"] = "/tmp/huggingface"
os.environ["HF_HUB_CACHE"] = "/tmp/huggingface/hub"
os.environ["HF_XET_CACHE"] = "/tmp/huggingface/xet"
os.environ["HF_ASSETS_CACHE"] = "/tmp/huggingface/assets"

import joblib
from pathlib import Path
from huggingface_hub import hf_hub_download


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "Models"

# Writable directory on Vercel
TEMP_MODEL_DIR = Path("/tmp/realestate_model")
TEMP_MODEL_DIR.mkdir(parents=True, exist_ok=True)

# Download the 35 MB model from Hugging Face
model_path = hf_hub_download(
    repo_id="kanithisurya/ai-realestate-house-price-model",
    filename="house_price_model.pkl",
    local_dir=TEMP_MODEL_DIR
)

# Load the downloaded model
model = joblib.load(model_path)

# Load the smaller files from your GitHub project
scaler = joblib.load(MODEL_DIR / "scaler.pkl")
encoders = joblib.load(MODEL_DIR / "encoders.pkl")
