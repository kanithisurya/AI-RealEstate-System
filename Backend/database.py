from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:Surya%402004@localhost:5432/real_estate_db"

engine = create_engine(DATABASE_URL)