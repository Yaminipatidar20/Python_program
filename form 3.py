x=eval(input("enter the value of x:-"))
y=eval(input("enter the value of y:-"))
z=eval(input("enter the value of z:-"))
max=None
if(x>y):
    if(x>z):
        max=x
    else:
            max=z
else:
    if(y>z):
        max=y
    else:
            max=z
print("maximum number is",max)            
            
            
        
