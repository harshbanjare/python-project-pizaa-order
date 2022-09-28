import imp
from msilib.schema import tables
import pymysql
from dotenv import load_dotenv
import os


class Db:
    def __init__(self):
        load_dotenv()
        self._host = os.getenv("DB_HOST")
        self._port = int(os.getenv("DB_PORT"))
        self._user = os.getenv("DB_USER")
        self._password = os.getenv("DB_PASSWORD")
        self._database = os.getenv("DB_DATABASE")
        self._connection = pymysql.connect(
            host=self._host, port=self._port, user=self._user, password=self._password, database=self._database)

        self._table = "Order"

    # insert data into database
    def insert(self, table, data):
        with self._connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO " + table + " VALUES " + data
            cursor.execute(sql)
        self._connection.commit()

    # update data in database
    def update(self, table, data, where):
        with self._connection.cursor() as cursor:
            # Create a new record
            sql = "UPDATE " + table + " SET " + data + " WHERE " + where
            cursor.execute(sql)
        self._connection.commit()

    # delete data from database
    def delete(self, table, where):
        with self._connection.cursor() as cursor:
            # Create a new record
            sql = "DELETE FROM " + table + " WHERE " + where
            cursor.execute(sql)
        self._connection.commit()

    # select data from database
    def select(self, table, where):
        with self._connection.cursor() as cursor:
            # Create a new record
            sql = "SELECT * FROM " + table + " WHERE " + where
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def get_next_order_id(self):
        with self._connection.cursor() as cursor:
            # Create a new record
            sql = "SELECT * FROM " + self._table + " ORDER BY Id DESC LIMIT 1"
            cursor.execute(sql)
            result = cursor.fetchall()
        return len(result) + 1
