from tkinter import *


#AND: ∧
#OR: ∨
#Exclusive OR (XOR): ⊕
#IMPLIES: →
#NEGATION: ¬
#BICONDITIONAL: ↔

logical_representers = {"∧": "&", "∨": "|", "¬": "~", "→": ">>", "↔": "==", "⊕": "^"}


root = Tk()
#root.title = "Complx"
output = Text(root, height=30, width=40, state='disabled', wrap='none')
output.grid(row=1, column=4, rowspan=5, padx=3, pady=2, sticky='nsew')
height = 600
width = 720
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.config(bg="#808080")
#root.overrideredirect(True)


input = Entry(root, width=45, font=("Trebuchet Ms", 17))
input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(char):
    #input.delete(0, END)
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(char))


def button_clear():
    input.delete(0, END)



def button_equivalent():
    compound_proposition = input.get()
    compound_proposition = compound_proposition.replace("∧", "and")
    compound_proposition = compound_proposition.replace("∨", "or")
    compound_proposition = compound_proposition.replace("⊕", "xor")
    compound_proposition = compound_proposition.replace("→", "implies")
    compound_proposition = compound_proposition.replace("¬", "not")
    compound_proposition = compound_proposition.replace("↔", "bicon")

    

    print(compound_proposition)
    #AND: ∧
    #OR: ∨
    #Exclusive OR (XOR): ⊕
    #IMPLIES: →
    #NEGATION: ¬
    #BICONDITIONAL: ↔

        

    my_proposition=compound_proposition
    my_prop=my_proposition
    my_proposition=my_proposition.split(" ")
    my_prop1=my_proposition.copy()

    prop=[]
    for value in my_prop1:
        if (value.isalpha() and len(value)==1) and not(value=="τ" or value=="о́"):
            prop.append(value)
    prop=list(set(prop))
    column_num=len(prop)
    row_num=2**len(prop)
    print(f"length of prop{len(prop)}")
    T_values=[True]*row_num
    F_values=[False]*row_num

    def evaluate_expression(expr):
        
        
        expr = expr.replace("τ", "True")
        expr = expr.replace("о́", "False")
        
        # Base case: if no parentheses are left, evaluate directly
        if '(' not in expr:
            expr = expr.split(" ")
            i = 0
            for value in expr:
                if value == "xor":
                    del expr[i]
                    expr.insert(i, "^")
                if value == "implies":
                    del expr[i]
                    expr.insert(i, "or")
                    expr.insert(i - 1, "not")
                if value == "bicon":
                    expr[i] = "^"  # Replace "implies" with "or"
                    expr.insert(i + 2, ")")
                    expr.insert(i - 1, "(")
                    expr.insert(i - 1, "not")
                i += 1

            expr = " ".join(expr)
            return eval(expr)
        
        # Recursively evaluate expressions inside parentheses
        while '(' in expr:
            expr = expr.split(" ")
            i = 0
            for value in expr:
                if value == "xor":
                    del expr[i]
                    expr.insert(i, "^")
                if value == "implies":
                    del expr[i]
                    expr.insert(i, "or")
                    expr.insert(i - 1, "not")
                if value == "bicon":
                    expr[i] = "^"  # Replace "implies" with "or"
                    expr.insert(i + 2, ")")
                    expr.insert(i - 1, "(")
                    expr.insert(i - 1, "not")
                i += 1

            expr = " ".join(expr)
            start = expr.rfind('(')  # Find the innermost '('
            end = expr.find(')', start)  # Find the corresponding ')'
            sub_expr = expr[start + 1:end]  # Extract the sub-expression inside parentheses
            sub_result = str(evaluate_expression(sub_expr))  # Evaluate and convert to string
            
            expr = expr[:start] + sub_result + expr[end + 1:]  # Replace the parentheses expression with its result

        return eval(expr)  # Evaluate the final expression without parentheses

        # return eval(expr)  # Evaluate the final expression without parentheses



    output.config(state='normal')
    
    output.delete("1.0","end")

    truth_table = [[None for _ in range(column_num)] for _ in range(row_num)]

    #need to simplify this section
    for i in range(column_num):  # Iterate over each column
        cycle_length = 2 ** (column_num - i - 1)
        value = True
        for j in range(row_num):  # Iterate over each row
            truth_table[j][i] = value
            if (j + 1) % cycle_length == 0:
                value = False if value == True else True  # Alternate values

    for val in my_prop1:
        if val=="τ":
            i=0
            for rows in truth_table:
                truth_table[i].append(T_values[i])
                i=i+1
        if val=="о́":
            i=0
            for rows in truth_table:
                truth_table[i].append(F_values[i])
                i=i+1
    print(truth_table)

    results = []
    for row in truth_table:
        eval_proposition = " ".join(
            [str(row[prop.index(value)]) if value in prop else value for value in my_prop1]
        )
        
        results.append(evaluate_expression(eval_proposition))
        
    
    if all(value == True for value in results):
        print("This is a tautology")
        output.insert(END,"This is a tautology")
    elif all(value == False for value in results):
        print("This is a contradiction")
        output.insert(END,"This is a contradiction")
    else:
        print("This is a contingency")
        output.insert(END,"This is a contingency")
    

    # Display the results
    print("Truth Table Results:")
    for row, result in zip(truth_table, results):
        print(row, "=>", result)  

    i=0
    for row in truth_table:
        row.append(results[i])
        i=i+1
    print(truth_table)
    
    i=0
    transformed_list = [["T" if value else "F" for value in row] for row in truth_table]
    output.insert(END,"\n")
    output.insert(END,"\nTruth Table")
    prop.append(compound_proposition)

    head="\n"+"|".join(prop)
    output.insert(END,head)
    for row in transformed_list:
        fin_table="\n"+"|".join(str(cell) for cell in row)
        
        output.insert(END,fin_table)
        i+=1

    output.insert(END,"\n")
    output.insert(END,"\nvalues satisfy the proposition")
    
    head="\n"+"|".join(prop)
    output.insert(END,head)
    satisfied_rows = [row for row in truth_table if row[-1]]
    transformed_list = [["T" if value else "F" for value in row] for row in satisfied_rows]
    print(f"satisfied_rows{satisfied_rows}")
    for row in transformed_list:
        fin_table="\n"+"|".join(str(cell) for cell in row)
        
        output.insert(END,fin_table)
    output.config(state='disabled')
    
   
