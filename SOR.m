clear
format long



steps=9;    
w=1.25;





an=0;
bn=0;
cn=0;
fprintf("\n\n")
fprintf("#        an              bn             cn\n")

for i=1:steps
    
    
  an=(1-w)*an+w*(4-bn+cn)/3;
  
  bn=(1-w)*bn+w*(1-2*an-cn)/4;
  
  cn=(1-w)*cn+w*(1+an-2*bn)/5;
  
  
 fprintf("%d    %.8f     %.8f     %.8f\n",i,an,bn,cn)
end