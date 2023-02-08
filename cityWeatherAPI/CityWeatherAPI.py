from datetime import datetime

from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from sqlalchemy import func, and_

from ResponseModels import CityStat, AVGStat, CityWeatherResponse
from base import session, Base, engine
from models import City, CityWeather
from openweathermap import get_city_id

app = FastAPI()

Base.metadata.create_all(engine)


@app.post("/weather/{city}")
async def add_city(city: str = Path()):
    db = session()
    city_in_db = db.query(City).filter(City.name_city == f'{city}').all()
    if city_in_db:
        raise HTTPException(status_code=417, detail="this city has already been added ")

    city_id = get_city_id(city)  # check if city exist city_id
    if not city_id:
        raise HTTPException(status_code=404, detail=f"city {city} not found ")

    db.add(City(city_id, city))
    db.commit()


@app.get("/city_stats")
async def get_city_status(city: str = Query(),
                          start_date: datetime | None = Query(default=datetime(2020, 1, 1)),
                          end_date: datetime | None = Query(default=datetime.now())
                          ):
    db = session()
    city_stats = db.query(
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
    city_stats_response = [CityStat.from_orm(cs) for cs in city_stats]
    avg_params = city_stats = db.query(
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
    avg_params_response = [AVGStat.from_orm(cs) for cs in avg_params]

    return {
        "name_city": city,
        "start_date": start_date,
        "end_date": end_date,
        "info": jsonable_encoder(city_stats_response),
        "avg": jsonable_encoder(avg_params_response)
    }


@app.get("/last_weather")
async def get_last_weather(search: str | None = Query(default="")):
    db = session()
    weather = db.query(
        City.name_city,
        func.row_number().over(partition_by=CityWeather.city_id, order_by = CityWeather.date).label('row_number'),
        CityWeather.temperature,
        CityWeather.date
    ).join(City,
           CityWeather.city_id == City.city_id
           ). \
        filter(City.name_city.like(f"{search}%")). \
        cte()
    last_weather = db.query(weather).filter(weather.c.row_number == 1).all()
    city_weather_response = [CityWeatherResponse.from_orm(cs) for cs in last_weather]

    return jsonable_encoder(city_weather_response)