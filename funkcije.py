import re
from bs4 import BeautifulSoup
import csv
import requests
import import_requests

#Poišče imena igralcev, ter njihove osnovne podatke na začetni strani
def najdi_imena_igralcev(ekipa):
    with open(f"{ekipa}.html", "r", encoding="UTF8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    tab = soup.find('table', class_='table table-striped table-sm table-hover overflow-hidden mb-2')
    info = []
    if tab:
        for vrstica in tab.find_all("tr"):
            try:
                ime = vrstica.find("a", title=True)
                ime = ime.text.strip()
                pos = [pos.strip() for pos in re.findall(r'PG |SG |C |PF |SF ', vrstica.text)]  
                info.append([ime, pos])
            except Exception as e:
                continue
    return info

# Zapiše imena, ter podatke o igrlalcih v csv datoteko
def napisi_imena_csv(info, ekipa):
    with open(f"Informacije_o_igralcih_{ekipa}.csv", "w", newline="", encoding="UTF8") as csvfile:
        csv_writer = csv.writer(csvfile)
        for informacija in info:
            csv_writer.writerow(informacija)

def dobi_seznam_igralcev(csv_datoteka):
    with open(csv_datoteka, "r") as csvfile:
        igralci1 = []
        for vrstica in csv.reader(csvfile):
            igralci1.append(vrstica[0])
    igralci = [x.replace(' ', '-') for x in igralci1]
    return igralci

def dobi_seznam_plozajev(csv_datoteka):
    with open(csv_datoteka, "r") as csvfile:
        polozaji = []
        for vrstica in csv.reader(csvfile):
            polozaji.append(vrstica[1])
    return polozaji

#Dobi seznam kategorij, da jih lahko zapišemo v tabelo
def dobi_seznam_atributov(igralec):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"
    }
    stran = requests.get(f"https://www.2kratings.com/{igralec}", headers=headers)

    with open("igralec.html", "w", encoding="UTF8") as dat:
        dat.write(stran.text)

    with open(f"igralec.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    tab = soup.find('div', class_='row mr-md-n4')
    atributi = []  

    if tab is not None:
        bloki = tab.find_all('div', class_='card mb-3 mb-md-4 mr-2')
        for blok in bloki:
            vrstica = blok.find_all('li', class_="mb-1")    
            for vrednosti in vrstica:
                atribut = vrednosti.text.strip()
                vrednost = re.findall(r"\d{2}", vrednosti.text)
                if vrednost:
                    atributi.append(atribut)
    else:
        atributi = ["abc", "baaa"]  #Ta del kode prepreci errorje

    najdelsi = max(atributi, key=len) #Tu odstranimo eno od vrednosti, ki se ni shranila pravilno
    atributi.remove(najdelsi)  
    atributi = [re.sub(r'\d+', '', x) for x in atributi] #Ker so se vse vrednosti shranjevale v obliki: 34 Vrednost, jih tu preoblikujemo

    return atributi



#Poisce vrednosti za kategorije   
def dobi_vrednosti(igralec):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"}
    stran = requests.get(f"https://www.2kratings.com/{igralec}", headers=headers)

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
