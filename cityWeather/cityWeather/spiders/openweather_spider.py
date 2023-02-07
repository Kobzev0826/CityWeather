import mysql.connector as sql
import scrapy
from cityWeather.items import CityweatherItem
from cityWeather.mysql_config import get_connector

class OpenWeather(scrapy.Spider):
    name = 'openweather_spider'

    def get_cities_id(self):
        self.con = get_connector()
        self.cur = self.con.cursor(buffered=True)
        self.cur.execute("""
            select city_id from cities
            """)
        city_ids = self.cur.fetchall()
        print("ids: ",city_ids)
        self.cur.close()
        self.con.close()
        return city_ids

    def get_start_links(self):
        id_list = self.get_cities_id()
        start_urls = []
        for city_id in id_list:
            start_urls.append(
                f'https://openweathermap.org/data/2.5/weather?id={city_id[0]}&appid=439d4b804bc8187953eb36d2a8c26a02')
        return start_urls

    def start_requests(self):
        for url in self.get_start_links():
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        print(response.json())
        item = CityweatherItem()
        response = response.json()
        item['temperature'] = response['main']['temp']
        item['city_id'] = response['id']
        item['wind_speed'] = response['wind']['speed']
        item['atmosphere_pressure'] = response['main']['pressure']
        yield item