#AND: ∧
#OR: ∨
#Exclusive OR (XOR): ⊕
#IMPLIES: →
#NEGATION: ¬
#BICONDITIONAL: ↔

btnR = Button(root, text="r", width=10, height=2, command=lambda: button_click('r '), bg="#A9A9A9")
btnImplication = Button(root, text="→", width=10, height=2, command=lambda: button_click('→ '), bg="#A9A9A9")
btnBiconditional = Button(root, text="↔", width=10, height=2, command=lambda: button_click('↔ '), bg="#A9A9A9")
btnQ = Button(root, text="q", width=10, height=2, command=lambda: button_click('q '), bg="#A9A9A9")
btnDisjunction = Button(root, text="∨", width=10, height=2, command=lambda: button_click('∨ '), bg="#A9A9A9")
btnExclusiveOr = Button(root, text="⊕", width=10, height=2, command=lambda: button_click('⊕ '), bg="#A9A9A9")
btnP = Button(root, text="p", width=10, height=2, command=lambda: button_click("p "), bg="#A9A9A9")
btnNegation = Button(root, text="¬", width=10, height=2, command=lambda: button_click("¬ "), bg="#A9A9A9")
btnConjunction = Button(root, text="∧", width=10, height=2, command=lambda: button_click('∧ '), bg="#A9A9A9")
btnS = Button(root, text="s", width=10, height=2, command=lambda: button_click("s "), bg="#A9A9A9")
btnT = Button(root, text="t", width=10, height=2, command=lambda: button_click("t "), bg="#A9A9A9")
closebracketbtn = Button(root, text=")", width=10, height=2, command=lambda: button_click(") "), bg="#A9A9A9")
openbracketbtn = Button(root, text="(", width=10, height=2, command=lambda: button_click("( "), bg="#A9A9A9")
equivalentbtn = Button(root, text="=", width=10, height=2, command=lambda: button_equivalent())

clearbtn = Button(root, text="Del", width=10, height=2, command=lambda: button_clear(), bg="#A9A9A9")
#Truebutn = Button(root, text="T", width=10, height=2, command=lambda: button_click("T"), bg="#A9A9A9")
#Falsebutn = Button(root, text="F", width=10, height=2, command=lambda: button_click("F"), bg="#A9A9A9")

btnP.grid(row=1, column=0, padx=1, pady=1, sticky='nsew')
btnQ.grid(row=1, column=1, padx=1, pady=1, sticky='nsew')
btnR.grid(row=1, column=2, padx=1, pady=1, sticky='nsew')

btnS.grid(row=2, column=0, padx=1, pady=1, sticky='nsew')
btnT.grid(row=2, column=1, padx=1, pady=1, sticky='nsew')
clearbtn.grid(row=2, column=2, padx=1, pady=1, sticky='nsew')

btnCon = Button(root, text ="F", padx = 40, pady= 20, command = lambda: button_click("о́ "))
btnTau = Button(root, text="T", width=10, height=2, command=lambda: button_click("τ "), bg="#A9A9A9")
btnCon = Button(root, text="F", width=10, height=2, command=lambda: button_click("о́ "), bg="#A9A9A9")

btnTau.grid(row=6, column=0, padx=5, pady=5, sticky='nsew')
btnCon.grid(row=6, column=1, padx=5, pady=5, sticky='nsew')

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