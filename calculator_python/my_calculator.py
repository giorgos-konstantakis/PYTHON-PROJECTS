from tkinter import *
import math
from math import*

# Initialization
expression=""

# Creating the tkinter surface
calculator = Tk()

# Title
calculator.title("CALCULATOR")
calculator.configure(background="pale turquoise")

# click function
def click(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression)

# clear function
def clear():
    entry.delete(0,END)
        
# equal function
def equal(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
        equation.set(" error ") 
        expression = ""    

    

# Equation's expression setup ( calculator's entry ) 
equation = StringVar() 
entry = Entry(calculator, textvariable=equation,width=130,borderwidth=10,bg="white",fg="blue")
entry.grid(row=0,column=0,columnspan=5,padx=20,pady=20)

# Calculator's buttons
button_1 = Button(calculator,text="1",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click(1))
button_2 = Button(calculator,text="2",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click(2))
button_3 = Button(calculator,text="3",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click(3))
button_4 = Button(calculator,text="4",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click(4))
button_5 = Button(calculator,text="5",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click(5))
button_6 = Button(calculator,text="6",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click(6))
button_7 = Button(calculator,text="7",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click(7))
button_8 = Button(calculator,text="8",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click(8))
button_9 = Button(calculator,text="9",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click(9))
button_0 = Button(calculator,text="0",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click(0))
button_add = Button(calculator,text="+",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("+"))
button_sub = Button(calculator,text="-",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("-"))
button_mult = Button(calculator,text="*",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("*"))
button_div = Button(calculator,text="/",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("/"))
button_square = Button(calculator,text="square(x^2) (x)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("**"))
button_equal = Button(calculator,text="=",width=50,padx=227,pady=20,bg="dark turquoise",fg="midnight blue",command=equal)
button_clear = Button(calculator,text="CLEAR CALCULATOR",width=50,padx=227,pady=20,bg="dark turquoise",fg="midnight blue",command=clear)
button_logar_10 = Button(calculator,text="log10 (x)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("log10"))
button_right_par = Button(calculator,text=")",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click(")"))
button_left_par = Button(calculator,text="(",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("("))
button_exper = Button(calculator,text="exp (x)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("exp"))
button_logar_2 = Button(calculator,text="log2 (x)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("log2"))
button_deg_to_rad = Button(calculator,text="deg to rad (x)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("radians"))
button_rad_to_deg = Button(calculator,text="rad to deg (x)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("degrees"))
button_dot = Button(calculator,text="comma(for floats)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("."))
button_power = Button(calculator,text="power(x^y)(x,y)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("pow"))
button_square_root = Button(calculator,text="square root (x)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("sqrt"))
button_cosine = Button(calculator,text="cos(x)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("cos"))
button_sine = Button(calculator,text="sin(x)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("sin"))
button_tann = Button(calculator,text="tan(x)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("tan"))
button_modulo = Button(calculator,text="mod(x,y)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("mod"))
button_fact = Button(calculator,text="factorial(x)",width=10,padx=30,pady=20,bg="dark turquoise",fg="midnight blue",command=lambda:click("factorial"))

# Buttons' grids
button_1.grid(row=1,column=1)
button_2.grid(row=1,column=2)                 
button_3.grid(row=1,column=3)
button_4.grid(row=1,column=4)
button_5.grid(row=2,column=0)
button_6.grid(row=2,column=1)
button_7.grid(row=2,column=2)
button_8.grid(row=2,column=3)
button_9.grid(row=2,column=4)
button_0.grid(row=1,column=0)
button_add.grid(row=3,column=0)
button_sub.grid(row=3,column=1)
button_mult.grid(row=3,column=2)
button_div.grid(row=3,column=3)
button_square.grid(row=3,column=4)
button_equal.grid(row=7,column=0,columnspan=5)
button_clear.grid(row=8,column=0,columnspan=5)
button_logar_10.grid(row=4,column=2)
button_right_par.grid(row=4,column=1)
button_left_par.grid(row=4,column=0)
button_exper.grid(row=4,column=3)
button_logar_2.grid(row=4,column=4)
button_deg_to_rad.grid(row=5,column=0)
button_rad_to_deg.grid(row=5,column=1)
button_dot.grid(row=5,column=2) 
button_power.grid(row=5,column=3)
button_square_root.grid(row=5,column=4)
button_cosine.grid(row=6,column=0)
button_sine.grid(row=6,column=1)
button_tann.grid(row=6,column=2)
button_modulo.grid(row=6,column=3)
button_fact.grid(row=6,column=4)

calculator.mainloop()







