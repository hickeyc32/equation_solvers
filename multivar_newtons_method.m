clear
format long
syms u v;






%CHANGE THESE VALUES FOR THE PROBLEM:
u0=1;
v0=1;
f1=u^2+v^2-1;
f2=(u-1)^2+v^2-1;
steps=15;






fprintf("\n\n")
fprintf("#       u         v\n")
fprintf("0    %.4f    %.4f\n",u0,v0)
for i = 1:steps
    x0=[u0;v0];
    F=[f1,f2];
    DF=jacobian([f1, f2], [u,v]);

    Df11=DF(1,1);
    Df12=DF(1,2);
    Df21=DF(2,1);
    Df22=DF(2,2);

    f10=subs(f1,[u,v],[u0,v0]);

    f20=subs(f2,[u,v],[u0,v0]);

    Df110=subs(Df11,[u,v],[u0,v0]);

    Df120=subs(Df12,[u,v],[u0,v0]);

    Df210=subs(Df21,[u,v],[u0,v0]);

    Df220=subs(Df22,[u,v],[u0,v0]);

    DF0=[Df110,Df120;Df210,Df220];
    F0=[f10;f20];
    F0_minus=-1*F0;
    system=rref([DF0 F0_minus]);
    s=system(:,end);

    x1=x0+s;

    u1=x1(1,1);
    v1=x1(2,1);

    u0=double(u1);
    v0=double(v1);
    
    if i<10
    fprintf("%d    %.4f    %.4f\n",i,u0,v0)
       
    else
    fprintf("%d   %.4f    %.4f\n",i,u0,v0)
    end
end
