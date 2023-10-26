import csv
from ekipe import seznam_ekip
import funkcije


# Napiše imena igralcev v CSV datoteko
for ekipa in seznam_ekip:
    sez = funkcije.najdi_imena_igralcev(ekipa)
    funkcije.napisi_imena_csv(sez, ekipa)

# Zapiše prvo vrstico CSV datoteke
atributi = funkcije.dobi_seznam_atributov("luka-doncic")
at = ["ime", "polozaj", "ekipa"] + atributi
with open(f"Informacije_o_igralcih.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(at)

# V CSV datoteko napiše igralce in vrednosti
for ekipa in seznam_ekip:
    igralci = funkcije.dobi_seznam_igralcev(f"Informacije_o_igralcih_{ekipa}.csv")
    polozaji = funkcije.dobi_seznam_polozajev(f"Informacije_o_igralcih_{ekipa}.csv")
    print(ekipa)
    for igralec in igralci:
        vrednost = funkcije.dobi_vrednosti(igralec)
        if len(vrednost) != 0:
            x = vrednost.pop(26)
            x = vrednost[33:39 + 1]  # Ker so se nekatere vrednosti zapisovale 2x, jih s tem jih odstranimo
            vrednost[33:39 + 1] = []
            index = igralci.index(igralec)
            pos = polozaji[index]
            vre = [igralec, pos.strip('[]'), ekipa] + vrednost
            with open(f"Informacije_o_igralcih.csv", "a", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(vre)
