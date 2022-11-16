#Daniil Meijel
#16.11.2022
#iseseisvad harjutused

"""
#kuupäevad
def kuu1(o):
    kuud = ["","jaan","veeb","dets","dets","dets","dets","dets","dets","dets","dets","dets","dets","dets"]
    return kuud[o]

def kuu2(u):
    print(f"11.{u} 2022")

kp = input("Lisa kp: ")
p,k,a = kp.split(".")
kuu2(kuu1(int(k)))
"""


"""

#tervitused
def tervitus(o):
    print("Võõrustaja: 'Tere!'")
    print(f"Tänan {o+1} kord tervitada, Mõtiskleb võõrustaja.")
    print("Külaline: 'Tere, suur tänu kutse eest!'")
a = int(input("Sisestage külaliste arv: "))
for i in range(a):
    tervitus(i)

"""

"""

#eelarve
def eelarve(o):
    f = (o*10+55)
    return f
a = int(input("Mitu inimest on kutsutud?: "))
b = int(input("Mitu inimest tuleb?: "))
print(f"Maksimaalne eelarve: {eelarve(a)}")
print(f"Minimaalne eelarve: {eelarve(b)}")

"""




