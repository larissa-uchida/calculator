from tkinter import *

root = Tk()
root.title('Calculator')
root.iconbitmap('icon.ico')
root.config(bg='#d6c7cf')

width_window = 360
height_window = 500
width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()
pos_x = int(width_screen/2 - (width_window/2))
pos_y = int(height_screen/2 - (height_window/2))
root.geometry(f'{width_window}x{height_window}+{pos_x}+{pos_y}')

viewer = Text(root, height=2, width=16, font='Arial 30')
viewer.grid(columnspan=4, pady=8, padx=1)
viewer.config(bg='#ffe6f9')
class Buttons:
    def __init__(self, color, symbol, column, row):
        self.color = color
        self.symbol = symbol
        self.column = column
        self.row = row

        self.botao = Button(text=symbol, bg=color, command=None, width=7, height=3, font='Arial 13 bold')
        self.botao.grid(column=column, row=row, pady=3)

    def change_size(self, width='', height=''):
        self.botao.configure(width=width, height=height)

clear_button = Buttons('#e376ac', 'C', 0, 3)
plus_button = Buttons('#e376ac', '+', 3, 5)
minus_button = Buttons('#e376ac', '-', 3, 4)
multiply_button = Buttons('#e376ac', 'x', 2, 3)
divide_button = Buttons('#e376ac', '/', 3, 3)
equal_button = Buttons('#e376ac', '=', 3, 6)
equal_button.botao.grid(rowspan=2)
equal_button.change_size(7, 7)
comma_button = Buttons('#e376ac', ',', 2, 7)
percent_button = Buttons('#e376ac', '%', 1, 3)

zero_button = Buttons('#e376ac', '0', 0, 7)
zero_button.botao.grid(columnspan=2)
zero_button.change_size(16, 3)
one_button = Buttons('#e376ac', '1', 0, 6)
two_button = Buttons('#e376ac', '2', 1, 6)
three_button = Buttons('#e376ac', '3', 2, 6)
four_button = Buttons('#e376ac', '4', 0, 5)
five_button = Buttons('#e376ac', '5', 1, 5)
six_button = Buttons('#e376ac', '6', 2, 5)
seven_button = Buttons('#e376ac', '7', 0, 4)
eight_button = Buttons('#e376ac', '8', 1, 4)
nine_button = Buttons('#e376ac', '9', 2, 4)
 
root.mainloop()