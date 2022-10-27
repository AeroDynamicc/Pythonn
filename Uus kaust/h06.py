#Daniil Meijel
#27.10.2022
#harjutus6

minu_fail = open("s6pru_l6ustaraamatus.txt", "r")

reformikad = 0
kesikud = 0
erakonnad = []


for i in minu_fail.readlines():
    enimi,pnimi,er,palk = i.split(" ")
    if er=="RE":
        reformikad+=1
    elif er=="KE":
        kesikud+=1
    if er not in erakonnad:
        erakonnad.append(er)
        
#poliitikute nimed
    with open('kirjutamine.txt','a') as fail_kirjutamiseks:
        fail_kirjutamiseks.write(enimi + " " + pnimi + "\n")

    
        
        
print(f"Reformikaid kokku: {reformikad}")
print(f"Kesikuid kokku: {kesikud}")
print(f"Erakondi kokku: {erakonnad}")



minu_fail.close



#Andra      Veidemann  SDE        3469      
#Evelyn     Sepp       KE         3569      
#Juku-Kalle Raid       IRL        4275      
#Jörgen     Siil       SDE        1865      
#Keit       Pentus     RE         3026      
#Kristiina  Ojuland    RE         4067      
#Liisa      Pakosta    IRL        2455      
#Margus     Tsahkna    IRL        2534      
#Marko      Mihkelson  RE         1504      
#Mart       Laar       IRL        2711  





















































