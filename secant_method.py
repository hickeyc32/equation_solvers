from sympy import *
x=symbols('x')




def secant_method(expr,x0,x1,steps):
    x=symbols('x')
    f=sympify(expr)
    xn=x1
    xn_minus_1=x0


    print"\n\n"
    print"#             x"
    print 0,"      ",'%.8f'% (x0)
    print 1,"      ",'%.8f'% (x1)
    for i in range (2,steps+1):
    
        fxn=f.subs(x,xn)
        fxn_minus_1=f.subs(x,xn_minus_1)
        xn_plus_1=xn-fxn*(xn-xn_minus_1)/(fxn-fxn_minus_1)
    
        print i,"      ",'%.8f'% (xn_plus_1)
    
        xn_minus_1=xn
        xn=xn_plus_1
    


func=str(input("Provide a function: "))
s=int(input("How many iterations?: "))
b=float(input("Provide an initial upper guess: "))
a=float(input("And an initial lower guess: "))


secant_method(func,a,b,s)
