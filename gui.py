#GUI 
version = 'BETA v1.0.2'
from tkinter import *
import sys
import os

import calculations

class Themes:
    def __init__(self):
        self.text_color = '#FA9605'
        self.entry_text_color = 'white'
        self.layer_1 = '#5f7587'
        self.layer_2 = '#354959'
        self.layer_3 = '#273947'

    def default(self):
        self.text_color = '#FA9605'
        self.entry_text_color = 'white'
        self.layer_1 = '#5f7587'
        self.layer_2 = '#354959'
        self.layer_3 = '#273947'

    def aqua(self):
        self.text_color = '#1cc4fc'
        self.entry_text_color = 'white'
        self.layer_1 = '#1b7896'
        self.layer_2 = '#1b5b70'
        self.layer_3 = '#153b47'

    def lava(self):
        self.text_color = '#f53d0f'
        self.entry_text_color = 'white'
        self.layer_1 = '#963921'
        self.layer_2 = '#692e1e'
        self.layer_3 = '#421003'

    def wind(self):
        self.text_color = '#169e97'
        self.entry_text_color = 'white'
        self.layer_1 = '#34d1c9'
        self.layer_2 = '#97f7f2'
        self.layer_3 = '#d7fcfa'     



class Header:
    def __init__(self):
        self.frame = Frame(sub_window, bg = theme.layer_3, width = 600)

        self.title_label = Label(self.frame, text = 'Proportional Calculator', font = ('Ariel', 27),
            bg = theme.layer_3, fg = theme.text_color, width = 27)

        self.basic_button = Button(self.frame, text = 'Basic', bg = theme.layer_2,
            fg = theme.text_color, width = 8, relief = 'ridge', font = ('Ariel', 10), bd = 1,
            overrelief = 'sunken', takefocus = 0, command = self.basic_btn)

        self.advanced_button = Button(self.frame, text = 'Advanced', bg = theme.layer_2,
            fg = theme.text_color, width = 8, relief = 'ridge', font = ('Ariel', 10), bd = 1,
            overrelief = 'sunken', takefocus = 0, command = self.advanced_btn)


    def show(self):
        self.frame.grid(row = 0, column = 0, pady = 5, padx = 5)
        self.title_label.grid(row = 0, column = 0, padx = 5, pady = 4)
        self.advanced_button.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'ne')

    def basic_btn(self):
        root.geometry('630x380')
        self.basic_button.grid_forget()
        self.advanced_button.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'ne')
        
        for field in fields[2:]:
            field.entry.delete(0,END)
            field.frame.grid_forget()

        calculate_sec.calculate()


    def advanced_btn(self):
        root.geometry('630x560')
        self.advanced_button.grid_forget()
        self.basic_button.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'ne')
        
        num = 3
        for field in fields[2:]:
            field.show(num)
            num += 1  

        #all other advanced options .grid() go here.



