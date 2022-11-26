import os

from pymongo import MongoClient
from pymongo.database import Database


class DBHandler:
    def __init__(self) -> None:
        self.client: MongoClient = MongoClient(os.getenv("MONGODB_URL"))
        self.db: Database = self.client[os.getenv("MONGODB_DB")]
        self.currency = self.db["currency"]

    def save_currency_to_db(self, new_currency: dict) -> str:
        new_currency_id: str = self.currency.insert_one(new_currency).inserted_id
        return new_currency_id
