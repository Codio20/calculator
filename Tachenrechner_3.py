import tkinter as tk

main = tk.Tk()
main.title("Taschenrechner Version 3.0")
main.geometry("366x320")


calculation = ""

text_result = tk.Text(main, height=5, width=46)
text_result.place(x=0, y=0)

def add_to_calculation(symbol):
    global calculation
    if symbol == "*10**" and not calculation:
        calculation += str("10**")
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    else:
        calculation += str(symbol)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def delete_last_entry():
    global calculation
    if calculation[-5:] == "*10**":
        calculation = calculation[:-5]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    elif calculation[-4:] == "10**":
        calculation = calculation[:-4]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    elif calculation[-2:] == "**":
        calculation = calculation[:-2]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    elif calculation[-5:] == "**0.5":
        calculation = calculation[:-5]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    elif calculation[-3:] == "**2":
        calculation = calculation[:-3]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    elif calculation[-5:] == "**(1/":
        calculation = calculation[:-5]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    else:
        calculation = calculation[:-1]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation

    if "**(1/" in calculation and calculation[-1] != ")":
        calculation += str(")")
        print(calculation)
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        calculation = ""
        text_result.insert(1.0, "Syntaxfehler")

def ende_calculation():
    main.destroy()

btn_xhochn = tk.Button(main, text="x^n", height=1, width=6, fg="white", bg="black", command=lambda: add_to_calculation("**"))
btn_xhochn.place(x=10, y=90)

btn_hoch2 = tk.Button(main, text="x^2", height=1, width=6, fg="white", bg="black", command=lambda: add_to_calculation("**2"))
btn_hoch2.place(x=68.333333, y=90)

btn_klammer_auf = tk.Button(main, text="(", height=1, width=6, fg="white", bg="black", command=lambda: add_to_calculation("("))
btn_klammer_auf.place(x=126.666666, y=90)

btn_klammer_zu = tk.Button(main, text=")", height=1, width=6, fg="white", bg="black", command=lambda: add_to_calculation(")"))
btn_klammer_zu.place(x=185, y=90)

btn_wurzel = tk.Button(main, text="sqrt", height=1, width=6, fg="white", bg="black", command=lambda: add_to_calculation("**0.5"))
btn_wurzel.place(x=243.333333, y=90)

btn_wurzel_n = tk.Button(main, text="sqrt^n", height=1, width=6, fg="white", bg="black", command=lambda: add_to_calculation("**(1/"))
btn_wurzel_n.place(x=301.666666, y=90)

btn_7 = tk.Button(main, text="7", height=2, width=7, font=("Arial", 10), bg="grey" ,fg="white", command=lambda: add_to_calculation("7"))
btn_7.place(x=10 , y=120)

btn_8 = tk.Button(main, text="8", height=2, width=7, font=("Arial", 10), bg="grey" ,fg="white", command=lambda: add_to_calculation("8"))
btn_8.place(x=80 , y=120)

btn_9 = tk.Button(main, text="9", height=2, width=7, font=("Arial", 10), bg="grey" ,fg="white", command=lambda: add_to_calculation("9"))
btn_9.place(x=150 , y=120)

btn_del = tk.Button(main, text="DEL", height=2, width=7, font=("Arial", 10), bg="blue",fg="white", command=delete_last_entry)
btn_del.place(x=220 , y=120)

btn_ac = tk.Button(main, text="AC", height=2, width=7, font=("Arial", 10), bg="blue",fg="white", command=clear_field)
btn_ac.place(x=290, y=120)

btn_4 = tk.Button(main, text="4", height=2, width=7, font=("Arial", 10), bg="grey" ,fg="white", command=lambda: add_to_calculation("4"))
btn_4.place(x=10 , y=170)

btn_5 = tk.Button(main, text="5", height=2, width=7, font=("Arial", 10), bg="grey" ,fg="white", command=lambda: add_to_calculation("5"))
btn_5.place(x=80 , y=170)

btn_6 = tk.Button(main, text="6", height=2, width=7, font=("Arial", 10), bg="grey" ,fg="white", command=lambda: add_to_calculation("6"))
btn_6.place(x=150 , y=170)

btn_mult = tk.Button(main, text="x", height=2, width=7, font=("Arial", 10), bg="orange",fg="white", command=lambda: add_to_calculation("*"))
btn_mult.place(x= 220, y=170)

btn_div = tk.Button(main, text="/", height=2, width=7, font=("Arial", 10), bg="orange",fg="white", command=lambda: add_to_calculation("/"))
btn_div.place(x=290 , y=170)

btn_1 = tk.Button(main, text="1", height=2, width=7, font=("Arial", 10), bg="grey" ,fg="white", command=lambda: add_to_calculation("1"))
btn_1.place(x=10 , y=220)

btn_2 = tk.Button(main, text="2", height=2, width=7, font=("Arial", 10), bg="grey" ,fg="white", command=lambda: add_to_calculation("2"))
btn_2.place(x=80, y=220)

btn_3 = tk.Button(main, text="3", height=2, width=7, font=("Arial", 10), bg="grey" ,fg="white", command=lambda: add_to_calculation("3"))
btn_3.place(x=150 , y=220)

btn_add = tk.Button(main, text="+", height=2, width=7, font=("Arial", 10), bg="orange",fg="white", command=lambda: add_to_calculation("+"))
btn_add.place(x=220 , y=220)

btn_sub = tk.Button(main, text="-", height=2, width=7, font=("Arial", 10), bg="orange",fg="white", command=lambda: add_to_calculation("-"))
btn_sub.place(x=290 , y=220)

btn_0 = tk.Button(main, text="0", height=2, width=7, font=("Arial", 10), bg="grey" ,fg="white", command=lambda: add_to_calculation("0"))
btn_0.place(x=10, y=270)

btn_komma = tk.Button(main, text=",", height=2, width=7, font=("Arial", 10), bg="white",fg="black", command=lambda: add_to_calculation("."))
btn_komma.place(x=80 , y=270)

btn_potenzn = tk.Button(main, text="x10^", height=2, width=7, font=("Arial", 10), bg="white",fg="black", command=lambda: add_to_calculation("*10**"))
btn_potenzn.place(x=150, y=270)

btn_power = tk.Button(main, text="OFF", height=2, width=7, font=("Arial", 10), bg="red",fg="white", command=ende_calculation)
btn_power.place(x=220, y=270)

btn_equal = tk.Button(main, text="=", height=2, width=7, font=("Arial", 10), bg="orange",fg="white", command=evaluate_calculation)
btn_equal.place(x=290, y=270)

main.mainloop()
