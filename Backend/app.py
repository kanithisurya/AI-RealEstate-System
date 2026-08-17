from fastapi import FastAPI
from sqlalchemy import text
import pandas as pd
from Backend.llm import explain_prediction

from Backend.schemas import HouseInput,SimilarPropertyRequest
from Backend.ml_model import model, encoders, scaler
from Backend.database import engine

from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def home():
    return {"message": "Real Estate API is running"}


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Real Estate API"
    }


@app.post("/predict")
def predict(data: HouseInput):
    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT 1
                FROM properties
                WHERE city = :city
                  AND location = :location
                LIMIT 1
            """),
            {
                "city": data.City,
                "location": data.Location
            }
        )

        valid = result.fetchone() is not None

    if not valid:
        return {
            "status": "error",
            "message": f"{data.Location} does not belong to {data.City}"
        }
    

    # Convert request data to DataFrame
    input_data = pd.DataFrame([data.model_dump()])

    # Encode categorical columns
    input_data["City"] = encoders["city"].transform(input_data["City"])
    input_data["Location"] = encoders["location"].transform(input_data["Location"])
    input_data["Furnishing"] = encoders["furnishing"].transform(input_data["Furnishing"])

    # Scale features
    input_scaled = scaler.transform(input_data)

    # Predict price
    prediction = model.predict(input_scaled)
    predicted_price = float(prediction[0])
    explanation = explain_prediction(data, predicted_price)

    # Save prediction history
    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO prediction_history
                (
                    city,
                    location,
                    bhk,
                    bathrooms,
                    size_in_sqft,
                    predicted_price
                )
                VALUES
                (
                    :city,
                    :location,
                    :bhk,
                    :bathrooms,
                    :size_in_sqft,
                    :predicted_price
                )
            """),
            {
                "city": data.City,
                "location": data.Location,
                "bhk": data.BHK,
                "bathrooms": data.Bathrooms,
                "size_in_sqft": data.Size_in_SqFt,
                "predicted_price": predicted_price
            }
        )
    

    return {
    "status": "success",
    "predicted_price_lakhs": round(predicted_price, 2),
    "ai_explanation": explanation
    }

@app.post("/similar-properties")
def similar_properties(data: SimilarPropertyRequest):

    with engine.begin() as conn:

        result = conn.execute(
            text("""
                SELECT
                    city,
                    location,
                    bhk,
                    size_in_sqft,
                    price_in_lakhs
                FROM properties
                WHERE city = :city
                AND bhk = :bhk
                AND price_in_lakhs <= :budget
                ORDER BY
                    ABS(price_in_lakhs - :budget),
                    ABS(size_in_sqft - :size)
                LIMIT 5
            """),
            {
                "city": data.City,
                "bhk": data.BHK,
                "budget": data.Budget,
                "size": data.Size_in_SqFt
            }
        )

        properties = []

        for row in result:
            properties.append(dict(row._mapping))

    return {
        "similar_properties": properties
    }
