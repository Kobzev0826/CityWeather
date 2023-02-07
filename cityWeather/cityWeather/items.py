# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CityweatherItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city_id = Field()
    temperature = Field()
    wind_speed = Field()
    atmosphere_pressure = Field()
