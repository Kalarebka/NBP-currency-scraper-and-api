import os

from typing import List

from pymongo import MongoClient
from pymongo.database import Database


class DBHandler:
    def __init__(self) -> None:
        self.client: MongoClient = MongoClient(os.getenv("MONGODB_URL"))
        self.db: Database = self.client[os.getenv("MONGODB_DB")]
        self.tables = self.db["currency_tables"]
        self.currency_rates = self.db["currency_rates"]

    def save_table_to_db(self, new_table: dict) -> str:
        new_table_id: str = self.tables.insert_one(new_table).inserted_id
        return new_table_id

    def save_currency_to_db(self, new_currency: dict) -> str:
        new_currency_id: str = self.currency_rates.insert_one(new_currency).inserted_id
        return new_currency_id
