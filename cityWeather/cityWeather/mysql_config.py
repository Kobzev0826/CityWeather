import os

import mysql.connector as sql


def get_connector():
    return sql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE']
    )
