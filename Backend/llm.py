import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel("gemini-2.5-flash")

def explain_prediction(data, predicted_price):

    prompt = f"""
    A house has these features:

    City: {data.City}
    Location: {data.Location}
    BHK: {data.BHK}
    Bathrooms: {data.Bathrooms}
    Size: {data.Size_in_SqFt} sq ft
    Furnishing: {data.Furnishing}
    Distance to Metro: {data.Distance_to_Metro_km} km
    School Rating: {data.School_Rating}
    Hospital Distance: {data.Hospital_Distance_km}
    Crime Index: {data.Crime_Index}

    The ML model predicted the house price as
    {predicted_price:.2f} lakhs.

    Explain in simple language why the property received this estimated price.
    Keep the explanation under 120 words.
    """

    response = model.generate_content(prompt)

    return response.text