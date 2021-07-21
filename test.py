from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()

var = IntVar()
var.set(1)

R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

def create_radio():
   radio_var = IntVar()
   radio_var.set(1)

   radio1 = Radiobutton(root, text = 'inches', variable = radio_var, value = 1)#, indicatoron = 0)
   radio1.configure()#bg = gray_medium, fg = orange)
   radio1.pack()

   radio2 = Radiobutton(root, text = 'feet', variable = radio_var, value = 2)#, indicatoron = 0)
   radio2.configure()#bg = gray_medium, fg = orange)
   radio2.pack()

label = Label(root)
label.pack()
create_radio()
root.mainloop()