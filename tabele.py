from bs4 import BeautifulSoup
from ekipe import seznam_ekip
import funkcije


# Load the HTML content from "Atlanta-Hawks.html" or your HTML file
for ekipa in seznam_ekip:
    sez = funkcije.najdi_podetke_igralcev(ekipa)
    funkcije.napisi_csv(sez, ekipa)

for ekipa in seznam_ekip:
    igralci = funkcije.dobi_seznam_igralcev(f"Informacije_o_igralcih_{ekipa}.csv")
    atributi = funkcije.dobi_seznam_atributov(igralci[0])
    at = ["ime"] + atributi
    print(ekipa)
    with open(f"Informacije_o_igralcih111_{ekipa}.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(at)
    for igralec in igralci:
        vrednost = funkcije.dobi_vrednosti(igralec)
        vre = [igralec] + vrednost
        with open(f"Informacije_o_igralcih111_{ekipa}.csv", "a", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(vre)
            print(igralec)
