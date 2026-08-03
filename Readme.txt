🏠 AI-Powered Real Estate Price Prediction System

An end-to-end AI-powered web application that predicts residential property prices using Machine Learning, explains predictions using Google's Gemini LLM, recommends similar properties from a PostgreSQL database, and provides an interactive user interface through Streamlit.

The project combines Machine Learning, FastAPI, PostgreSQL, Streamlit, and Generative AI into a production-style application that assists users in estimating property prices and comparing them with similar market listings.

🚀 Features
🤖 AI Price Prediction
Predicts residential property prices using a trained Random Forest Regression model.
Accepts multiple property features as input.
Returns accurate estimated prices in Lakhs.
🧠 AI Explanation (Gemini)
Generates natural language explanations for every prediction.
Explains how features such as location, BHK, furnishing, metro distance, and amenities influence the estimated price.
🏠 Similar Property Recommendation
Searches the PostgreSQL database for properties with similar:
City
BHK
Budget
Property Size
Displays the closest matching properties to help users compare market prices.
💾 Prediction History
Stores every prediction made by users.
Saves prediction details into PostgreSQL for future analysis.
🌐 REST API
Built using FastAPI.
Provides REST endpoints for prediction and recommendation.
🎨 Interactive Frontend
User-friendly interface developed using Streamlit.
Simple property input forms.
Displays predictions, AI explanations, and similar properties.
📊 Price Comparison Dashboard
Compares predicted price with similar market properties.
Helps users evaluate whether the predicted value aligns with current market trends.
📸 Application Workflow
                    User
                      │
                      ▼
          Streamlit Web Application
                      │
                      ▼
                FastAPI Backend
        ┌─────────────┴─────────────┐
        ▼                           ▼
 Machine Learning Model       PostgreSQL Database
(Random Forest Regressor)     (Property Listings)
        │                           │
        ▼                           ▼
 Price Prediction        Similar Property Search
        │                           │
        └─────────────┬─────────────┘
                      ▼
              Gemini AI Explanation
                      │
                      ▼
             Display Results to User
🏗️ Project Architecture
AI-RealEstate-System
│
├── Backend
│   ├── app.py
│   ├── database.py
│   ├── llm.py
│   ├── ml_model.py
│   ├── schemas.py
│
├── Frontend
│   └── streamlit_app.py
│
├── Models
│   ├── house_price_model.pkl
│   ├── scaler.pkl
│   └── encoders.pkl
│
├── Dataset
│   └── real_estate_dataset_5000.csv
│
├── requirements.txt
│
└── README.md
🧠 Machine Learning Pipeline

The project follows a complete Machine Learning workflow.

Data Collection
Real estate dataset containing residential property information.
Data Preprocessing
Missing value handling
Duplicate removal
Feature selection
Label Encoding
Feature Scaling using StandardScaler
Features Used
Feature	Description
City	Property city
Location	Property locality
BHK	Number of bedrooms
Bathrooms	Number of bathrooms
Size_in_SqFt	Property size
Age_of_Property	Property age
Parking	Parking spaces
Floor	Current floor
Total_Floors	Building floors
Furnishing	Furnishing type
Distance_to_Metro_km	Metro distance
School_Rating	Nearby school rating
Hospital_Distance_km	Hospital distance
Crime_Index	Local crime index
Target Variable
Price_in_Lakhs
🤖 Machine Learning Model

Algorithm Used:

Random Forest Regressor

Reason for Selection:

Handles nonlinear relationships.
Works well with mixed numerical and categorical data.
Robust against overfitting.
Produces high prediction accuracy.
⚙️ Technology Stack
Programming Language
Python
Machine Learning
Scikit-learn
Pandas
NumPy
Backend
FastAPI
Uvicorn
Frontend
Streamlit
Database
PostgreSQL
SQLAlchemy
psycopg2
Generative AI
Google Gemini API
Model Persistence
Joblib
📂 Database Schema
Properties Table

Stores available residential properties.

Example columns:

property_id
city
location
bhk
bathrooms
size_in_sqft
furnishing
price_in_lakhs
Prediction History

Stores every prediction made by users.

Column
prediction_id
city
location
bhk
bathrooms
size_in_sqft
predicted_price
prediction_time
🌐 API Endpoints
Home
GET /

Returns

{
    "message":"Welcome to AI Real Estate API"
}
Predict Price
POST /predict

Request

{
    "City":"Hyderabad",
    "Location":"Gachibowli",
    "BHK":3,
    "Bathrooms":2,
    "Size_in_SqFt":1500,
    "Age_of_Property":5,
    "Parking":1,
    "Floor":4,
    "Total_Floors":10,
    "Furnishing":"Furnished",
    "Distance_to_Metro_km":1.5,
    "School_Rating":4.5,
    "Hospital_Distance_km":2,
    "Crime_Index":1.2
}

Response

{
    "status":"success",
    "predicted_price_lakhs":121.85,
    "ai_explanation":"..."
}
Similar Properties
POST /similar-properties

Request

{
    "City":"Hyderabad",
    "BHK":2,
    "Budget":120,
    "Size_in_SqFt":1200
}

Response

{
    "similar_properties":[
        {
            "city":"Hyderabad",
            "location":"Madhapur",
            "bhk":2,
            "size_in_sqft":1180,
            "price_in_lakhs":118
        }
    ]
}
💻 Installation
Clone Repository
git clone https://github.com/yourusername/AI-RealEstate-System.git
Navigate
cd AI-RealEstate-System
Create Virtual Environment
python -m venv venv

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
▶️ Running the Backend
uvicorn Backend.app:app --reload

API Documentation

http://127.0.0.1:8000/docs
▶️ Running Streamlit
streamlit run Frontend/streamlit_app.py
🔄 Project Workflow
User enters property details.
Streamlit sends data to FastAPI.
FastAPI validates the request.
Categorical features are encoded.
Features are scaled.
Random Forest predicts the property price.
Gemini generates an explanation.
Prediction is stored in PostgreSQL.
User can request similar properties.
SQL queries retrieve matching properties.
Results are displayed with price comparison.
📈 Future Enhancements
Interactive price comparison charts using Plotly
Property price trend analysis
Authentication and user accounts
Property image support
Google Maps integration
Real-time property listing updates
Cloud deployment (Render, Railway, AWS, Azure)
Docker containerization
CI/CD pipeline using GitHub Actions
🎯 Learning Outcomes

This project demonstrates practical experience in:

Machine Learning model development
Feature engineering
Model serialization
REST API development
Backend engineering with FastAPI
Frontend development using Streamlit
PostgreSQL database integration
SQL query optimization
Prompt engineering with Gemini
AI-assisted explanation generation
Recommendation system implementation
End-to-end ML application deployment
👨‍💻 Author

Surya Kanithi

B.Tech – Computer Science Engineering (AI & ML)
Python | Machine Learning | FastAPI | PostgreSQL | Streamlit | Generative AI | SQL | Scikit-learn