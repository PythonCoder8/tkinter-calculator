import tkinter as tk

equation = ''

def edit_equation(char):
    global equation
    equation += char
    equation_field.delete(1.0, 'end')
    equation_field.insert(1.0, equation)

def solve_equation():
    global equation
    try:
        answer = str(eval(equation))
        equation = ''
        equation_field.delete(1.0, 'end')
        equation_field.insert(1.0, answer)

    except:
        equation_field.delete(1.0, 'end')
        equation_field.insert(1.0, 'ERROR')

def clear():
    global equation
    equation = ''
    equation_field.delete(1.0, 'end')

root = tk.Tk()
root.resizable(False, False)
root.title('Calculator')
root.geometry('293x275')

equation_field = tk.Text(root, height=2, width=16, font=('Arial', 24))
equation_field.grid(columnspan=5)

b_1 = tk.Button(root, text='1', command=lambda: edit_equation('1'), width=5, font=('Arial', 14))
b_1.grid(row=2, column=1)
b_2 = tk.Button(root, text='2', command=lambda: edit_equation('2'), width=5, font=('Arial', 14))
b_2.grid(row=2, column=2)
b_3 = tk.Button(root, text='3', command=lambda: edit_equation('3'), width=5, font=('Arial', 14))
b_3.grid(row=2, column=3)
b_4 = tk.Button(root, text='4', command=lambda: edit_equation('4'), width=5, font=('Arial', 14))
b_4.grid(row=3, column=1)
b_5 = tk.Button(root, text='5', command=lambda: edit_equation('5'), width=5, font=('Arial', 14))
b_5.grid(row=3, column=2)
b_6 = tk.Button(root, text='6', command=lambda: edit_equation('6'), width=5, font=('Arial', 14))
b_6.grid(row=3, column=3)
b_7 = tk.Button(root, text='7', command=lambda: edit_equation('7'), width=5, font=('Arial', 14))
b_7.grid(row=4, column=1)
b_8 = tk.Button(root, text='8', command=lambda: edit_equation('8'), width=5, font=('Arial', 14))
b_8.grid(row=4, column=2)
b_9 = tk.Button(root, text='9', command=lambda: edit_equation('9'), width=5, font=('Arial', 14))
b_9.grid(row=4, column=3)
b_0 = tk.Button(root, text='0', command=lambda: edit_equation('0'), width=5, font=('Arial', 14))
b_0.grid(row=5, column=2)
b_p1 = tk.Button(root, text='(', command=lambda: edit_equation('('), width=5, font=('Arial', 14))
b_p1.grid(row=5, column=1)
b_p2 = tk.Button(root, text=')', command=lambda: edit_equation(')'), width=5, font=('Arial', 14))
b_p2.grid(row=5, column=3)
b_plus = tk.Button(root, text='+', command=lambda: edit_equation('+'), width=5, font=('Arial', 14))
b_plus.grid(row=2, column=4)
b_minus = tk.Button(root, text='-', command=lambda: edit_equation('+'), width=5, font=('Arial', 14))
b_minus.grid(row=3, column=4)
b_mul = tk.Button(root, text='*', command=lambda: edit_equation('*'), width=5, font=('Arial', 14))
b_mul.grid(row=4, column=4)
b_div = tk.Button(root, text='/', command=lambda: edit_equation('/'), width=5, font=('Arial', 14))
b_div.grid(row=5, column=4)
b_equate = tk.Button(root, text='=', command=solve_equation, width=11, font=('Arial', 14))
b_equate.grid(row=6, column=1, columnspan=2)
b_clear = tk.Button(root, text='CLEAR', command=clear, width=11, font=('Arial', 14))
b_clear.grid(row=6, column=3, columnspan=2)
root.mainloop()
