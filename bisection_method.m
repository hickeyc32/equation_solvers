clear
syms x;
i=0;


%CHANGE VALUES FOR PROBLEM HERE:
epsilon=.001;
f=x^6-x-1;
a=1;
b=2;



fa=subs(f,x,a);
fb=subs(f,x,b);

if fa*fb>0
    fprintf("\n\n No root exists on this interval. \n\n")

else
    fprintf("\n\n")       
    fprintf("#       a         f(a)         c          f(c)          b         f(b)\n")
    while (b-a)>epsilon
        c=(b+a)/2;
        fc=subs(f,x,c);
        fprintf("%d    %.4f     %.4f     %.4f      %.4f      %.4f     %.4f\n",i,a,fa,c,fc,b,fb)
        
        fa=subs(f,x,a);
        fb=subs(f,x,b);
       
        if fc==0
            break
        elseif fa*fc<0
            b=c;
        else
            a=c;
        end
        
       
       i=1+i;
    end
end