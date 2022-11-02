#Daniil Meijel
#02.11.2022
#harjutus10





import re

fh = open('utekst.txt')
for line in fh:
    if re.search('^[A-Z0-9]+[A-Z]{1}', line):
        print(line,end='')

print("------------------------")
#kuva korralikud paroolid
import re

fh = open('utekst.txt')
for line in fh:
    if re.search(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$") :


























