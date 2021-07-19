#GUI 

from tkinter import *

#colors_used
orange = '#FA9605'
gray = '#3B3B3C'
gray_medium = '#4F4F51'
gray_light = '#9D9FA2'

root = Tk()
root.title('proportion tool')
root.configure(bg = gray)

title_image = PhotoImage(file = 'resources/images/title_image.gif')

title_label = Label(
    root,
    image = title_image,
    bg = gray,
    fg = orange,
    padx = 100,
    pady = 4
    )

title_label.grid(row = 0, column = 0)


class Field:
    def __init__(self):
        #option_list = ['inches', 'feet']
        self.frame = Frame(root, bg = gray_medium, width = 400, height = 40)
        self.label = Label(self.frame, bg = gray_medium, fg = orange, width = 20)
        self.entry = Entry(self.frame, bg = gray_light, fg = 'white', width = 10)

        self.radio_var = IntVar()
        self.radio_var.set('inches')

        self.radio1 = Radiobutton(self.frame, text = 'inches', variable = self.radio_var, value = 0)
        self.radio1.configure(bg = gray_medium, fg = orange)

        self.radio2 = Radiobutton(self.frame,text = 'feet', variable = self.radio_var, value = 1)
        self.radio2.configure(bg = gray_medium, fg = orange)


    def show(self, num = 1):
        self.frame.grid(row = num, column = 0, padx = 100, pady = 10)
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

    fields[0].label.configure(text = 'Height')
    fields[1].label.configure(text = 'Width')
    fields[2].label.configure(text = 'Max Height')
    fields[3].label.configure(text = 'Max Width')
    fields[4].label.configure(text = 'Max Sqaure Footage') 




fields = create_fields()
cal_button = Button(text = '• CALCULATE •', bg = gray_medium, fg = orange, width = 30, relief = 'flat')
cal_button.grid(row = 6, column = 0, pady = 10)


# field = Field()
# field.show()


root.mainloop()