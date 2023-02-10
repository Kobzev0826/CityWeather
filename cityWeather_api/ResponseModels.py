from datetime import datetime
from typing import  Optional
from pydantic import BaseModel, Field


class CityStat(BaseModel):
    temperature: float = Field(..., alias="temperature")
    wind_speed: float = Field(..., alias="wind_speed")
    atmosphere_pressure: float = Field(..., alias="atmosphere_pressure")
    dttm: datetime = Field(..., alias="dttm")

    class Config:
        orm_mode = True


class AVGStat(BaseModel):
    temperature: float = Field(..., alias="temperature")
    wind_speed: float = Field(..., alias="wind_speed")
    atmosphere_pressure: float = Field(..., alias="atmosphere_pressure")

    class Config:
        orm_mode = True


class CityWeatherResponse(BaseModel):
    name_city: Optional[str] = Field(None, alias="name_city")
    temperature: Optional[float] = Field(None, alias="temperature")
    dttm: Optional[datetime] = Field(None, alias="dttm")

    class Config:
        orm_mode = True
