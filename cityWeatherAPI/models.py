from sqlalchemy import Column, String, Integer, DECIMAL, DATETIME

from base import Base


class City(Base):
    __tablename__ = "cities"
    __table_args__ = {
        'schema': "city_weather"
    }

    city_id = Column(Integer, primary_key=True, index=True)
    name_city = Column(String)

    def __init__(self, city_id, name_city):
        self.city_id = city_id
        self.name_city = name_city


class CityWeather(Base):
    __tablename__ = "cityweather"
    __table_args__ = {
        'schema': "city_weather"
    }

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer)
    temperature = Column(DECIMAL(4, 2))
    wind_speed = Column(DECIMAL(8, 2))
    atmosphere_pressure = Column(Integer)
    date = Column(DATETIME)

    def __init__(self, city_id, temperature, wind_speed, atmosphere_pressure, date):
        self.city_id = city_id
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.atmosphere_pressure = atmosphere_pressure
        self.date = date
