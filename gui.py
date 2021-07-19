#GUI 

from tkinter import *

#colors_used
orange = '#FA9605'
gray = '#3B3B3C'
gray_medium = '#4F4F51'
gray_light = '#9D9FA2'

root = Tk()
root.geometry('630x540')
root.title('proportion tool for Debra')
root.configure(bg = gray)

#title_image = PhotoImage(file = 'resources/images/title_image.gif')

sub_window = Frame(root, bg = gray, width = 610, height = 600, relief = 'solid', bd = 1)
sub_window.grid(row = 0, column = 0, padx = 10, pady = 10)
title_label = Label(
    sub_window,
    #image = title_image,
    text = 'Proportion Tool', font = ('Times', 40),
    bg = gray,
    fg = orange,
    padx = 5,
    pady = 4
    )

title_label.grid(row = 0, column = 0)


class Field:
    def __init__(self):

        self.frame = Frame(sub_window, bg = gray_medium, width = 600, height = 40)
        self.label = Label(self.frame, bg = gray_medium, fg = orange, width = 20, font = ('Ariel', 15))
        self.entry = Entry(self.frame, bg = gray_light, fg = 'white', width = 10, relief = 'flat', font = ('Ariel', 15))

        self.radio_var = IntVar()
        self.radio_var.set(1)

        self.radio1 = Radiobutton(self.frame, text = 'inches', variable = self.radio_var, value = 1, width = 5, font = ('Ariel', 15))
        self.radio1.configure(bg = gray_medium, fg = orange)
        #self.radio1.select()

        self.radio2 = Radiobutton(self.frame, text = 'feet', variable = self.radio_var, value = 2, width = 5, font = ('Ariel', 15))
        self.radio2.configure(bg = gray_medium, fg = orange)



    def show(self, num = 1):
        self.frame.grid(row = num, column = 0, padx = 5, pady = 10)
        self.frame.grid_propagate(0)
        self.label.grid(row = 0, column = 0, padx = 10, pady = 5)
        self.entry.grid(row = 0, column = 1, padx = 10, pady = 5)
        self.radio1.grid(row = 0, column = 2 )
        self.radio2.grid(row = 0, column = 3 )   


def create_fields():
    fields = [Field() for num in range(5)]
    num = 1
    for field in fields:
        field.show(num)
        num +=1

    fields[0].label.configure(text = 'Current Height')
    fields[1].label.configure(text = 'Current Width')
    fields[2].label.configure(text = 'Max Height')
    fields[3].label.configure(text = 'Max Width')
    fields[4].label.configure(text = 'Max Sqaure Footage')

    return fields




fields = create_fields()
cal_button = Button(sub_window, text = '• CALCULATE •', bg = gray_medium, fg = orange, width = 30, relief = 'flat', font = ('Ariel', 15))
cal_button.grid(row = 6, column = 0, pady = 10)
return_lbl = Label(sub_window, bg = gray_medium, fg = orange, width = 50, height = 3, font = ('Ariel', 15))
return_lbl.grid(row = 7, column = 0, pady = 5 )

return_lbl.configure(text = 'Height:\nWidth:\nSquare Footage:', justify = 'left', anchor = 'w')



root.mainloop()