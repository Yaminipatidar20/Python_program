num1=eval(input("enter the value of num1:-"))
num2=eval(input("enter the value of num2:-"))
num3=eval(input("enter the value of num3:-"))
if(num1>num2)and (num1>num3):
    largest=num1
elif(num2>num1)and (num2>num3):
    largest=num2
else:
    largest=num3
print("the largest number is",largest)    
