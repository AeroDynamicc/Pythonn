#Daniil Meijel
#01.11.22
#harjutus7


def Kuup(a):
    print(f"Kuubi ruumala on {a**3}")
    
def Koonus(r,h):
    print(f"Koonuse ruumala on {round(math.pi*r**2)*h/3,2}")
    
def kera(r):
    print(f"Kera ruumala on)
    
     

print("***********LEIAME RUUMALA***********")
loop = 1

while loop==1:
    print("Vali kujund: \n1.Kuup \n2.Kera \n3.Koonus \n4.Silinder")
    kujund = int(input("Lisa kujundi number 1-4: "))
    if kujund==1:
        x = int(input("Sisesta kuubi küljepikkus: "))
        Kuup(x)
    elif kujund==2:
        Kera()
    elif kujund==3:
        r = int(input("Sisesta koonuse põhja raadius: "))
        h = int(input("Sisesta koonuse kõrgus: "))
        Koonus(r,h)
    elif kujund==4:
        q=
        e=
        Silinder()
    else:
        print("***********\nPalun tee valik 1-4\n***********")
    


"""

#oma funktsiooni loomine paarmeetritega
def tervita(a="uknown", b="ge"):
    if b=="et":
        print(f"Tere {a}")
    elif b=="en":
        print(f"Hi {a}")
    else:
        print(f"Hallo {a}")
    
    
#funktsiooni väljakutsumine
tervita("Daniil","et")

"""





















"""
#tärnidega vanus
vanused = [54,68,54,23,56,78,90,45,12,60]
for i in vanused

"""






















"""

#vanused
vanused = [15,54,3,8,34,62,12,45,65,85]
print(f"Vanim {max(vanused)}")
print(f"Noorim {min(vanused)}")
print(f"Vanuste summa {sum(vanused)}")
print(f"Keskmine vanus {sum(vanused)}")

"""








"""
#duplikaadid
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
puh_opilased = []
for i in opilased:
    if i in opilased:
        if opilased.count(i) >= 2:
            opilased.remove(i)
"""    
    




















"""
#õpilased
g = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
for i in opilased:
    print(f"(g). (i)")
    g+=1
nr = int(input("millist nime tahad muuta?: "))
"""
"""
#Nimede lisamine loendisse
nimed = []
for i in range(5):
    nimi = input("Lisa nimi loendisse: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)
print(f"Viimati lisatud nimi: {nimed[-1]}")
"""
















