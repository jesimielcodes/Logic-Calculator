from tkinter import *
from sympy import symbols, sympify
from sympy.logic.boolalg import truth_table

#AND: ∧
#OR: ∨
#Exclusive OR (XOR): ⊕
#IMPLIES: →
#NEGATION: ¬
#BICONDITIONAL: ↔

logical_representers = {"∧": " & ", "∨": " | ", "¬": "~", "→": ">>", "↔": "==", "⊕": " ^ "}
p, q, r, s, t = symbols('p q r s t')

def sympy_translation(statement):
    for key, value in logical_representers.items():
        statement = statement.replace(key, value)
    return statement

#creating and customizing window
root = Tk()
root.title("LOGICALC")
height = 600
width = 720
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.config(bg="#808080")
#root.overrideredirect(True)

#creating the field for text input and setting the dimensions and placing
input = Entry(root, width=45, font=("Trebuchet Ms", 17))
input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


#truthValues = {'p': True, 'q': True, 'r': True, 's': True, 't': True, 'T': True, 'F': False}


def button_click(char):
    #input.delete(0, END)
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))

def button_clicked(symbol):
    #input.delete(0, END)
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(symbol))


def button_clear():
    input.delete(0, END)


"""def get_truth_value(variable):
    if variable.startswith("¬"):
        variable = variable[1:]
        return not truthValues.get(variable, False)
    else:
        return truthValues.get(variable, False)"""


def button_disjunction(char):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))
    first_variable = input.get()
    global f_truth_value
    global operator
    operator = "disjunction"
    #f_truth_value = get_truth_value(first_variable)
    #input.delete(0, END)


def button_conjunction(char):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))
    first_variable = input.get()
    global f_truth_value
    global operator
    operator = "conjunction"
    #f_truth_value = get_truth_value(first_variable)
    #input.delete(0, END)


def button_exclusive_or(char):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))
    first_variable = input.get()
    global f_truth_value
    global operator
    operator = "exclusive or"
    #f_truth_value = get_truth_value(first_variable)
    #input.delete(0,END)


def button_implication(char):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))
    first_variable = input.get()
    global f_truth_value
    global operator
    operator = "implication"
    #f_truth_value = get_truth_value(first_variable)
    #input.delete(0, END)


def button_biconditional(char):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))
    first_variable = input.get()
    global f_truth_value
    global operator
    operator = "biconditional"
    #f_truth_value = get_truth_value(first_variable)
    #input.delete(0, END)


def button_equivalent(char):
    second_variable=input.get()
    #s_truthvalue = get_truth_value(second_variable)
    try:
        """if operator == "disjunction":
            parse = f_truth_value or s_truthvalue
            #input.insert(0, "True" if parse else "False")
        elif operator == "conjunction":
            parse = f_truth_value and s_truthvalue
            #input.insert(0, "True" if parse else "False")
        elif operator == "exclusive or":
            parse = f_truth_value != s_truthvalue
            #input.insert(0, "True" if parse else "False")
        elif operator == "implication":
            parse = not f_truth_value or s_truthvalue
            #input.insert(0, "True" if parse else "False")
        elif operator == "biconditional":
            parse = (f_truth_value and s_truthvalue) or (not f_truth_value and not s_truthvalue)
            #input.insert(0, "True" if parse else "False")"""

        print(second_variable)
        sympy_format = sympy_translation(second_variable)
        print(sympy_format)

        sympy_evaluation = sympify(sympy_format)
        print(sympy_evaluation)
        atomic_propositions = sorted(sympy_evaluation.free_symbols, key=lambda x: str(x))
        print(sympy_evaluation.free_symbols)

        evaluated_truth_table = truth_table(sympy_evaluation, atomic_propositions)


        output.config(state='normal')
        output.delete(1.0, "end")
        header = " | ".join([str(variable) for variable in atomic_propositions]) + " |" + second_variable + "\n"
        output.insert(END, header)
        output.insert(END, "-" * (len(header) + 2) + "\n")

        classification_column = []
        propositional_satisfiability_rows = []

        for row in evaluated_truth_table:
            classification_column.append(row[1])
            line = " | ".join(map(lambda x: "T" if x else "F", row[0])) + " | " + ("T" if row[1] else "F") + "\n"
            output.insert(END, line)

            if row[1]:
                propositional_satisfiability_rows.append(row[0])
        output.config(state='disabled')

        if all(classification_column):
            classification = "Tautology"
        elif not any(classification_column):
            classification = "Contradiction"
        else:
            classification = "Contingency"

        propositional_satisfiability = any(classification_column)

        output.config(state='normal')
        output.insert(END, "\n\nClassification: " + classification + "\n")
        if propositional_satisfiability is True:
            output.insert(END, "Propositional satisfiability exists\n\n")
            for row in propositional_satisfiability_rows:
                line = " | ".join(map(lambda x: "T" if x else "F", row)) + " | T\n"
                output.insert(END, line)
        else:
            output.insert(END, "No propositional satisfiability")
        output.config(state='disabled')
    except Exception as e:
        print("Error message: ",e)
        error_message = "Input error! Retry"
        input.insert(0, error_message)




