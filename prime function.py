num=eval(input("enter any number:-"))
def prime_num():
    flage=True
    i=2
    while i<num:
        if num%i==0:
            flage=False
            break;
        i=i+1
    if flage==True:
        print("Given Number",num,"is prime number")
        return True;
    else:
        print("Given Number",num,"is not prime number")
        return False;
prime_num()
        
