from datetime import datetime

from fastapi import FastAPI, Path, Query
from fastapi.encoders import jsonable_encoder

import repository
from ResponseModels import CityStat, AVGStat, CityWeatherResponse
from repository import session

app = FastAPI()

repository.create_tables()


@app.post("/weather/{city}")
async def add_city(city: str = Path()):
    repository.add_city(city)


@app.get("/city_stats")
async def get_city_stats(city: str = Query(),
                         start_date: datetime | None = Query(default=datetime(2020, 1, 1)),
                         end_date: datetime | None = Query(default=datetime.now())
                         ):
    city_stats = repository.get_city_stat(city, start_date, end_date)
    city_stats_response = [CityStat.from_orm(cs) for cs in city_stats]

    avg_params = repository.get_avg_city_stat(city, start_date, end_date)
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
    last_weather = repository.get_last_weather(search)
    city_weather_response = [CityWeatherResponse.from_orm(cs) for cs in last_weather]

    return jsonable_encoder(city_weather_response)
