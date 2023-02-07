# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector as sql

class CityweatherPipeline:

    def __init__(self):
        self.con = sql.connect(
            host = 'localhost',
            user = 'user',
            password = '123456',
            database = 'city_weather'
        )
        self.cur = self.con.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS cityWeather(
                id int not NULL auto_increment,
                city_id int,
                temperature decimal(4,2),
                wind_speed decimal(6,2),
                atmosphere_pressure int,
                date datetime,
                PRIMARY KEY (id)
                )
        """)

    def process_item(self, item, spider):
        ## Define insert statement
        print(f"city_id={item['city_id']}")
        items = ( item["city_id"], item["temperature"], item["wind_speed"],item["atmosphere_pressure"])
        print("items: " , items)
        self.cur.execute(""" insert into cityWeather (city_id, temperature, wind_speed,atmosphere_pressure, date ) values (%s,%s,%s,%s,now())""", items)

        ## Execute insert of data into database
        self.con.commit()

    def close_spider(self, spider):
        ## Close cursor & connection to database
        self.cur.close()
        self.con.close()