import requests

from bs4 import BeautifulSoup as bs

# from db_handler import DBHandler
from models import CurrencyA, CurrencyB, CurrencyC, Table


BASE_URL = "https://www.nbp.pl/kursy/xml/"
# db_handler = DBHandler()


def get_A_table(url: str):
    xml_data = requests.get(url).text
    soup = bs(xml_data, 'xml')
    table_data = {"date_published": soup.find("data_publikacji").text,
    "type": "A",
    "currency_rates": []}
    
    for currency in soup.find_all("pozycja"):
        currency_data = {
            "currency_name": currency.find("nazwa_waluty").text,
            "code": currency.find("kod_waluty").text,
            "multiplier": int(currency.find("przelicznik").text),
            "average_rate": float(currency.find("kurs_sredni").text.replace(",", "."))
        }
        table_data["currency_rates"].append(CurrencyA(**currency_data))
    print(table_data)



def get_B_table(url: str):
    pass


def get_C_table(url: str):
    pass


def get_table_filenames():
    # Create a list of filenames for tables from 2022
    filenames = requests.get(BASE_URL + "dir.txt")
    for filename in filenames.split("\n"):
        yield filename


if __name__ == "__main__":
    # for filename in get_table_filenames():
    #     url = f"{BASE_URL}{filename.strip()}.xml"
    #     if filename.startswith("a"):
    #         get_A_table(url)
    #     elif filename.startswith("b"):
    #         get_B_table(url)
    #     elif filename.startswith("c"):
    #         get_C_table(url)
    get_A_table("https://www.nbp.pl/kursy/xml/a012z210120.xml")
