from datetime import datetime, date, time
from typing import List, Optional

from fastapi import APIRouter

from api.db_handler import DBHandler
from api.models import BaseCurrency, CurrencyFactory, TableType

router = APIRouter(prefix="/table")
db = DBHandler()


@router.get("/")
async def get_latest_table(table: TableType) -> List[BaseCurrency]:
    # returns latest table
    result = await db.get_latest_table(table_type=table)
    return [CurrencyFactory.create(currency) for currency in result]


@router.get("/today")
async def get_todays_table(table: TableType) -> Optional[List[BaseCurrency]]:
    # returns table from today or None
    result = await db.get_table_from_date(
        table_type=table, day=datetime.combine(date.today(), time())
    )
    if result:
        return [CurrencyFactory.create(currency) for currency in result]
    return []


@router.get("/date")
async def get_table_from_date(
    table: TableType, day: date
) -> Optional[List[BaseCurrency]]:
    # return table from that day or None
    result = await db.get_table_from_date(
        table_type=table, day=datetime.combine(day, time())
    )
    if result:
        return [CurrencyFactory.create(currency) for currency in result]
    return []
