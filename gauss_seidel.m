clear
format long




steps=2;    


an=0;
bn=0;
cn=0;

fprintf("#        an             bn             cn\n")

for i=1:steps
  an=(3-bn+cn)/4;
  
  bn=(19-2*an-cn)/7;
  
  cn=(31-an+3*bn)/12;
  
  
 fprintf("%d    %.8f     %.8f     %.8f\n",i,an,bn,cn)
end