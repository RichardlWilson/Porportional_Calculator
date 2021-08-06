#GUI 
version = ' v1.1.0'
from tkinter import *
import sys
import os

import calculations as cal

class Themes:
    '''
    Atribbutes that change the appearance of the app.
    '''
    def __init__(self):
        self.theme_num = 1
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


    def switch(self):
        self.theme_num += 1

        if self.theme_num >4:
            self.theme_num = 1
            self.default()    
        elif self.theme_num == 2:
            self.aqua()
        elif self.theme_num == 3:
            self.lava()
        elif self.theme_num == 4:
            self.wind()
            
        root.configure(bg = self.layer_3)
        sub_window.configure(bg = self.layer_3)

        toolbar.button_frame.configure(bg = self.layer_3)
        toolbar.theme_button.configure(bg = self.layer_2, fg = self.text_color)
        toolbar.basic_button.configure(bg = self.layer_2, fg = self.text_color)
        toolbar.advanced_button.configure(bg = self.layer_2, fg = self.text_color)

        header.frame.configure(bg = self.layer_3)
        header.title_label.configure(bg = self.layer_3, fg = self.text_color)

        for field in data_entries[0:4]:
            field.frame.configure(bg = self.layer_2)
            field.label.configure(bg = self.layer_2, fg = self.text_color)
            field.entry.configure(bg = self.layer_1)
            field.radio1.configure(bg = self.layer_2, selectcolor = self.layer_2, fg = self.text_color)
            field.radio2.configure(bg = self.layer_2, selectcolor = self.layer_2, fg = self.text_color)
            field.clear_btn.configure(bg = self.layer_3, fg = self.text_color)

        max_square_footage_sec.frame.configure(bg = self.layer_2)
        max_square_footage_sec.label.configure(bg = self.layer_2, fg = self.text_color)
        max_square_footage_sec.entry.configure(bg = self.layer_1)
        max_square_footage_sec.label_2.configure(bg = self.layer_2)
        max_square_footage_sec.clear_btn.configure(bg = self.layer_3, fg = self.text_color)

        calculate_sec.frame.configure(bg = self.layer_3)
        calculate_sec.cal_button.configure(bg = self.layer_2, fg = self.text_color)
        calculate_sec.clear_all_btn.configure(bg = self.layer_3, fg = self.text_color)

        result_sec.frame.configure(bg = self.layer_2)
        result_sec.info_label.configure(bg = self.layer_2, fg = self.text_color)
        result_sec.return_label.configure(bg = self.layer_2, fg = self.text_color)
        result_sec.copy_button.configure(bg = self.layer_2, fg = self.text_color)



            

                 

class ToolBar:
    '''
    Top tool bar.
    '''
    def __init__(self):

        self.button_frame = Frame(sub_window, bg = theme.layer_3, width = 20)

        self.theme_button = Button(self.button_frame, text = 'Theme', bg = theme.layer_2,
            fg = theme.text_color, width = 8, relief = 'ridge', font = ('Ariel', 10), bd = 1,
            overrelief = 'sunken', takefocus = 0, command = theme.switch )

        self.basic_button = Button(self.button_frame, text = 'Basic', bg = theme.layer_2,
            fg = theme.text_color, width = 8, relief = 'ridge', font = ('Ariel', 10), bd = 1,
            overrelief = 'sunken', takefocus = 0, command = self.basic_btn)

        self.advanced_button = Button(self.button_frame, text = 'Advanced', bg = theme.layer_2,
            fg = theme.text_color, width = 8, relief = 'ridge', font = ('Ariel', 10), bd = 1,
            overrelief = 'sunken', takefocus = 0, command = self.advanced_btn)


    def show(self, num = 1):
        self.button_frame.grid(row = num, column = 0, padx = 5, sticky = 'ne')
        self.theme_button.grid(row = 0, column = 0, padx = 0, pady = 5)
        self.advanced_button.grid(row = 0, column = 1, padx = 0, pady = 5)
    

    def basic_btn(self):
        root.geometry('630x410')
        self.basic_button.grid_forget()
        self.advanced_button.grid(row = 0, column = 1, padx = 0, pady = 5)
        
        for field in data_entries[2:]:
            field.entry.delete(0,END)
            field.frame.grid_forget()

        calculate_sec.calculate()


    def switch(self):
        print('Hit')
        theme.switch()    


    def advanced_btn(self):
        root.geometry('630x610')
        self.advanced_button.grid_forget()
        self.basic_button.grid(row = 0, column = 1, padx = 0, pady = 5)
        
        max_height_sec.show(4)
        max_width_sec.show(5)
        max_square_footage_sec.show(6)

        #all other advanced options .grid() go here.



class Header:
    '''
    Top Section af app. Includes the Title.
    '''
    def __init__(self):
        self.frame = Frame(sub_window, bg = theme.layer_3, width = 600)

        self.title_label = Label(self.frame, text = 'Proportional Calculator',
            font = ('Ariel', 27), bg = theme.layer_3, fg = theme.text_color,
            width = 27)

    def show(self, num = 1):
        self.frame.grid(row = num, column = 0, pady = 5, padx = 5)
        self.title_label.grid(row = 0, column = 0, padx = 5, pady = 4)
        


