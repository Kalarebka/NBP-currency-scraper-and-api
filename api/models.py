from datetime import date
from enum import Enum
from typing import Generator, List

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
    average_rate: float = Field(...)


class CurrencyB(BaseCurrency):
    country: str = Field(...)
    average_rate: float = Field(...)


class CurrencyC(BaseCurrency):
    ask_rate: float = Field(...)
    bid_rate: float = Field(...)


class TableType(str, Enum):
    A = "A"
    B = "B"
    C = "C"


class Table(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    table_type: TableType = Field(...)
    date_published: date = Field(...)
    currency_rates: List[BaseCurrency] = Field(...)
