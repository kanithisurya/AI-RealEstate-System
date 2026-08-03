import streamlit as st
import requests

st.set_page_config(
    page_title="AI Real Estate Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 AI Real Estate Price Prediction")
st.write("Enter the property details below.")

city = st.selectbox(
    "City",
    ["Hyderabad", "Bengaluru", "Chennai", "Pune"]
)

location = st.selectbox(
    "Location",
    ["Hadapsar", "Tambaram", "HSR Layout", "Baner", "Kharadi","Madhapur","Electronic City","Gachibowli","Anna Nagar","Kondapur","Whitefield","Velachery","OMR","Kukatpally","Porur","Hinjewadi","Marathahalli","Indiranagar","Wakad","Miyapur"]
)

bhk = st.number_input("BHK", min_value=1, max_value=10, value=2)

bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

size = st.number_input("Size (Sq Ft)", min_value=300, max_value=10000, value=1200)

age = st.number_input("Age of Property", min_value=0, max_value=100, value=5)

parking = st.number_input("Parking Spaces", min_value=0, max_value=10, value=1)

floor = st.number_input("Floor", min_value=0, max_value=100, value=3)

total_floors = st.number_input("Total Floors", min_value=1, max_value=100, value=10)

furnishing = st.selectbox(
    "Furnishing",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

metro = st.number_input(
    "Distance to Metro (km)",
    min_value=0.0,
    value=2.0
)

school = st.slider(
    "School Rating",
    1.0,
    5.0,
    4.0
)

hospital = st.number_input(
    "Hospital Distance (km)",
    min_value=0.0,
    value=2.0
)

crime = st.number_input(
    "Crime Index",
    min_value=0.0,
    value=1.0
)

if st.button("Predict Price"):

    data = {
        "City": city,
        "Location": location,
        "BHK": bhk,
        "Bathrooms": bathrooms,
        "Size_in_SqFt": size,
        "Age_of_Property": age,
        "Parking": parking,
        "Floor": floor,
        "Total_Floors": total_floors,
        "Furnishing": furnishing,
        "Distance_to_Metro_km": metro,
        "School_Rating": school,
        "Hospital_Distance_km": hospital,
        "Crime_Index": crime
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    if response.status_code == 200:

        result = response.json()

        if result["status"] == "success":

            st.session_state["prediction"] = result["predicted_price_lakhs"]
            st.session_state["ai_explanation"] = result["ai_explanation"]

        else:
            st.error(result["message"])

    else:
        st.error("Prediction failed.")
        st.write(response.text)


# Display Prediction

if "prediction" in st.session_state:

    st.success(f"🏡 Estimated Price: ₹ {st.session_state['prediction']:.2f} Lakhs")
    st.subheader("🤖 AI Explanation")
    st.write(st.session_state["ai_explanation"])


    if st.button("🏠 Show Similar Properties"):

        similar_data = {
            "City": city,
            "BHK": bhk,
            "Budget": st.session_state["prediction"],
            "Size_in_SqFt": size
        }

        similar_response = requests.post(
            "http://127.0.0.1:8000/similar-properties",
            json=similar_data
        )

        if similar_response.status_code == 200:

            houses = similar_response.json()["similar_properties"]

            if len(houses) == 0:

                st.warning("No similar properties found.")

            else:

                st.subheader("🏠 Similar Properties")

                for house in houses:

                    st.markdown(f"""### 📍 {house['location']}🏙 **City:** {house['city']}🛏 **BHK:** {house['bhk']}📐 **Size:** {house['size_in_sqft']} Sq Ft💰 **Price:** ₹ {house['price_in_lakhs']:.2f} Lakhs---""")

        else:

            st.error("Failed to fetch similar properties.")
            st.write(similar_response.text)