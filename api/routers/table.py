from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter

from api.db_handler import DBHandler
from api.models import BaseCurrency, CurrencyFactory, TableType

router = APIRouter(prefix="/table")
db = DBHandler()


@router.get("/{table}")
async def get_latest_table(table: TableType) -> List[BaseCurrency]:
    # returns latest table
    result = await db.get_latest_table(table_type=table)
    return [CurrencyFactory.create(currency) for currency in result]


@router.get("/{table}/today")
async def get_todays_table(table: TableType) -> Optional[List[BaseCurrency]]:
    # returns table from today or None
    result = await db.get_table_from_date(table_type=table, day=datetime.today())
    if result:
        return [CurrencyFactory.create(currency) for currency in result]
    return []


@router.get("/{table}/{date}}")
async def get_table_from_date(
    table: TableType, day: datetime
) -> Optional[List[BaseCurrency]]:
    # return table from that day or None
    result = await db.get_table_from_date(table_type=table, day=day)
    if result:
        return [CurrencyFactory.create(currency) for currency in result]
    return []
