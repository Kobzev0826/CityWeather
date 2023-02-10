# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from cityWeather.mysql_config import get_connector


class CityweatherPipeline:

    def __init__(self):
        self.con = get_connector()
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        ## Define insert statement
        print(f"city_id={item['city_id']}")
        items = (item["city_id"], item["temperature"], item["wind_speed"], item["atmosphere_pressure"])

        self.cur.execute(
            f""" insert into cityWeather (city_id, temperature, wind_speed, atmosphere_pressure, dttm ) 
            values ({items[0]},{items[1]},{items[2]},{items[3]},now())""")
        print("items1: ", items)
        ## Execute insert of data into database
        self.con.commit()
        print("items2: ", items)

    def close_spider(self, spider):
        ## Close cursor & connection to database
        self.cur.close()
        self.con.close()
