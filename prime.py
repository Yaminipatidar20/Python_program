num=int(input("enter any number:-"))
flage=True
i=2
while i<num:
    if num%i==0:
        flage=False
        break
    i=i+1
if flage==True:
    print("given num",num,"is prime number")
else:
    print("given num",num,"is not prime number")
