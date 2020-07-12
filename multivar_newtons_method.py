from sympy import *
u,v,w=symbols('u v w')
init_printing()






def multivar_newtons_method(*args):
    u,v,w=symbols('u v w')
    if len(args)==5:
        f1=sympify(args[0])
        f2=sympify(args[1])
        u0=args[2]
        v0=args[3]
        steps=args[4]
        df1_1=diff(f1,u)
        df1_2=diff(f1,v)
        df2_1=diff(f2,u)
        df2_2=diff(f2,v)
        F=Matrix([[f1],[f2]])
        DF=Matrix([[df1_1,df1_2],[df2_1,df2_2]])
        print"\n\n"
        print 0,"    ",'%.4f' % (u0),"       ",'%.4f' % (v0)
        for i in range (1,steps+1):
            x0=Matrix([[u0],[v0]])
            F0=((F.subs(u,u0)).subs(v,v0))*-1
            
            DF0=(DF.subs(u,u0)).subs(v,v0)
            
            system=(DF0.col_insert(2,F0)).rref()
            sol=system[0]
            s=sol.col(-1)
            x1=Matrix(x0+s)
            u0=x1[0,0]
            v0=x1[1,0]
        
            if i<10:
                print i,"    ",'%.4f' % (u0),"       ",'%.4f' % (v0)
            else:
                print i,"   ",'%.4f' % (u0),"       ",'%.4f' % (v0)
    elif len(args)==7:
       
        f1=sympify(args[0])
        f2=sympify(args[1])
        f3=sympify(args[2])
        u0=args[3]
        v0=args[4]
        w0=args[5]
        steps=args[6]
        df1_1=diff(f1,u)
        df1_2=diff(f1,v)
        df1_3=diff(f1,w)
        df2_1=diff(f2,u)
        df2_2=diff(f2,v)
        df2_3=diff(f2,w)
        df3_1=diff(f3,u)
        df3_2=diff(f3,v)
        df3_3=diff(f3,w)
        F=Matrix([[f1],[f2],[f3]])
        DF=Matrix([[df1_1,df1_2,df1_3],[df2_1,df2_2,df2_3],[df3_1,df3_2,df3_3]])
        print"\n\n"
        print 0,"    ",'%.4f' % (u0),"       ",'%.4f' % (v0),"       ",'%.4f' % (w0)
        for i in range (1,steps+1):
            x0=Matrix([[u0],[v0],[w0]])
            F0=(((F.subs(u,u0)).subs(v,v0)).subs(w,w0))*-1
            
            DF0=((DF.subs(u,u0)).subs(v,v0)).subs(w,w0)
            
            system=(DF0.col_insert(3,F0)).rref()
            sol=system[0]
            s=sol.col(-1)
            x1=Matrix(x0+s)
            u0=x1[0,0]
            v0=x1[1,0]
            w0=x1[2,0]
        
            if i<10:
                print i,"    ",'%.4f' % (u0),"       ",'%.4f' % (v0),"       ",'%.4f' % (w0)
            else:
                print i,"   ",'%.4f' % (u0),"       ",'%.4f' % (v0),"       ",'%.4f' % (w0)
        
    else:
        print "System must be of 2 or 3 variables"


choice=input("How many variables are used? 2 or 3 (u,v,w)")        
while choice!=2 and choice!=3:
    print "System must be of 2 or 3 variables\n\n"
    
    choice=input("How many variables are used? 2 or 3 (u,v,w)") 

if choice==2:
    f1=str(input("Provide the first function: "))
    f2=str(input("Provide the second function: "))
    u0=float(input("Give an initial guess for u: "))
    v0=float(input("Give an initial guess for v: "))
    s=int(input("And how many iterations?"))
    multivar_newtons_method(f1,f2,u0,v0,s)
elif choice==3:
 
    f1=str(input("Provide the first function: "))
    f2=str(input("Provide the second function: "))
    f3=str(input("Provide the third function: "))
    u0=float(input("Give an initial guess for u: "))
    v0=float(input("Give an initial guess for v: "))
    w0=float(input("Give an initial guess for w: "))
    s=int(input("And how many iterations?"))
    multivar_newtons_method(f1,f2,f3,u0,v0,w0,s)

    


