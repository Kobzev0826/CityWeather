from fastapi import FastAPI, Path, HTTPException

from base import session, Base, engine
from models import City
from openweathermap import get_city_id

app = FastAPI()

Base.metadata.create_all(engine)


@app.post("/weather/{city}")
async def add_city(city: str = Path()):
    print(f'city={city}')
    db = session()
    city_in_db = db.query(City).filter(City.name_city == f'{city}').all()
    print('city_in_db', city_in_db)
    if city_in_db:
        raise HTTPException(status_code=417, detail="this city has already been added ")

    city_id = get_city_id(city)  # check if city exist city_id
    if not city_id:
        raise HTTPException(status_code=404, detail=f"city {city} not found ")

    db.add(City(city_id, city))
    db.commit()
