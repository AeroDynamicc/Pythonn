from tkinter import *


#akna seaded
aken = Tk()
aken.title('Mündid')
aken.geometry("200x100")

    
#pronksikarva_summa
def pronksikarva_summa(numbers):
    return sum([x for x in numbers if x in [1, 2, 5]])

filename = input("Sisesta faili nimi: ")

try:
    with open(filename) as file:
        numbers = [int(line.strip()) for line in file]
        result = pronksikarva_summa(numbers)
        print("Pronksikarva sentide summa: ", result)
except FileNotFoundError:
    print("Sellist faili ei leitud")
except ValueError:
    print("Failis on vigased andmed")


aken.mainloop()
























