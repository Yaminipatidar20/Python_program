try:
    a=eval(input("Enter the value of a:-"))
    b=eval(input("Enter the value of b:-"))
    r=a/b
    print("Result:-",t);
except ArithmeticError as e:
    print(e)
except NameError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("Successfully Done")
finally:
    print("This is finally block")