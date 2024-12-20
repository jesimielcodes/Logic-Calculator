from tkinter import *

root = Tk()
root.title("Calculator app")

height = 600
width= 400
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.config(bg="#808080")
#root.overrideredirect(True)

input = Entry(root, width=45, font=("Trebuchet Ms", 16))
input.grid(row=0, column=0, columnspan=3, padx=5, pady=5)


truthValues = {'p': True, 'q': True, 'r': True, 's': True, 't': True}


def button_click(char):
    #input.delete(0, END)
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))


def button_clear():
    input.delete(0, END)


def get_truth_value(variable):
    if variable.startswith("¬"):
        variable = variable[1:]
        return not truthValues.get(variable, False)
    else:
        return truthValues.get(variable, False)


def button_disjunction(char):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))
    first_variable = input.get()
    global f_truth_value
    global operator
    operator = "disjunction"
    f_truth_value = get_truth_value(first_variable)
    #input.delete(0, END)


def button_conjunction(char):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))
    first_variable = input.get()
    global f_truth_value
    global operator
    operator = "conjunction"
    f_truth_value = get_truth_value(first_variable)
    #input.delete(0, END)


def button_exclusive_or(char):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))
    first_variable = input.get()
    global f_truth_value
    global operator
    operator = "exclusive or"
    f_truth_value = get_truth_value(first_variable)
    #input.delete(0,END)


def button_implication(char):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))
    first_variable = input.get()
    global f_truth_value
    global operator
    operator = "implication"
    f_truth_value = get_truth_value(first_variable)
    #input.delete(0, END)

def button_biconditional(char):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))
    first_variable = input.get()
    global f_truth_value
    global operator
    operator = "biconditional"
    f_truth_value = get_truth_value(first_variable)
    #input.delete(0, END)


def button_equivalent():
    second_variable = input.get()
    s_truthvalue = get_truth_value(second_variable)
    input.delete(0, END)

    if operator == "disjunction":
        parse = f_truth_value or s_truthvalue
        input.insert(0, "True" if parse else "False")
    elif operator == "conjunction":
        parse = f_truth_value and s_truthvalue
        input.insert(0, "True" if parse else "False")
    elif operator == "exclusive or":
        parse = f_truth_value != s_truthvalue
        input.insert(0, "True" if parse else "False")
    elif operator == "implication":
        parse = not f_truth_value or s_truthvalue
        input.insert(0, "True" if parse else "False")
    elif operator == "biconditional":
        parse = (f_truth_value and s_truthvalue) or (not f_truth_value and not s_truthvalue)
        input.insert(0, "True" if parse else "False")






#AND: ∧
#OR: ∨
#Exclusive OR (XOR): ⊕
#IMPLIES: →
#NEGATION: ¬
#BICONDITIONAL: ↔

btnR = Button(root, text="r", width=10, height=2, command=lambda: button_click('r'), bg="#A9A9A9")
btnImplication = Button(root, text="→", width=10, height=2, command=lambda: button_implication("→"), bg="#A9A9A9")
btnBiconditional = Button(root, text="↔", width=10, height=2, command=lambda: button_biconditional("↔"), bg="#A9A9A9")
btnQ = Button(root, text="q", width=10, height=2, command=lambda: button_click("q"), bg="#A9A9A9")
btnDisjunction = Button(root, text="∨", width=10, height=2, command=lambda: button_disjunction("∨"), bg="#A9A9A9")
btnExclusiveOr = Button(root, text="⊕", width=10, height=2, command=lambda: button_exclusive_or("⊕"), bg="#A9A9A9")
btnP = Button(root, text="p", width=10, height=2, command=lambda: button_click("p"), bg="#A9A9A9")
btnNegation = Button(root, text="¬", width=10, height=2, command=lambda: button_click("¬"), bg="#A9A9A9")
btnConjunction = Button(root, text="∧", width=10, height=2, command=lambda: button_conjunction("∧"), bg="#A9A9A9")
btnS = Button(root, text="s", width=10, height=2, command=lambda: button_click("s"), bg="#A9A9A9")
btnT = Button(root, text="t", width=10, height=2, command=lambda: button_click("t"), bg="#A9A9A9")
closebracketbtn = Button(root, text=")", width=10, height=2, command=lambda: button_click(")"), bg="#A9A9A9")
openbracketbtn = Button(root, text="(", width=10, height=2, command=lambda: button_click("("), bg="#A9A9A9")
equivalentbtn = Button(root, text="=", width=10, height=2, command=lambda: button_equivalent())
clearbtn = Button(root, text="Del", width=10, height=2, command=lambda: button_clear(), bg="#A9A9A9")



btnP.grid(row=1, column=0, padx=1, pady=1, sticky='nsew')
btnQ.grid(row=1, column=1, padx=1, pady=1, sticky='nsew')
btnR.grid(row=1, column=2, padx=1, pady=1, sticky='nsew')

btnS.grid(row=2, column=0, padx=1, pady=1, sticky='nsew')
btnT.grid(row=2, column=1, padx=1, pady=1, sticky='nsew')
clearbtn.grid(row=2, column=2, padx=1, pady=1, sticky='nsew')

btnNegation.grid(row=3, column=0, padx=1, pady=1, sticky='nsew')
btnConjunction.grid(row=3, column=1, padx=1, pady=1, sticky='nsew')
btnDisjunction.grid(row=3, column=2, padx=1, pady=1, sticky='nsew')

btnExclusiveOr.grid(row=4, column=0, padx=1, pady=1, sticky='nsew')
btnImplication.grid(row=4, column=1, padx=1, pady=1, sticky='nsew')
btnBiconditional.grid(row=4, column=2, padx=1, pady=1, sticky='nsew')

openbracketbtn.grid(row=5, column=0, padx=1, pady=1, sticky='nsew')
closebracketbtn.grid(row=5, column=1, padx=1, pady=1, sticky='nsew')
equivalentbtn.grid(row=5, column=2, padx=1, pady=1, sticky='nsew')


for i in range(6):
    root.grid_rowconfigure(i, weight = 1)
for i in range(3):
    root.grid_columnconfigure(i, weight = 1)

root.mainloop()
