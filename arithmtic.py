x=eval(input("enter first num:-"))
op=input("enter operator symbole (ex. +,-,*,/,//,**):-")
y=eval(input("enter second number:-"))
if op=='+':
    print("sum of two numbers:-",x+y)
elif op=='-':
    print("sub of two numbers:-",x-y)
elif op=='*':
    print("multi of two numbers:-",x*y)
elif op=='/':
    print("div of two numbers:-",x/y)
elif op=='//':
    print("integer of two numbers:-",x//y)
elif op=='**':
    print("x pow y:-",x**y)
else:
    print("error:invalid operator");
