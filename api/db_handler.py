from __future__ import annotations

import os

from datetime import datetime
from typing import List, Optional

from motor import motor_asyncio


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
        self.currency = self.db["currency"]

    async def get_latest_table(self, table_type: TableType) -> List[dict]:
        latest_record = await self.currency.find_one(
            {"table": table_type}, {"_id": 0}, sort=[("date_published", -1)]
        )
        result = await self.currency.find(
            {
                "table": table_type,
                "date_published": latest_record["date_published"],
            },
            {"_id": 0},
        ).to_list(length=None)
        return result

    async def get_table_from_date(
        self, table_type: TableType, day: datetime
    ) -> Optional[List[dict]]:
        result = await self.currency.find(
            {"table": table_type, "date_published": day}, {"_id": 0}
        ).to_list(length=None)
        return result

    async def get_latest_currency(self, table_type: TableType, code: str) -> dict:
        result = await self.currency.find_one(
            {"table": table_type, "code": code},
            {"_id": 0},
            sort=[("date_published", -1)],
        )
        return result

    async def get_currency_from_date(
        self, table_type: TableType, code: str, day: datetime
    ) -> Optional[dict]:
        result = await self.currency.find_one(
            {"table": table_type, "code": code, "date_published": day}, {"_id": 0}
        )
        return result

    async def get_last_n_currency(
        self, table_type: TableType, code: str, n_results: int
    ) -> List[dict]:
        result: List[dict] = (
            await self.currency.find({"code": code, "table": table_type}, {"_id": 0})
            .sort("date_published", -1)
            .to_list(length=n_results)
        )
        return result

    async def get_currency_date_range(
        self, table_type: TableType, code: str, from_date: datetime, to_date: datetime
    ) -> List[dict]:
        result = await self.currency.find(
            {
                "code": code,
                "table": table_type,
                "date_published": {"$lte": to_date, "$gte": from_date},
            },
            {"_id": 0},
        ).to_list(length=None)
        return result
