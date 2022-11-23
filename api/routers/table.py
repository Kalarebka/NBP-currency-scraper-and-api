from fastapi import APIRouter

from api.db_handler import DBHandler
from api.models import CURRENCY_TYPES, TableType

router = APIRouter(prefix="/table")
db = DBHandler()


@router.get("/{table}")
async def get_latest_table():
    # table - enum A/B/C, returns latest table
    pass


@router.get("/{table}/today")
async def get_today_table():
    # returns table from today or None
    pass


@router.get("/{table}/{date}}")
async def get_table_from_date():
    # return table from that day or None
    pass


@router.get("/{table}/last/{count}")
async def get_last_n_tables():
    # return last n tables
    pass


@router.get("/{table}/{start_date}/{end_date}")
async def get_tables_date_range():
    # return tables from start_date to end_date
    pass
