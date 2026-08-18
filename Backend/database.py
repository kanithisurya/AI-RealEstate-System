from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:@localhost:5432/real_estate_db"

engine = create_engine(DATABASE_URL)
