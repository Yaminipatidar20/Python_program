def simple_intrest(p,t,r):
    return(p*t*r)/100;
p=eval(input("enter the principle ammount:-"))
t=eval(input("enter the time period:-"))
r=eval(input("enter the rate:-"))
print("simple interest:-",simple_intrest(p,t,r))
