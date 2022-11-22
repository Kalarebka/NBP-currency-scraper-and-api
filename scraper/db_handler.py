import os

from typing import List

from pymongo import MongoClient
from pymongo.database import Database

from scraper.models import Table


class DBHandler:
    def __init__(self) -> None:
        self.client: MongoClient = MongoClient(os.getenv("MONGODB_URL"))
        self.db: Database = self.client[os.getenv("MONGODB_DB")]
        self.tables = self.db["currency_tables"]

    def save_table_to_db(self, new_table: Table) -> str:
        new_table_id: str = self.tables.insert_one(new_table).inserted_id
        return new_table_id
