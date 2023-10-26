# Analiza NBA igralcev

Iz spletne strani https://www.2kratings.com sem zajel podatke, o igralcih in jih analiziral.

Zajeti podatki vključujejo:
* Ime igralca
* Ekipo, v kateri igra igralec
* Igralčev igralni položaj
* Vrednosti vseh njegovih statističnih podatkov


## Navodila za zagon
Z datoteko [prenos.py](prenos.py) prenesemo html datoteke vseh NBA ekip na spletni strani https://www.2kratings.com. Potem z datoteko [tebele.py](tabele.py) iz spletnih strani izluščimo imena igralcev, ter njihove igralne položaje, kar shranimo v [Informacije_o_igralcih.csv](Informacije_o_igralcih.csv). Nato program prebere csv datoteke in za vsakega igralca iz spletnih strani izlušči njegove atribute. Atributi so nato analizirani v datoteki [analiza.ipynb](analiza.ipnyb). V datoteki [funkcije.py](funkcije.py) so shranjene vse funkcije, ki so bile uporabljene pri prenašanju podatkov.
Za pogon kode so potrebne naslednje knjižnice:
* requests
* re
* csv
* BeautifulSoup



