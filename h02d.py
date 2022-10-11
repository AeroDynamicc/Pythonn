#Daniil Meijel
#11.10.22
#Ülesanne02
import math



km = 400
l = 26
v = l/(km*100)
print(v)




#arvusüsteemid
b = int(input("sisesta täisarv: "))
print("2ndsüsteemis:", bin(b))
print("16ndsüsteemis:", hex(b))



#ajateisendus
aeg = int(input("Sisesta minutid: "))
tunnid = aeg // 60 #täisarvuline jagamine
minutid = aeg % 60 #jääk
print("Vastus:",minutid,":",tunnid)








#hüpotenuus
a,b = 16,9
c = round(math.sqrt(pow(a,2) + b**2),2)
print("Kolmnurga hüpo on:",c)




#rulluisutajad
kiirus = 29.9
aeg = 24
kaugus = round(kiirus/60*aeg,2)
print("Sportlane jõuab",kaugus,"km")





#pitsa
hind = 12.9
tip = 0.1
kogus = 3
summa = (hind+hind*tip)/kogus
print(kogus,"Iga tüüp maksab",summa,"eurot")








#toote hind
hind = 36.75
ale = 0.4
kogus = 3
summa = round((hind-hind*ale)*3,2)
print(kogus,"toote summa on",summa,"eurot")








#kolmnurga ümbermõõt
a,b,c = 5,5,5
p = a + b + c
print("Kolmnurga ümbermõõt on: ", p)
















