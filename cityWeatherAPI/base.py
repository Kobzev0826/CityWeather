from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

url = "mysql+mysqlconnector://root:123456@localhost:3306/city_weather"

engine = create_engine(url)

session = sessionmaker(engine)

Base = declarative_base()
