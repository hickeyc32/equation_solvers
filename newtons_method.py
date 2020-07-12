from sympy import *
init_printing(use_unicode=True)
x=symbols('x')



def newtons_method(expr,epsilon,x_start):
    x=symbols('x')
    f=sympify(expr)
    x_naught=float(x_start)
    df=diff(f,x)

    print"\n\n"
    print'#           x'
    print'0        ', x_naught

    for i in range(1,200):   
    
        f_naught=f.subs(x,x_naught)
        df_naught=df.subs(x,x_naught)
  
        x_one=x_naught-(f_naught/df_naught)   
  
  
        if abs(x_one-x_naught) < epsilon:
            break
          
  
        print i,"        ",x_one
  
        x_naught=x_one



function=str(input("Provide a function: "))
ep=float(input("Provide an epsilon: "))
initialx=float(input("And give an initial guess: "))
newtons_method(function,ep,initialx)
