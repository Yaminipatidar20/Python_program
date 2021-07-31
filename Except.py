try:
    a=eval(input("Enter the value of a:-"))
    b=eval(input("Enter the value of b:-"))
    r=a/b
    print("Result is:-",r)
except Exception:
    print("Can't divide by zero")
    print(Exception)
print("This is Example of Exception Handling")