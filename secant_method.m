clear
syms x;


f=x^2-5;
x0=2;
x1=3;
steps=4;


xn=x1;
xn_minus_1=x0;


fprintf("\n\n")
fprintf("#           x\n")
fprintf("%d      %.8f\n",0,x0)
fprintf("%d      %.8f\n",1,x1)
for i=2:steps
    
    fxn=subs(f,x,xn);
    fxn_minus_1=subs(f,x,xn_minus_1);
    xn_plus_1=xn-fxn*(xn-xn_minus_1)/(fxn-fxn_minus_1);
    
    fprintf("%d      %.8f\n",i,xn_plus_1)
    
    xn_minus_1=xn;
    xn=xn_plus_1;
    
end