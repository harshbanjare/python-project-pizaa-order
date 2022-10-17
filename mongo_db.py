import pymongo
from dotenv import load_dotenv
import os
import pprint
import certifi


class DB:
    def __init__(self) -> None:
        load_dotenv()
        self.__user = os.getenv("MONGO_USER")
        self.__password = os.getenv("MONGO_PASSWORD")
        self._client = pymongo.MongoClient(
            f"mongodb+srv://{self.__user}:{self.__password}@instance.hmqd8.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
        self._db = self._client['pizza-delivery-system']
        self._collections = self._db['orders']

    def insert(self, data):
        self._collections.insert_one(data)

    def update(self, data, where):
        self._collections.update_one(where, data)

    def delete(self, where):
        self._collections.delete_one(where)

    def select(self, where):
        return self._collections.find(where)

    def select_all(self):
        return self._collections.find({})


class Orders(DB):
    def __init__(self):
        super().__init__()
        self._table = "orders"

    def get_next_order_id(self):
        return self._collections.count_documents({}) + 1

    def create_order(self, id, name, email, phone, address, type):
        data = {
            "id": id,
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "type": type,
            "status": "PENDING"
        }
        print(data)

        if not (name and email and phone and address and type):
            return False

        try:
            self.insert(data)
            return True
        except Exception as e:
            print(e)
            return False

    def update_status(self, id, status):
        data = {"$set": {"status": status}}
        where = {"id": int(id)}
        try:
            self.update(data, where)
            return True
        except Exception as e:
            print(e)
            return False

    def get_order_status(self, id):
        status = self._collections.find_one({"id": int(id)})
        if status:
            return status['status']
        else:
            return False

    def get_pending_orders(self):
        orders = self.select({"status": "PENDING"})
        orders_tuple = []
        for order in orders:
            l = list(order.values())
            l.pop(0)
            orders_tuple.append(tuple(l))

        if orders:
            return tuple(orders_tuple)
        else:
            return False

    def get_served_orders(self):
        orders = self.select({"status": "IN TRANSIT"})
        orders_tuple = []
        for order in orders:
            l = list(order.values())
            l.pop(0)
            orders_tuple.append(tuple(l))

        if orders:
            return tuple(orders_tuple)
        else:
            return False

    def get_cancelled_orders(self):
        orders = self.select({"status": "CANCELLED"})
        orders_tuple = []
        for order in orders:
            l = list(order.values())
            l.pop(0)
            orders_tuple.append(tuple(l))

        if orders:
            return tuple(orders_tuple)
        else:
            return False

    def cancel_order(self, id):
        return self.update_status(id, "CANCELLED")


if __name__ == "__main__":
    orders = Orders()
    # print(orders.update_status(1, "DELIVERED"))
    # print(orders.select({"id": 1}))
    # print(orders.get_order_status(1))
    # print(orders.get_next_order_id())
    pprint.pprint(orders.get_pending_orders())
    # pprint.pprint([i for i in orders.select_all()])
