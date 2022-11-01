#Daniil Meijel
#01.11.2022
#harjutus09

import locale
import datetime

#Tekita tänane kuupäev ning esita kujul 16. June 2016
aeg = datetime.datetime.now()
print(aeg.strftime("%d. %B %Y"))

#Kuva eestistatud kuupäev kujul 16. Juuni 2016
locale.setlocale(locale.LC_ALL, "et_EE")
print(aeg.strftime("%d. %B %Y"))


#Eralda isikukoodist sünnikuupäev ja leia isiku vanus
ik="50603117019"
sp = datetime.date(int("20"+ik[1:3]), int(ik[3:5]), int(ik[5:7]))
print(sp)
print(aeg.year-sp.year) 




















