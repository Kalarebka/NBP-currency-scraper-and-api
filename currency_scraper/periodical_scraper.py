from typing import Any

from celery import Celery
from celery.schedules import crontab

from archive_scraping import BASE_URL, get_A_table, get_B_table, get_C_table

app = Celery("periodical_scraper")

app.config_from_object("celery_config")


@app.task(name="periodical_scraper.get_A_table_task")
def get_A_table_task():
    get_A_table(BASE_URL + "LastA.xml")


@app.task(name="periodical_scraper.get_B_table_task")
def get_B_table_task():
    get_B_table(BASE_URL + "LastB.xml")


@app.task(name="periodical_scraper.get_C_table_task")
def get_C_table_task():
    get_C_table(BASE_URL + "LastC.xml")


@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs: Any) -> None:
    sender.add_periodic_task(
        crontab(hour="0", minute="1"),
        get_A_table_task.s(),
        name="get table A on workdays after 12:15",
    )
    sender.add_periodic_task(
        crontab(hour="0", minute="1"),
        get_B_table_task.s(),
        name="get atble B on Wednesdays after 12:15",
    )
    sender.add_periodic_task(
        crontab(hour="0", minute="1"),
        get_C_table_task.s(),
        name="get table C on workdays after 8:15",
    )
