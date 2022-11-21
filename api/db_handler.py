from __future__ import annotations

import os

from motor import motor_asyncio


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs): # type: ignore
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBHandler(metaclass=Singleton):
    def __init__(self) -> None:
        self.client = motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
        self.db = self.client[os.environ["MONGODB_DB"]]
        self.queries = self.db["queries"]
        self.offers = self.db["offers"]