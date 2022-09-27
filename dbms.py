import pymysql

HOST = 'technical.timepvp.in'
PORT = 3306
USER = 'u2_i4YRrBdoQW'
PASSWORD = 'MO4HI7.^!Cq^62^n2gL6XPs9'
DATABASE = 's2_test'


class Db:
    def __init__(self):
        self._host = HOST
        self._port = PORT
        self._user = USER
        self._password = PASSWORD
        self._database = DATABASE
        self._connection = pymysql.connect(
            host=self._host, port=self._port, user=self._user, password=self._password, database=self._database)

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
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = "DELETE FROM " + table + " WHERE " + where
            cursor.execute(sql)
        self.connection.commit()

    # select data from database
    def select(self, table, where):
        with self._connection.cursor() as cursor:
            # Create a new record
            sql = "SELECT * FROM " + table + " WHERE " + where
            cursor.execute(sql)
            result = cursor.fetchall()
        return result
