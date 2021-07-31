try:
    a=eval(input("Enter the value of a:-"))
    b=eval(input("Enter the value of b:-"))
    r=a/b
    print("Result:-",r);
except(ArithmeticError,IOError,NameError):
    print("Arithmetic Exception")
else:
    print("Successfully Done")