class EntryField:
    def __init__(self):   

        self.frame = Frame(sub_window, bg = theme.layer_2, width = 600,
            height = 40)

        self.label = Label(self.frame, bg = theme.layer_2, fg = theme.text_color,
            width = 20, font = ('Ariel', 15), justify = 'right', anchor = 'e')
        
        validation = self.frame.register(is_digit)
        self.entry = Entry(self.frame, bg = theme.layer_1, fg = theme.entry_text_color,
            width = 10, relief = 'flat', font = ('Ariel', 15), validate = 'key',
            validatecommand = (validation, '%P'))
        
        self.radio_var = IntVar()
        self.radio_var.set(0)

        self.radio1 = Radiobutton(self.frame, text = 'inches',
            variable = self.radio_var, value = 0, width = 5,
            font = ('Ariel', 15), indicatoron = 0, relief = 'groove', bd = 1,
            selectcolor = theme.layer_2, overrelief = 'sunken', takefocus = 0)

        self.radio1.configure(bg = theme.layer_2, fg = theme.text_color)

        self.radio2 = Radiobutton(self.frame, text = 'feet',
            variable = self.radio_var, value = 1, width = 5,
            font = ('Ariel', 15), indicatoron = 0, relief = 'groove', bd = 1,
            selectcolor = theme.layer_2, overrelief = 'sunken', takefocus = 0)

        self.radio2.configure(bg = theme.layer_2, fg = theme.text_color)

        self.clear_btn = Button(self.frame, text = 'Clear', bg = theme.layer_3,
            fg = theme.text_color, width = 5, relief = 'ridge', font = ('Ariel', 10),
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



class SquareFootage:
    def __init__(self):
    
        self.frame = Frame(sub_window, bg = theme.layer_2, width = 600,
            height = 40)

        self.label = Label(self.frame, bg = theme.layer_2, fg = theme.text_color,
            width = 20, font = ('Ariel', 15), justify = 'right', anchor = 'e')
        
        validation = self.frame.register(is_digit)
        self.entry = Entry(self.frame, bg = theme.layer_1, fg = theme.entry_text_color,
            width = 10, relief = 'flat', font = ('Ariel', 15), validate = 'key',
            validatecommand = (validation, '%P'))

        self.label_2 = Label(self.frame, bg = theme.layer_2, fg = theme.text_color, width = 17)

        self.clear_btn = Button(self.frame, text = 'Clear', bg = theme.layer_3,
            fg = theme.text_color, width = 5, relief = 'ridge', font = ('Ariel', 10),
            bd = 1, overrelief = 'sunken', command = self.clear_entry,
            takefocus = 0)
        
    def show(self, num = 1):
        self.frame.grid(row = num, column = 0, padx = 5, pady = 10)
        self.frame.grid_propagate(0)
        self.label.grid(row = 0, column = 0, padx = 10, pady = 5)
        self.entry.grid(row = 0, column = 1, padx = 10, pady = 5)
        self.label_2.grid(row =0, column = 2, columnspan = 2)
        self.clear_btn.grid(row = 0, column = 4, padx = 35,sticky = 'e')

    def clear_entry(self):
        self.entry.delete(0, END)



class CalculateSection:
    def __init__(self):
        self.frame = Frame(sub_window, bg = theme.layer_3, width = 600)

        self.cal_button = Button(self.frame, text = 'CALCULATE', bg = theme.layer_2,
            fg = theme.text_color, width = 23, relief = 'ridge', font = ('Ariel', 15), bd = 1,
            overrelief = 'sunken', command = self.calculate, takefocus = 0)

        self.cal_radio_var = IntVar()
        self.cal_radio_var.set(1)

        self.clear_all_btn = Button(self.frame, text = 'Clear All', bg = theme.layer_3,
            fg = theme.text_color, width = 8, relief = 'ridge', font = ('Ariel', 10),
            bd = 1, overrelief = 'sunken', command = self.clear_all, takefocus = 0)
    
    def show(self):
        self.frame.grid(row = 6, column = 0, pady = 5, padx = 5)
        self.cal_button.grid(row = 0, column = 0, pady = 10, padx = 13)
        self.clear_all_btn.grid(row = 0, column = 3, padx = 20, sticky = 'e')

    def calculate(self,key_event = None):
        info = []
        for field in fields[:4]:
            info.append([field.entry.get(),field.radio_var.get()])

        info.append([fields[4].entry.get(), 1])    
             
        calculation = calculations.Calculation(info)
        updated_calculation[0] = calculation.compute()

        result_sec.return_label['text'] = updated_calculation[0]    

    def clear_all(self):
        for field in fields:
            field.entry.delete(0, END)
            return_label['text'] = '0\n0\n0'    

class ResultSection:
    def __init__(self):

        self.frame = Frame(sub_window, bg = theme.layer_2, width = 600)

        self.info_label = Label(self.frame, bg = theme.layer_2, relief = 'flat',
            fg = theme.text_color, width = 20, height = 3, font = ('Ariel', 15))
        
        self.info_label.configure(justify = 'right', anchor = 'e',
            text = 'Height: \nWidth: \nSquare Footage: ' )

        self.return_label = Label(self.frame, bg = theme.layer_2, relief = 'flat',
            fg = theme.text_color, width = 20, height = 3, font = ('Ariel', 15))
        
        self.return_label.configure(justify = 'left', anchor = 'w',
            text = '0 \n0 \n0 ' )

        self.copy_button = Button(self.frame, text = 'Copy', bg = theme.layer_2,
            fg = theme.text_color, width = 10, relief = 'ridge', font = ('Ariel', 10), bd = 1,
            command = lambda : self.copy_to_clipboard('text'), overrelief = 'sunken',
            takefocus = 0)
        

    def show(self):
        self.frame.grid(row = 7, column = 0, pady = 5, padx = 5)
        self.info_label.grid(row = 0, column = 0, pady = 5)
        self.return_label.grid(row = 0, column = 1, pady = 5)
        self.copy_button.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = 'ne')

    def copy_to_clipboard(self, text):
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



def get_path():
    '''
    Retreives the path in memory.
    '''
    try:
       wd = sys._MEIPASS
    except AttributeError:
       wd = os.getcwd()

    return os.path.join(wd,'resources\\images\\icon.png')


def win_center(app_width, app_height):
    '''
    returns window geometry to center the window on the screen.
    '''
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width/2 - app_width/2)
    center_y = int(screen_height/2 - app_height/2)

    return f'{app_width}x{app_height}+{center_x}+{center_y}'


def create_fields():
    '''
    Creates the entry fields.
    '''
    #creates current height, current width, max height, max width and
    #max square footage data entry fields.
    fields = [EntryField() for num in range(4)]

    num = 1
    for field in fields[0:2]:
        field.show(num)
        num +=1

    fields[0].label.configure(text = 'Current Height:')
    fields[0].label.configure(text = 'Current Height:')
    fields[1].label.configure(text = 'Current Width:')
    fields[2].label.configure(text = 'Max Height:')
    fields[3].label.configure(text = 'Max Width:')
    
    #creates the max square footage data entry field
    max_square_footage = SquareFootage()
    max_square_footage.label.configure(text = 'Max Sqaure Footage:')
    # max_square_footage.show(5)
    fields.append(max_square_footage)

    return fields


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


theme = Themes()
#theme.lava()

root = Tk()
root.title('Proprtional Calculator ' + version)
root.configure(bg = theme.layer_3)
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
root.geometry(win_center(630, 380))#'630x380'

file_path = get_path()

root.iconphoto(True, PhotoImage(file = file_path))

sub_window = Frame(root, bg = theme.layer_3, width = 610,height = 600, relief = 'solid', 
    bd = 1)
sub_window.grid(row = 0, column = 0, padx = 10, pady = 10)


#create a tool bar to go at top of window. house advanced, basic and theme buttons.

updated_calculation = ['']

#creates header section.
header = Header()
header.show()

#creates data entry fields
fields = create_fields()

#creates the calculation button section.
calculate_sec = CalculateSection()
calculate_sec.show()

#create class for the return results section.
result_sec = ResultSection()
result_sec.show()


if __name__ == '__main__':
    root.bind('<Return>', calculate_sec.calculate)
    tab_order()
    root.mainloop()