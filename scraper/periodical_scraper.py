from typing import Any

from celery import Celery
from celery.schedules import crontab

from scraper.archive_scraping import BASE_URL, get_table
from scraper.models import TableType


app = Celery("periodical_scraper")

app.config_from_object("scraper.celery_config")


@app.task(name="periodical_scraper.get_A_table_task")
def get_A_table_task() -> None:
    get_table(BASE_URL + "LastA.xml", TableType.A)


@app.task(name="periodical_scraper.get_B_table_task")
def get_B_table_task() -> None:
    get_table(BASE_URL + "LastB.xml", TableType.B)


@app.task(name="periodical_scraper.get_C_table_task")
def get_C_table_task() -> None:
    get_table(BASE_URL + "LastC.xml", TableType.C)


@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs: Any) -> None:
    sender.add_periodic_task(
        crontab(hour=12, minute=30, day_of_week="1-5"),
        get_A_table_task.s(),
        name="get table A on workdays after 12:15",
    )
    sender.add_periodic_task(
        crontab(hour=4, minute=0, day_of_week="wed"),
        get_B_table_task.s(),
        name="get table B on Wednesdays after 12:15",
    )
    sender.add_periodic_task(
        crontab(hour=8, minute=30, day_of_week="1-5"),
        get_C_table_task.s(),
        name="get table C on workdays after 8:15",
    )
