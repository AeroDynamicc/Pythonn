from tkinter import *

#akna seaded
aken = Tk()
aken.resizable(0,0)
aken.title("Kalkulaator")
aken.geometry("200x200")
tekst = Label(aken,
              text="Siia tuleb Vastus!",
              font = "Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=0, column=0, columnspan=4)







#nupud
nupp1 = Button(aken, text="1",width=4, font = "Tahoma 12")
nupp1.grid(row=1, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="2",width=4, font = "Tahoma 12")
nupp2.grid(row=1, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="3",width=4, font = "Tahoma 12")
nupp3.grid(row=1, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="4",width=4, font = "Tahoma 12")
nupp4.grid(row=1, column=3, padx=2, pady=2)














aken.mainloop()