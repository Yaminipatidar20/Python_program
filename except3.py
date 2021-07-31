try:
    a=int(input("Enter value of a:-"))
    b=int(input("Enter value of b:-"))
    c=a/b
    print("a/b=%d"%c)
except Exception as e:
    print("Can't Divide by Zero")
    print(e)
else:
    print("Hi I am ELse Block")

