import requests
from bs4 import BeautifulSoup
from ekipe import seznam_ekip

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"}


stran = requests.get(
    "https://www.2kratings.com/teams/dallas-mavericks",
    headers=headers
)

with open("{ekipa}.html", "w", encoding="UTF8") as dat:
    dat.write(stran.text)
for ekipa in seznam_ekip:
    stran = requests.get(
        f"https://www.2kratings.com/teams/{ekipa}", headers=headers
    )
    with open(f"{ekipa}.html", "w", encoding="UTF8") as dat:
        dat.write(stran.text) 
