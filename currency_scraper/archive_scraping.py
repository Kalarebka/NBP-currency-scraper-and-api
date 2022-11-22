import requests

from bs4 import BeautifulSoup

from db_handler import DBHandler
from models import CurrencyA, CurrencyB, CurrencyC, Table, TableType


BASE_URL = "https://www.nbp.pl/kursy/xml/"
HEADERS = {'User-Agent': 'Mozilla/5.0'}
CURRENCY_TYPES = {"A": CurrencyA, "B": CurrencyB, "C": CurrencyC}

db = DBHandler()


def get_table(url: str, table_type: TableType):
    xml_data = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(xml_data, "xml")

    table_data = {
        "date_published": soup.find("data_publikacji").text,
        "table_type": table_type,
        "currency_rates": [],
    }

    for currency in soup.find_all("pozycja"):
        currency_data = {
            "currency_name": currency.find("nazwa_waluty").text,
            "code": currency.find("kod_waluty").text,
            "multiplier": int(currency.find("przelicznik").text),
        }
        if table_type == TableType.A:
            currency_data["average_rate"] = float(
                currency.find("kurs_sredni").text.replace(",", ".")
            )
        elif table_type == TableType.B:
            currency_data["country"] = currency.find("nazwa_kraju").text
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

        table_data["currency_rates"].append(CURRENCY_TYPES[table_type](**currency_data))
    db.save_table()


def get_table_filenames():
    # Create a list of filenames for tables from 2022
    filenames = requests.get(BASE_URL + "dir.txt")
    for filename in filenames.split("\n"):
        yield filename.strip()


if __name__ == "__main__":
    for filename in get_table_filenames():
        url = f"{BASE_URL}{filename}.xml"
        if filename[0] in "abc":
            get_table(url, filename[0].upper())
