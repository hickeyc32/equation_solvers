clear
format long
syms x;



x0=.5;
steps=25;



fprintf("\n\n")
fprintf("#          x      ei         ei/ei_1\n")
fprintf("%d     %.8f        %.8f        %.8f\n",0,x0)
x=x0;
for i=1:steps
    x=(1-x)^(1/3);

fprintf("%d     %.8f\n",i,x)
end