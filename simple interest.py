p=eval(input("enter the value of principal ammount:-"))
r=eval(input("enter the annual rate of interest:-"))
t=eval(input("enter the time duration:-"))
si=p*r*t/100
print("simple interest:-%f" %(si))
ammount=p+si;
print("ammount payable:-",ammount)
