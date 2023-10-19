from bs4 import BeautifulSoup
from ekipe import seznam_ekip
import funkcije


# Load the HTML content from "Atlanta-Hawks.html" or your HTML file
for ekipa in seznam_ekip:
    sez = funkcije.najdi_podetke_igralcev(ekipa)
    funkcije.napisi_csv(sez, ekipa)