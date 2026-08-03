from pydantic import BaseModel

class HouseInput(BaseModel):
    City: str
    Location: str
    BHK: int
    Bathrooms: int
    Size_in_SqFt: float
    Age_of_Property: int
    Parking: int
    Floor: int
    Total_Floors: int
    Furnishing: str
    Distance_to_Metro_km: float
    School_Rating: float
    Hospital_Distance_km: float
    Crime_Index: float
class SimilarPropertyRequest(BaseModel):
    City: str
    BHK: int
    Budget: float
    Size_in_SqFt: float