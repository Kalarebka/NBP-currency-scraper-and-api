import requests
import os, sys

from bs4 import BeautifulSoup

sys.path.insert(0, os.path.abspath(".."))

from scraper.db_handler import DBHandler
from scraper.models import TableType


BASE_URL = "https://www.nbp.pl/kursy/xml/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

db = DBHandler()


def get_table(url: str, table_type: TableType) -> None:
    xml_data = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(xml_data, "xml")

    table_data = {
        "date_published": soup.find("data_publikacji").text,
        "table_type": table_type,
        "currency_rates": [],
    }

    table_id = db.save_table_to_db(table_data)

    for currency in soup.find_all("pozycja"):
        currency_data = {
            "currency_name": currency.find("nazwa_waluty").text,
            "code": currency.find("kod_waluty").text,
            "multiplier": int(currency.find("przelicznik").text),
            "table_id": table_id
        }
        if table_type == TableType.A:
            currency_data["average_rate"] = float(
                currency.find("kurs_sredni").text.replace(",", ".")
            )
        elif table_type == TableType.B:
            country = currency.find("nazwa_kraju")
            if country:
                currency_data["country"] = country.text
            currency_data["average_rate"] = float(
                currency.find("kurs_sredni").text.replace(",", ".")
            )
        else:
            currency_data["bid_rate"] = float(
                currency.find("kurs_kupna").text.replace(",", ".")
            )
            currency_data["ask_rate"] = float(
                currency.find("kurs_sprzedazy").text.replace(",", ".")
            )

        db.save_currency_to_db(currency_data)

    


def get_table_filenames():
    # Create a list of filenames for tables from 2022
    filenames = requests.get(BASE_URL + "dir.txt")
    for filename in filenames.text.split("\n"):
        yield filename.strip()


if __name__ == "__main__":
    for filename in get_table_filenames():
        url = f"{BASE_URL}{filename}.xml"
        if filename[0] in "abc":
            get_table(url, filename[0].upper())
