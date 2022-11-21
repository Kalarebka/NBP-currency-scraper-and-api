from fastapi import APIRouter

from app.db_handler import DBHandler

router = APIRouter(prefix="/currency")
db = DBHandler()


@router.get("/{table}/{code}")
async def get_latest_rate():
    # return the latest exchange rate of the <code> currency from <table> table
    pass

@router.get("/{table}/{code}/today")
async def get_todays_rate():
    # returns rate from today or None
    pass

@router.get("/{table}/{code}")
async def get_rate_from_date():
    # return rate from that day or None
    pass

@router.get("/{table}/{code}/last/{count}")
async def get_last_n_rates():
    # return last n tables
    pass

@router.get("/{table}/{code}")
async def get_rates_date_range():
    # return rates from start_date to end_date
    pass