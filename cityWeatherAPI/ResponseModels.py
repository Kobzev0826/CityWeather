from datetime import datetime

from pydantic import BaseModel, Field


class CityStat(BaseModel):
    temperature: float = Field(..., alias="temperature")
    wind_speed: float = Field(..., alias="wind_speed")
    atmosphere_pressure: float = Field(..., alias="atmosphere_pressure")
    date: datetime = Field(..., alias="date")

    class Config:
        orm_mode = True


class AVGStat(BaseModel):
    temperature: float = Field(..., alias="temperature")
    wind_speed: float = Field(..., alias="wind_speed")
    atmosphere_pressure: float = Field(..., alias="atmosphere_pressure")

    class Config:
        orm_mode = True


class CityWeatherResponse(BaseModel):
    name_city: str = Field(..., alias="name_city")
    temperature: float = Field(..., alias="temperature")
    date: datetime = Field(..., alias="date")

    class Config:
        orm_mode = True
