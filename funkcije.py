import re
from bs4 import BeautifulSoup
import csv

def najdi_podetke_igralcev(ekipa):
    with open(f"{ekipa}.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    tab = soup.find('table', class_='table table-striped table-sm table-hover overflow-hidden mb-2')
    info = []
    if tab:
        for vrstica in tab.find_all("tr"):
            ime = vrstica.find("a", title=True)
            if ime:
                ime = ime.text.strip()
                najdi_visino = re.search(r'(\d{1,2})\'(\d{1,2})"', vrstica.text)
                visina = f"{najdi_visino.group(1)}'{najdi_visino.group(2)}\"" if najdi_visino else ""
                pos = [pos.strip() for pos in re.findall(r'PG |SG |C |PF |SF ', vrstica.text)]   
                info.append([ime, visina, ", ".join(pos)])
    return info


# Zapiše imena, ter podatke o igrlalcih v csv datoteko
def napisi_csv(info, ekipa):
    with open(f"Informacije_o_igralcih_{ekipa}.csv", "w", newline="", encoding="UTF8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Ime igralca", "Višina", "Igralni položaj"])
        for informacija in info:
            csv_writer.writerow(informacija)