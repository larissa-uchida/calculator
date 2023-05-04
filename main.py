from tkinter import *

# Window settings
root = Tk()
root.title('Calculator')
root.iconbitmap('icon.ico')
root.config(bg='#ba2563')
root.resizable(False, False)

width_window = 363
height_window = 525
width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()
pos_x = int(width_screen/2 - (width_window/2))
pos_y = int(height_screen/2 - (height_window/2))
root.geometry(f'{width_window}x{height_window}+{pos_x}+{pos_y}')

# Viewer settings
viewer = Text(root, height=1, width=13, font='Arial 36', wrap='none', spacing1=20, spacing3=20)
viewer.grid(columnspan=4, pady=5, padx=1)
viewer.config(bg='#a3ada1')

# Class to create buttons
class Buttons:
    def __init__(self, color, symbol, column, row, command, fg):
        self.color = color
        self.symbol = symbol
        self.column = column
        self.row = row
        self.command = command
        self.fg = fg

        self.botao = Button(text=symbol, bg=color, command=command, width=5, height=2, font='Arial 18 bold')
        self.botao.grid(column=column, row=row, pady=1, padx=2)
        self.botao.config(fg=fg)

    def change_size(self, width='', height=''):
        self.botao.configure(width=width, height=height)

    def change_padx(self, padx=''):
        self.botao.grid(padx=padx)

equation = ''

# Function to clear the equation
def clear():
    global equation
    equation = ''
    viewer.delete(1.0, END)

# Function that adds the mathematical operators in the equation and shows is the viewer
def click_operator(symbol):
    global equation

    if equation[-1] in "-, +, *, /, .":
        return

    equation += symbol
    viewer.insert(END, symbol)

# Function that calculates the equation
def calculates():
    global equation

    result = str(eval(equation))
    viewer.delete(1.0, END)
    viewer.insert(END, result)

# Function that adds the numbers in the equation and shows in the viewer
def click_number(symbol):
    global equation

    equation += symbol
    viewer.insert(END, symbol)

def cancel_entry():
    global equation

    viewer.delete('end-2c', 'end-1c')
# Operator buttons
clear_button = Buttons('#fcd4e5', 'C', 0, 3, command=lambda: clear(), fg='black')
clear_button.change_size(5, 2)
clear_button.change_padx(4)
cancel_entry_button = Buttons('#fcd4e5', 'CE', 1, 3, command=lambda: cancel_entry(), fg='black')
plus_button = Buttons('#fcd4e5', '+', 3, 5, command=lambda: click_operator('+'), fg='black')
minus_button = Buttons('#fcd4e5', '-', 3, 4, command=lambda: click_operator('-'), fg='black')
multiply_button = Buttons('#fcd4e5', 'x', 2, 3, command=lambda: click_operator('*'), fg='black')
divide_button = Buttons('#fcd4e5', '/', 3, 3, command=lambda: click_operator('/'), fg='black')
equal_button = Buttons('#fcd4e5', '=', 3, 6, command=lambda: calculates(), fg='black')
equal_button.botao.grid(rowspan=2)
equal_button.change_size(5, 5)
comma_button = Buttons('#f05696', ',', 2, 7, command=lambda: click_operator('.'), fg='white')

# Number buttons
zero_button = Buttons('#f05696', '0', 0, 7, command=lambda: click_number('0'), fg='white')
zero_button.botao.grid(columnspan=2)
zero_button.change_size(11, 2)
zero_button.change_padx(4)
one_button = Buttons('#f05696', '1', 0, 6, command=lambda: click_number('1'), fg='white')
one_button.change_padx(4)
two_button = Buttons('#f05696', '2', 1, 6, command=lambda: click_number('2'), fg='white')
three_button = Buttons('#f05696', '3', 2, 6, command=lambda: click_number('3'), fg='white')
four_button = Buttons('#f05696', '4', 0, 5, command=lambda: click_number('4'), fg='white')
four_button.change_padx(4)
five_button = Buttons('#f05696', '5', 1, 5, command=lambda: click_number('5'), fg='white')
six_button = Buttons('#f05696', '6', 2, 5, command=lambda: click_number('6'), fg='white')
seven_button = Buttons('#f05696', '7', 0, 4, command=lambda: click_number('7'), fg='white')
seven_button.change_padx(4)
eight_button = Buttons('#f05696', '8', 1, 4, command=lambda: click_number('8'), fg='white')
nine_button = Buttons('#f05696', '9', 2, 4, command=lambda: click_number('9'), fg='white')

root.mainloop()