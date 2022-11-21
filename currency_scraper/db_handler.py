import os

from typing import List

from pymongo import MongoClient
from pymongo.database import Database


class DBHandler:
    def __init__(self) -> None:
        self.client: MongoClient = MongoClient(os.getenv("MONGODB_URL"))
        self.db: Database = self.client[os.getenv("MONGODB_DB")]

    def save_item_to_db(self):
        pass
