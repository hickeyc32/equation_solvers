from sympy import *
x=symbols('x')





def bisection_method(expr,epsilon,a,b):
    x=symbols('x')
    i=0
    f=sympify(expr)
    fa=f.subs(x,a);
    fb=f.subs(x,b);
   
    if (fa*fb)>0:
        print"\n\n No root exists on this interval. \n\n"

    else:
        print "\n\n"      
        print "#         a              f(a)         c            f(c)            b           f(b)"
        while (b-a)>epsilon:
            c=(b+a)/2
            fc=f.subs(x,c);
            print i,"    ",'%.4f' % (a),"       ",'%.4f' % (fa),"     ",'%.4f' % (c),"      ",'%.4f' % (fc),"      ",'%.4f' % (b),"     ",'%.4f' % (fb)
        
            fa=f.subs(x,a);
            fb=f.subs(x,b);
       
            if fc==0:
                break
            elif fa*fc<0:
                b=c
            else:
                a=c
        
        
       
            i+=1
    




func=str(input("Provide a function: "))
eps=(input("Provide an epsilon: "))
b1=float(input("Provide an initial upper guess: "))
a1=float(input("And an initial lower guess: "))

bisection_method(func,eps,a1,b1)
