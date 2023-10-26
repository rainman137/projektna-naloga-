import re
import csv
import requests
from bs4 import BeautifulSoup

# Poišče imena igralcev in njihove osnovne informacije na začetni strani
def najdi_imena_igralcev(ekipa):
    with open(f"{ekipa}.html", "r", encoding="UTF8") as datoteka:
        soup = BeautifulSoup(datoteka, "html.parser")
    
    tabela = soup.find('table', class_='table table-striped table-sm table-hover overflow-hidden mb-2')
    informacije = []
    
    if tabela:
        for vrstica in tabela.find_all("tr"):
            try:
                ime = vrstica.find("a", title=True)
                ime = ime.text.strip()
                polozaji = [polozaj.strip() for polozaj in re.findall(r'PG |SG |C |PF |SF ', vrstica.text)]
                informacije.append([ime, polozaji])
            except Exception as e:
                continue
    return informacije

# Dobi seznam atributov, da jih lahko zapišemo v tabelo
def dobi_seznam_atributov(igralec):
    glave = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"
    }
    stran = requests.get(f"https://www.2kratings.com/{igralec}", headers=glave)

    with open("igralec.html", "w", encoding="UTF8") as dat:
        dat.write(stran.text)

    with open(f"igralec.html", "r", encoding="utf-8") as datoteka:
        soup = BeautifulSoup(datoteka, "html.parser")

    tabela = soup.find('div', class_='row mr-md-n4')
    atributi = []

    if tabela is not None:
        bloki = tabela.find_all('div', class_='card mb-3 mb-md-4 mr-2')
        for blok in bloki:
            vrstice = blok.find_all('li', class_="mb-1")
            for vrednosti in vrstice:
                atribut = vrednosti.text.strip()
                vrednost = re.findall(r"\d{2}", vrednosti.text)
                if vrednost:
                    atributi.append(atribut)
    else:
        atributi = ["abc", "baaa"]  # Ta del kode prepreči napake

    najdaljsi = max(atributi, key=len)
    atributi.remove(najdaljsi)
    atributi = [re.sub(r'\d+', '', x) for x in atributi]

    return atributi

# Poišče vrednosti za kategorije   
def dobi_vrednosti(igralec):
    glave = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"}
    stran = requests.get(f"https://www.2kratings.com/{igralec}", headers=glave)

    with open("igralec.html", "w", encoding="UTF8") as dat:
        dat.write(stran.text)

    with open("igralec.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    tab = soup.find('div', class_='row mr-md-n4')
    
    vrednosti2 = []  

    if tab is not None:
        bloki = tab.find_all('div', class_='card mb-3 mb-md-4 mr-2')
        for blok in bloki:
            vrstica = blok.find_all('li', class_='mb-1')
            for vrednosti in vrstica:
                vrednost = re.findall(r"\d{2}", vrednosti.text)
                if vrednost:
                    vrednosti2.extend(vrednost)  

    return vrednosti2

