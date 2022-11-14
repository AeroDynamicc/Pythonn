"""

#tervitused mõtisklustega 
def tervitus(x):
    for i in range(x):
        print("Võõrustaja: 'Tere!'")
        print(f"Täna {i+1} kord tervitada, mõtiskleb võõrustaja.")
        print("Külaline: 'Tere, suur tänu kutse eest!'")
n = int(input("Sisestage külaliste arv: "))
tervitus(n)   
    
        
     """   
    
"""

#peo eelarve
def eelarve(x):
    g = (x*10+55)
    return g
y = int(input("Mitu inimes on kutsutud: "))
u = int(input("Mitu inimest tuleb: "))
print(f"Maksimaalne eelarve: {eelarve(y)}")
print(f"Minimaalne eelarve: {eelarve(u)}")

"""

"""

#ounamahla tegemine
def mahlapakkide_arv(x):
    g = round(x*0.4/3)
    print(g)
y = float(input("Õunte kogus kilogrammides: "))
mahlapakkide_arv(y)

    
"""





#bänner
def banner(x):
    print(x.upper())

g = input("reklaamlause: ")

banner(g)

y = int(input("mitu korda soovite reklaami kuvada: "))
for i in range(y):
    banner(g)

    """
#tahvli juurde
from datetime import *
x = 1
fail = open("nimekiri.txt")
for i in range(fail):
    if x==datetime.now().day:
        print(x, rida, end="")
    x +=1

    
"""







#jukebox
#muusika = input("Sisestage faili nimi: ")
#x = 1
#fail = open(muusika)
#for rida in fail:
#    print(x, rida, end="")
#    x +=1
#    
#a = int(input("Vali laul: "))
#x = 1
#fail = open(a)
#for rida in fail:
#    if x==a:
#        print(x,rida,end="")
#    x +=1
#file.close()
