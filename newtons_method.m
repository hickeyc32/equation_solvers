clear
format long
syms x;



%CHANGE THESE VALUES FOR THE PROBLEM:
epsilon=.1;
x0=-.7;
f=x^3+x-1;


fprintf("\n\n")
fprintf("#       x\n")
fprintf("0    %.8f\n",x0)
df=diff(f,x);

for i=1:200
   
    
  f0=subs(f,x,x0);
  df0=subs(df,x,x0);
  
  x1=x0-f0/df0;
   
  
  
  if abs(x1-x0) < epsilon
      break
  end  
  
 fprintf("%d    %.8f\n",i,x1)
  
  x0=x1;
  
end  