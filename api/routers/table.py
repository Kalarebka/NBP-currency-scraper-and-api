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
