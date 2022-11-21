from typing import Any

from celery import Celery
from celery.schedules import crontab

app = Celery("periodical_scraper")

app.config_from_object("celery_config")

@app.task(name="periodical_scraper.get_A_table_task")
def get_A_table_task():
    print("scraping table A")

@app.task(name="periodical_scraper.get_B_table_task")
def get_B_table_task():
    print("scraping table B")

@app.task(name="periodical_scraper.get_C_table_task")
def get_C_table_task():
    print("scraping table C")


@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs: Any) -> None:
    sender.add_periodic_task(
        crontab(hour="0", minute="1"),
        get_A_table_task.s(),
        name="",
    )
    sender.add_periodic_task(
        crontab(hour="0", minute="1"),
        get_B_table_task.s(),
        name="",
    )
    sender.add_periodic_task(
        crontab(hour="0", minute="1"),
        get_C_table_task.s(),
        name="",
    )