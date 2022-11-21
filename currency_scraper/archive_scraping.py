import requests

from datetime import date

from bs4 import BeautifulSoup as bs


BASE_URL = "https://www.nbp.pl/kursy/xml/"


def get_table_filenames():
    # Create a list of filenames for tables from 2022
    filenames = requests.get(BASE_URL + "dir.txt")
    for filename in filenames.split("\n"):
        yield filename


def get_A_table(url: str):
    pass

def get_B_table(url: str):
    pass
   
def get_C_table(url: str):
    pass



if __name__ == "__main__":
    for filename in get_table_filenames():
        url = f"{BASE_URL}{filename.strip()}.xml"
        if filename.startswith("a"):
            get_A_table(url)
        elif filename.startswith("b"):
            get_B_table(url)
        elif filename.startswith("c"):
            get_C_table(url)
   