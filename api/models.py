from datetime import date, datetime, time
from enum import Enum
from typing import Generator, Optional

from bson import ObjectId
from pydantic import BaseModel, Field


# from mongodb.com; convert bson ObjectIds to strings
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls) -> Generator:
        yield cls.validate

    @classmethod
    def validate(cls, v: str) -> ObjectId:
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema: dict) -> None:
        field_schema.update(type="string")



class BaseCurrency(BaseModel):
    currency_name: str = Field(...)
    code: str = Field(...)
    multiplier: int = Field(...)


class CurrencyA(BaseCurrency):
    # kurs średni
    pass


class CurrencyB(BaseCurrency):
    # nazwa kraju, kurs średni
    pass


class CurrencyC(BaseCurrency):
    # kurs kupna, kurs sprzedaży
    pass


class Table(BaseModel):
    pass
    


