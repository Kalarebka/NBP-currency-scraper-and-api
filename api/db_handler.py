from __future__ import annotations

import os, sys

from datetime import date
from typing import List

from motor import motor_asyncio

sys.path.insert(0, os.path.abspath(".."))

from api.models import TableType


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):  # type: ignore
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBHandler(metaclass=Singleton):
    def __init__(self) -> None:
        self.client = motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
        self.db = self.client[os.environ["MONGODB_DB"]]
        self.tables = self.db["currency_tables"]

    async def get_latest_table(self, table_type: TableType) -> dict:
        pass

    async def get_table_from_date(self, table_type: TableType, day: date) -> dict:
        pass

    async def get_last_n_tables(
        self, table_type: TableType, num_tables: int
    ) -> List[dict]:
        pass

    async def get_tables_date_range(
        self, table_type: TableType, from_date: date, to_date: date
    ) -> List[dict]:
        pass

    async def get_latest_currency(self, table_type: TableType, code: str) -> dict:
        result = self.tables.find().sort({"date_published": -1}).limit(1)
        return result

    async def get_currency_from_date(
        self, table_type: TableType, code: str, day: date
    ) -> dict:
        pass

    async def get_last_n_currency(
        self, table_type: TableType, code: str, n_results: int
    ) -> List[dict]:
        pass

    async def get_currency_date_range(
        self, table_type: TableType, code: str, from_date: date, to_date: date
    ) -> List[dict]:
        pass
