import csv
from ekipe import seznam_ekip
import funkcije

# Zapiše prvo vrstico CSV datoteke
atributi = funkcije.dobi_seznam_atributov("luka-doncic")
at = ["ime", "polozaj", "ekipa"] + atributi
with open(f"Informacije_o_igralcih.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(at)

# V CSV datoteko napiše igralce in vrednosti
for ekipa in seznam_ekip:
    igralci = funkcije.najdi_imena_igralcev(ekipa)
    print(ekipa)
    for igralec, polozaj in igralci:
        igralec_link = igralec.replace(' ', '-')
        vrednost = funkcije.dobi_vrednosti(igralec_link)
        if len(vrednost) != 0:
            x = vrednost.pop(26)
            x = vrednost[33:39 + 1]  # Ker so se nekatere vrednosti zapisovale 2x, jih s tem jih odstranimo
            vrednost[33:39 + 1] = []
            vre = [igralec, polozaj, ekipa] + vrednost
            with open(f"Informacije_o_igralcih.csv", "a", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(vre)
