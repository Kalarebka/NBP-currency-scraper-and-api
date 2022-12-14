from datetime import date, datetime, time
from typing import List, Optional

from fastapi import APIRouter

from api.db_handler import DBHandler
from api.models import BaseCurrency, CurrencyFactory, TableType

router = APIRouter(prefix="/currency")
db = DBHandler()


@router.get("/")
async def get_latest_rate(table: TableType, code: str) -> Optional[BaseCurrency]:
    # return the latest exchange rate of the <code> currency from <table> table
    result: dict = await db.get_latest_currency(table_type=table, code=code)
    response: Optional[BaseCurrency] = CurrencyFactory.create(result)
    return response


@router.get("/today")
async def get_todays_rate(table: TableType, code: str) -> Optional[BaseCurrency]:
    # return rate from today or None
    result: Optional[dict] = await db.get_currency_from_date(
        table_type=table, code=code, day=datetime.today()
    )
    if result:
        response: Optional[BaseCurrency] = CurrencyFactory.create(result)
        return response
    return None


@router.get("/date")
async def get_rate_from_date(
    table: TableType, code: str, day: date
) -> Optional[BaseCurrency]:
    # return rate from that day or None
    result: Optional[dict] = await db.get_currency_from_date(
        table_type=table, code=code, day=datetime.combine(day, time())
    )
    if result:
        response: Optional[BaseCurrency] = CurrencyFactory.create(result)
        return response
    return None


@router.get("/last-count")
async def get_last_n_rates(
    table: TableType, code: str, count: int
) -> List[BaseCurrency]:
    # return last n currency rates
    result = await db.get_last_n_currency(table_type=table, code=code, n_results=count)
    return [CurrencyFactory.create(currency) for currency in result]


@router.get("/range")
async def get_rates_date_range(
    table: TableType, code: str, start_date: date, end_date: date
) -> List[BaseCurrency]:
    # return rates between two dates (inclusive)
    result = await db.get_currency_date_range(
        table_type=table,
        code=code,
        from_date=datetime.combine(start_date, time()),
        to_date=datetime.combine(end_date, time()),
    )
    return [CurrencyFactory.create(currency) for currency in result]
