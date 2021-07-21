#GUI 

from tkinter import *
import calculations

#colors_used
orange = '#FA9605'
gray = '#3B3B3C'
gray_medium = '#4F4F51'
gray_light = '#9D9FA2'

root = Tk()
root.geometry('630x560')
root.title('proportion tool for Debra')
root.configure(bg = gray)
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
#root.eval('tk::PlaceWindow . center')
#root.resizable(0,0)

sub_window = Frame(root, bg = gray, width = 610,height = 600, relief = 'solid', 
    bd = 1)
sub_window.grid(row = 0, column = 0, padx = 10, pady = 10)

title_label = Label(sub_window, text = 'Proportion Tool', font = ('Times', 40),
    bg = gray, fg = orange, padx = 5, pady = 4)

title_label.grid(row = 0, column = 0)

advanced_button = Button(sub_window, text = 'Advanced', bg = gray_medium,
    fg = orange, width = 10, relief = 'ridge', font = ('Ariel', 10), bd = 1,
    overrelief = 'sunken')
#advanced_button.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'ne')

class Field:
    def __init__(self):

        self.frame = Frame(sub_window, bg = gray_medium, width = 600,
            height = 40)

        self.label = Label(self.frame, bg = gray_medium, fg = orange,
            width = 20, font = ('Ariel', 15), justify = 'right', anchor = 'e')
        
        validation = self.frame.register(is_digit)
        self.entry = Entry(self.frame, bg = gray_light, fg = 'white',
            width = 10, relief = 'flat', font = ('Ariel', 15), validate = 'key',
            validatecommand = (validation, '%P'))
        
        self.radio_var = IntVar()
        self.radio_var.set(1)

        self.radio1 = Radiobutton(self.frame, text = 'inches',
            variable = self.radio_var, value = 1, width = 5,
            font = ('Ariel', 15), indicatoron = 0, relief = 'groove', bd = 1,
            selectcolor = gray_medium, overrelief = 'sunken')

        self.radio1.configure(bg = gray_medium, fg = orange)
        #self.radio1.select()

        self.radio2 = Radiobutton(self.frame, text = 'feet',
            variable = self.radio_var, value = 2, width = 5,
            font = ('Ariel', 15), indicatoron = 0, relief = 'groove', bd = 1,
            selectcolor = gray_medium, overrelief = 'sunken')

        self.radio2.configure(bg = gray_medium, fg = orange)

        self.clear_btn = Button(self.frame, text = 'Clear', bg = gray,
            fg = orange, width = 5, relief = 'ridge', font = ('Ariel', 10),
            bd = 1, overrelief = 'sunken', command = self.clear_entry)

    def show(self, num = 1):
        self.frame.grid(row = num, column = 0, padx = 5, pady = 10)
        self.frame.grid_propagate(0)

        self.label.grid(row = 0, column = 0, padx = 10, pady = 5)
        self.entry.grid(row = 0, column = 1, padx = 10, pady = 5)
        self.radio1.grid(row = 0, column = 2 )
        self.radio2.grid(row = 0, column = 3 )
        self.clear_btn.grid(row = 0, column = 4, padx = 35,sticky = 'e')

    def clear_entry(self):
        self.entry.delete(0, END)     
        
               

def create_fields():
    fields = [Field() for num in range(5)]
    num = 1
    for field in fields:
        field.show(num)
        num +=1

    fields[0].label.configure(text = 'Current Height:')
    fields[1].label.configure(text = 'Current Width:')
    fields[2].label.configure(text = 'Max Height:')
    fields[3].label.configure(text = 'Max Width:')
    fields[4].label.configure(text = 'Max Sqaure Footage:')

    return fields


def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(updated_calculation[0])
    root.update()


def is_digit(text):
    if text =='':
        return True
    try:
        float(text)
        return True
    except:
        return False


def clear_all():
    for field in fields:
        field.entry.delete(0, END)


def calculate():
    info = []
    for field in fields:
        info.append(float(field.entry.get()))

    updated_calculation[0] = calculations.calculation(tuple(info))
    return_label.configure(text = updated_calculation[0])


updated_calculation = ['']

fields = create_fields()

cal_btn_frame = Frame(sub_window, bg = gray, width = 600)

cal_btn_frame.grid(row = 6, column = 0, pady = 5, padx = 5)

cal_button = Button(cal_btn_frame, text = 'CALCULATE', bg = gray_medium,
    fg = orange, width = 23, relief = 'ridge', font = ('Ariel', 15), bd = 1,
    overrelief = 'sunken', command = calculate)

cal_button.grid(row = 0, column = 0, pady = 10, padx = 13)

cal_radio_var = IntVar()

cal_radio_var.set(1)

cal_radio_inches = Radiobutton(cal_btn_frame, text = 'inches',
    variable = cal_radio_var, value = 1, width = 5, font = ('Ariel', 15),
    indicatoron = 0, relief = 'groove', bd = 1, selectcolor = gray_medium,
    overrelief = 'sunken', bg = gray_medium, fg = orange)

cal_radio_inches.grid(row = 0, column = 1, padx = 0, pady = 5)

cal_radio_feet = Radiobutton(cal_btn_frame, text = 'feet',
    variable = cal_radio_var, value = 2, width = 5, font = ('Ariel', 15),
    indicatoron = 0, relief = 'groove', bd = 1, selectcolor = gray_medium,
    overrelief = 'sunken', bg = gray_medium, fg = orange)

cal_radio_feet.grid(row = 0, column = 2, padx = 0, pady = 5)

clear_all_btn = Button(cal_btn_frame, text = 'Clear All', bg = gray,
    fg = orange, width = 8, relief = 'ridge', font = ('Ariel', 10),
    bd = 1, overrelief = 'sunken', command = clear_all)

clear_all_btn.grid(row = 0, column = 3, padx = 20, sticky = 'e')

return_frame = Frame(sub_window, bg = gray_medium, width = 600)

return_frame.grid(row = 7, column = 0, pady = 5, padx = 5)

return_label = Label(return_frame, bg = gray_medium, relief = 'flat',
    fg = orange, width = 50, height = 3, font = ('Ariel', 15))

return_label.grid(row = 0, column = 0, pady = 5 )

return_label.configure(justify = 'right', anchor = 'w',
    text = ' Height: \n Width: \n Square Footage: ' )

copy_button = Button(return_frame, text = 'Copy', bg = gray_medium,
    fg = orange, width = 10, relief = 'ridge', font = ('Ariel', 10), bd = 1,
    command = lambda : copy_to_clipboard('text'), overrelief = 'sunken')

copy_button.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'ne')


root.mainloop()