from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy import func, and_
from sqlalchemy.orm import sessionmaker

from models import City, CityWeather, Base
from openweathermap import get_city_id

url = "mysql+mysqlconnector://root:123456@localhost:3306/city_weather"

engine = create_engine(url)

session = sessionmaker(engine)


def create_tables():
    Base.metadata.create_all(engine)


def get_city_stat(city, start_date, end_date):
    db = session()
    return db.query(
        CityWeather.temperature,
        CityWeather.wind_speed,
        CityWeather.atmosphere_pressure,
        CityWeather.date,
    ).join(City,
           CityWeather.city_id == City.city_id). \
        filter(
        City.name_city.like(f"{city}%"),
        and_(
            CityWeather.date > start_date,
            CityWeather.date < end_date
        )
    ). \
        all()


def get_avg_city_stat(city, start_date, end_date):
    db = session()
    return db.query(
        func.avg(CityWeather.temperature).label('temperature'),
        func.avg(CityWeather.wind_speed).label("wind_speed"),
        func.avg(CityWeather.atmosphere_pressure).label("atmosphere_pressure")
    ).join(City,
           CityWeather.city_id == City.city_id). \
        filter(
        City.name_city.like(f"{city}%"),
        and_(
            CityWeather.date > start_date,
            CityWeather.date < end_date
        )
    ). \
        group_by(
        City.name_city,
    ). \
        all()


def get_last_weather(search):
    db = session()
    weather = db.query(
        City.name_city,
        func.row_number().over(partition_by=CityWeather.city_id, order_by=CityWeather.date).label('row_number'),
        CityWeather.temperature,
        CityWeather.date
    ).join(City,
           CityWeather.city_id == City.city_id
           ). \
        filter(City.name_city.like(f"{search}%")). \
        cte()
    last_weather = db.query(weather).filter(weather.c.row_number == 1).all()
    return last_weather


def add_city(city):
    db = session()
    city_in_db = db.query(City).filter(City.name_city == f'{city}').all()
    if city_in_db:
        raise HTTPException(status_code=417, detail="this city has already been added ")

    city_id = get_city_id(city)  # check if city exist city_id
    if not city_id:
        raise HTTPException(status_code=404, detail=f"city {city} not found ")

    db.add(City(city_id, city))
    db.commit()
