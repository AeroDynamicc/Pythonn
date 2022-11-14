#Daniil Meijel
#14.11.2022
#iseseisvad harjutused



#bänner
def banner(x):
    print(x.upper())

g = input("Reklaamlause: ")

banner(g)

y = int(input("Mitu korda soovite reklaami kuvada: "))
for i in range(y):
    banner(g)