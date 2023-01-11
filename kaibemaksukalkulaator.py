from tkinter import *


from tkinter import *

#akna seaded
aken = Tk()
aken.title('Nupud')
aken.geometry("245x175")

#funktsioonid
def tervita():
    nimi = sisestus.get()
    print("Tere " +nimi)

#sildid
silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=0,column=0)

silt = Label(aken, text="Käibemaksumäär:")
silt.grid(row=1,column=0)

silt = Label(aken, text="________________________________________________")
silt.grid(row=3,columnspan=2)

valjund1 = Label(aken, text="0.00€")
valjund1.grid(row=4,column=1)

valjund2 = Label(aken, text="0.00€")
valjund2.grid(row=5,column=1)

silt = Label(aken, text="Käibemaks:")
silt.grid(row=4,column=0)

silt = Label(aken, text="Hind käibemaksuga:")
silt.grid(row=5,column=0)

#valikukast
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=1,)
valikukast.grid(row=1,column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=2,)
valikukast.grid(row=2,column=1)

#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

#nupud
nupp1 = Button(aken, text="OK", width=10, command=tervita)
nupp1.grid(row=6, column=1)

aken.mainloop()





























