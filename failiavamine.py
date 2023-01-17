from tkinter import *
import tkinter.filedialog

#akna seaded
aken = Tk()
aken.title('Dialoogiaknad')
aken.geometry("200x200")

def vali_fail():
    faili_tyyp = [('Python failid', '*.py'), ('Kõik failid', '*')]
    nimi = tkinter.filedialog.Open(filetypes=faili_tyyp)
    valik = nimi.show()
    
    if valik != '':
        print(valik)

Button(aken, text = "Vali fail...", command = vali_fail).pack()

aken.mainloop()