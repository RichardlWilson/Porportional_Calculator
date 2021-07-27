#GUI 

from tkinter import *
import calculations

#colors_used
orange = '#FA9605'
gray = '#273947'
gray_medium = '#354959'
gray_light = '#5f7587'

root = Tk()
root.geometry('630x560')
root.title('proportion tool for Debra')
root.configure(bg = gray)
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
root.iconphoto(True, PhotoImage(file = 'resources/images/icon.png'))
#root.eval('tk::PlaceWindow . center')
#root.resizable(0,0)

sub_window = Frame(root, bg = gray, width = 610,height = 600, relief = 'solid', 
    bd = 1)
sub_window.grid(row = 0, column = 0, padx = 10, pady = 10)


title_label = Label(sub_window, text = 'Proportion Tool', font = ('Times', 40),
    bg = gray, fg = orange, padx = 5, pady = 4)

title_label.grid(row = 0, column = 0)

def destroy_now():
    fields[0].frame.grid_forget()

advanced_button = Button(sub_window, text = 'Advanced', bg = gray_medium,
    fg = orange, width = 10, relief = 'ridge', font = ('Ariel', 10), bd = 1,
    overrelief = 'sunken', command = destroy_now)

advanced_button.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'ne')


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
        self.radio_var.set(0)

        self.radio1 = Radiobutton(self.frame, text = 'inches',
            variable = self.radio_var, value = 0, width = 5,
            font = ('Ariel', 15), indicatoron = 0, relief = 'groove', bd = 1,
            selectcolor = gray_medium, overrelief = 'sunken', takefocus = 0)

        self.radio1.configure(bg = gray_medium, fg = orange)

        self.radio2 = Radiobutton(self.frame, text = 'feet',
            variable = self.radio_var, value = 1, width = 5,
            font = ('Ariel', 15), indicatoron = 0, relief = 'groove', bd = 1,
            selectcolor = gray_medium, overrelief = 'sunken', takefocus = 0)

        self.radio2.configure(bg = gray_medium, fg = orange)

        self.clear_btn = Button(self.frame, text = 'Clear', bg = gray,
            fg = orange, width = 5, relief = 'ridge', font = ('Ariel', 10),
            bd = 1, overrelief = 'sunken', command = self.clear_entry,
            takefocus = 0)

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

    try:
        text = updated_calculation[0].split('\n')
        root.clipboard_append(f'Height: {text[0]} \nWidth: {text[1]} \nSquare' \
            + f'Footage: {text[2]}')
    except IndexError:
        text = [0,0,0]

        root.clipboard_append(f'Height: {text[0]} \nWidth: {text[1]} \nSquare' \
            + f'Footage: {text[2]}')

    root.update()


def tab_order():
    entry_fields = [fields[0].entry, fields[1].entry, fields[2].entry,
        fields[3].entry, fields[4].entry] 

    entry_fields[0].focus()
    print(entry_fields)      


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
        return_label['text'] = '0\n0\n0'


def calculate(key_event = None):
    info = []
    for field in fields:
        info.append([field.entry.get(),field.radio_var.get()])
         
    calculation = calculations.Calculation(info)
    updated_calculation[0] = calculation.compute()

    return_label['text'] = updated_calculation[0]


updated_calculation = ['']

fields = create_fields()


cal_btn_frame = Frame(sub_window, bg = gray, width = 600)

cal_btn_frame.grid(row = 6, column = 0, pady = 5, padx = 5)

cal_button = Button(cal_btn_frame, text = 'CALCULATE', bg = gray_medium,
    fg = orange, width = 23, relief = 'ridge', font = ('Ariel', 15), bd = 1,
    overrelief = 'sunken', command = calculate, takefocus = 0)

cal_button.grid(row = 0, column = 0, pady = 10, padx = 13)


cal_radio_var = IntVar()

cal_radio_var.set(1)

# cal_radio_inches = Radiobutton(cal_btn_frame, text = 'inches',
#     variable = cal_radio_var, value = 1, width = 5, font = ('Ariel', 15),
#     indicatoron = 0, relief = 'groove', bd = 1, selectcolor = gray_medium,
#     overrelief = 'sunken', bg = gray_medium, fg = orange, takefocus = 0)

# cal_radio_inches.grid(row = 0, column = 1, padx = 0, pady = 5)

# cal_radio_feet = Radiobutton(cal_btn_frame, text = 'feet',
#     variable = cal_radio_var, value = 2, width = 5, font = ('Ariel', 15),
#     indicatoron = 0, relief = 'groove', bd = 1, selectcolor = gray_medium,
#     overrelief = 'sunken', bg = gray_medium, fg = orange, takefocus = 0)

# cal_radio_feet.grid(row = 0, column = 2, padx = 0, pady = 5)


clear_all_btn = Button(cal_btn_frame, text = 'Clear All', bg = gray,
    fg = orange, width = 8, relief = 'ridge', font = ('Ariel', 10),
    bd = 1, overrelief = 'sunken', command = clear_all, takefocus = 0)

clear_all_btn.grid(row = 0, column = 3, padx = 20, sticky = 'e')


return_frame = Frame(sub_window, bg = gray_medium, width = 600)

return_frame.grid(row = 7, column = 0, pady = 5, padx = 5)


info_label = Label(return_frame, bg = gray_medium, relief = 'flat',
    fg = orange, width = 20, height = 3, font = ('Ariel', 15))

info_label.grid(row = 0, column = 0, pady = 5 )

info_label.configure(justify = 'right', anchor = 'e',
    text = 'Height: \nWidth: \nSquare Footage: ' )


return_label = Label(return_frame, bg = gray_medium, relief = 'flat',
    fg = orange, width = 20, height = 3, font = ('Ariel', 15))

return_label.grid(row = 0, column = 1, pady = 5 )

return_label.configure(justify = 'left', anchor = 'w',
    text = '0 \n0 \n0 ' )


copy_button = Button(return_frame, text = 'Copy', bg = gray_medium,
    fg = orange, width = 10, relief = 'ridge', font = ('Ariel', 10), bd = 1,
    command = lambda : copy_to_clipboard('text'), overrelief = 'sunken',
    takefocus = 0)

copy_button.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = 'ne')


#temp patch for square footage frame.
fields[4].radio1.configure(state = DISABLED)
fields[4].radio2.select()


root.bind('<Return>', calculate )
tab_order()
root.mainloop()