class EntryField:
    '''
    Data Entry Field.
    '''
    def __init__(self, name):   

        self.frame = Frame(sub_window, bg = theme.layer_2, width = 600,
            height = 40)

        self.label = Label(self.frame, bg = theme.layer_2, fg = theme.text_color,
            width = 20, font = ('Ariel', 15), justify = 'right', anchor = 'e',
            text = name)
        
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
    '''
    Square footage data field.
    '''
    def __init__(self, name):
    
        self.frame = Frame(sub_window, bg = theme.layer_2, width = 600,
            height = 40)

        self.label = Label(self.frame, bg = theme.layer_2, fg = theme.text_color,
            width = 20, font = ('Ariel', 15), justify = 'right', anchor = 'e',
            text = name)
        
        validation = self.frame.register(is_digit)
        self.entry = Entry(self.frame, bg = theme.layer_1, fg = theme.entry_text_color,
            width = 10, relief = 'flat', font = ('Ariel', 15), validate = 'key',
            validatecommand = (validation, '%P'))

        self.label_2 = Label(self.frame, bg = theme.layer_2, fg = theme.text_color,
            width = 17)

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
    '''
    Calculate Button Section.
    '''
    def __init__(self):
        self.frame = Frame(sub_window, bg = theme.layer_3, width = 600)

        self.cal_button = Button(self.frame, text = 'CALCULATE', bg = theme.layer_2,
            fg = theme.text_color, width = 23, relief = 'ridge', font = ('Ariel', 15), bd = 1,
            overrelief = 'sunken', command = self.calculate, takefocus = 0)

        # self.cal_radio_var = IntVar()
        # self.cal_radio_var.set(1)

        self.clear_all_btn = Button(self.frame, text = 'Clear All', bg = theme.layer_3,
            fg = theme.text_color, width = 8, relief = 'ridge', font = ('Ariel', 10),
            bd = 1, overrelief = 'sunken', command = self.clear_all, takefocus = 0)
    
    def show(self,num = 1):
        self.frame.grid(row = num, column = 0, pady = 5, padx = 5)
        self.cal_button.grid(row = 0, column = 0, pady = 10, padx = 13)
        self.clear_all_btn.grid(row = 0, column = 3, padx = 20, sticky = 'e')

    def calculate(self,key_event = None):
        info = []
        for field in data_entries[:4]:
            info.append([field.entry.get(),field.radio_var.get()])

        info.append([data_entries[4].entry.get(), 1])    
             
        calculation = cal.calculate(info)
        updated_result[0] = calculation

        result_sec.return_label['text'] = updated_result[0]    

    def clear_all(self):
        for field in data_entries:
            field.entry.delete(0, END)
            result_sec.return_label['text'] = '0.0" | 0.0\'\n0.0" | 0.0\'\n0.0\''   



class ResultSection:
    '''
    Results Displayed in this section.
    '''
    def __init__(self):

        self.frame = Frame(sub_window, bg = theme.layer_2, width = 600)

        self.info_label = Label(self.frame, bg = theme.layer_2, relief = 'flat',
            fg = theme.text_color, width = 20, height = 3, font = ('Ariel', 15))
        
        self.info_label.configure(justify = 'right', anchor = 'e',
            text = 'Height: \nWidth: \nSquare Footage: ' )

        self.return_label = Label(self.frame, bg = theme.layer_2, relief = 'flat',
            fg = theme.text_color, width = 20, height = 3, font = ('Ariel', 15))
        
        self.return_label.configure(justify = 'left', anchor = 'w',
            text = '0.0" | 0.0\'\n0.0" | 0.0\'\n0.0\'' )

        self.copy_button = Button(self.frame, text = 'Copy', bg = theme.layer_2,
            fg = theme.text_color, width = 10, relief = 'ridge', font = ('Ariel', 10), bd = 1,
            command = lambda : self.copy_to_clipboard('text'), overrelief = 'sunken',
            takefocus = 0)
        

    def show(self, num = 1):
        self.frame.grid(row = num, column = 0, pady = 5, padx = 5)
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
    Retreives the root path in memory.
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


def tab_order():
    '''
    Sets the Tab order for the data entry fields.
    '''
    entry_fields = [data_entries[0].entry, data_entries[1].entry, data_entries[2].entry,
                    data_entries[3].entry, data_entries[4].entry] 

    entry_fields[0].focus()


def is_digit(text):
    '''
    Checks if input is a integer or a float.
    '''
    if text =='':
        return True
    try:
        float(text)
        return True
    except:
        return False



if __name__ == '__main__':
    theme = Themes()
    #theme.lava()

    root = Tk()
    root.title('Proprtional Calculator ' + version)
    root.configure(bg = theme.layer_3)
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)
    root.geometry(win_center(630, 410))#'630x380'

    file_path = get_path()

    root.iconphoto(True, PhotoImage(file = file_path))

    sub_window = Frame(root, bg = theme.layer_3, width = 610,height = 600,
        relief = 'solid', bd = 1)
    sub_window.grid(row = 0, column = 0, padx = 10, pady = 10)

    #toolbar section.
    toolbar = ToolBar()
    toolbar.show(0)

    #creates header section.
    header = Header()
    header.show(1)

    #creates data entry fields
    data_entries = []

    current_height_sec = EntryField('Current Height:')
    current_height_sec.show(2)
    data_entries.append(current_height_sec)

    current_width_sec = EntryField('Current Width:')
    current_width_sec.show(3)
    data_entries.append(current_width_sec)

    max_height_sec = EntryField('Max Height:')
    data_entries.append(max_height_sec)

    max_width_sec = EntryField('Max Width:')
    data_entries.append(max_width_sec)

    max_square_footage_sec = SquareFootage('Max Sqaure Footage:')
    data_entries.append(max_square_footage_sec)

    #creates the calculation button section.
    calculate_sec = CalculateSection()
    calculate_sec.show(7)

    #create class for the return results section.
    updated_result = ['']
    result_sec = ResultSection()
    result_sec.show(8)

    root.bind('<Return>', calculate_sec.calculate)
    tab_order()
    root.mainloop()