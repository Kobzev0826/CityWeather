import os

import mysql.connector as sql


def get_connector():
    return sql.connect(
        host=os.environ['DB.HOST'],
        user=os.environ['DB.USER'],
        password=os.environ['DB.PASSWORD'],
        database=os.environ['DB.NAME']
    )