#AND: ∧
#OR: ∨
#Exclusive OR (XOR): ⊕
#IMPLIES: →
#NEGATION: ¬
#BICONDITIONAL: ↔

btnR = Button(root, text="r", width=10, height=2, command=lambda: button_clicked(r), bg="#A9A9A9")
btnImplication = Button(root, text="→", width=10, height=2, command=lambda: button_implication("→"), bg="#A9A9A9")
btnBiconditional = Button(root, text="↔", width=10, height=2, command=lambda: button_biconditional("↔"), bg="#A9A9A9")
btnQ = Button(root, text="q", width=10, height=2, command=lambda: button_clicked(q), bg="#A9A9A9")
btnDisjunction = Button(root, text="∨", width=10, height=2, command=lambda: button_disjunction("∨"), bg="#A9A9A9")
btnExclusiveOr = Button(root, text="⊕", width=10, height=2, command=lambda: button_exclusive_or("⊕"), bg="#A9A9A9")
btnP = Button(root, text="p", width=10, height=2, command=lambda: button_clicked(p), bg="#A9A9A9")
btnNegation = Button(root, text="¬", width=10, height=2, command=lambda: button_click("¬"), bg="#A9A9A9")
btnConjunction = Button(root, text="∧", width=10, height=2, command=lambda: button_conjunction("∧"), bg="#A9A9A9")
btnS = Button(root, text="s", width=10, height=2, command=lambda: button_clicked(s), bg="#A9A9A9")
btnT = Button(root, text="t", width=10, height=2, command=lambda: button_clicked(t), bg="#A9A9A9")
closebracketbtn = Button(root, text=")", width=10, height=2, command=lambda: button_click(")"), bg="#A9A9A9")
openbracketbtn = Button(root, text="(", width=10, height=2, command=lambda: button_click("("), bg="#A9A9A9")
equivalentbtn = Button(root, text="=", width=10, height=2, command=lambda: button_equivalent("="))

clearbtn = Button(root, text="Del", width=10, height=2, command=lambda: button_clear(), bg="#A9A9A9")
#Truebutn = Button(root, text="T", width=10, height=2, command=lambda: button_click("T"), bg="#A9A9A9")
#Falsebutn = Button(root, text="F", width=10, height=2, command=lambda: button_click("F"), bg="#A9A9A9")

btnP.grid(row=1, column=0, padx=1, pady=1, sticky='nsew')
btnQ.grid(row=1, column=1, padx=1, pady=1, sticky='nsew')
btnR.grid(row=1, column=2, padx=1 , pady=1, sticky='nsew')

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

#Truebutn.grid(row=6, column=0, padx=1, pady=1, sticky='nsew')
#Falsebutn.grid(row=6, column=2, padx=1, pady=1, sticky='nsew')

output = Text(root, height=30, width=40, state='disabled', wrap='none')
output.grid(row=1, column=4, rowspan=5, padx=3, pady=2, sticky='nsew')

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

"""compound_proposition = input.get("1.0", "end-1c")

    sympy_format = sympy_translation(compound_proposition)
    sympy_evaluation = sympify(sympy_format)
    atomic_propositions = sorted(sympy_evaluation.free_symbols, key=lambda x: str(x))
    evaluated_truth_table = truth_table(sympy_evaluation, atomic_propositions)

    output.config(state='normal')  # Make it editable
    output.delete(1.0, "end")  # Clear previous content
    header = " | ".join([str(prop) for prop in atomic_propositions]) + " |" +compound_proposition+"\n"
    output.insert(END, header)
    output.insert(END, "-" * (len(header) + 2) + "\n")
    for row in evaluated_truth_table:
        line = " | ".join(map(str, row[0])) + " | " + str(row[1]) + "\n"
        output.insert(END, line)
    output.config(state='disabled')"""
