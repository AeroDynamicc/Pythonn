#Daniil Meijel
#teadmiste kontroll
#harjutus_1
#21.11.2022

#arvu sisestamine
num = int(input("Sisesta number: "))
if (num % 2) == 0:
    print("{0} on Paaris".format(num))
else:
    print("{0} on Paaritu".format(num))
    
with open ('numbrid.txt', 'w') as file:
    file.write('3 on Paaritu')



    


















