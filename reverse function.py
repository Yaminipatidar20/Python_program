def reverse_num():
    num=int(input("Enter any number:-"))
    temp=num
    rev=0

    while temp!=0:
        rem=temp%10;
        rev=(rev*10)+rem
        temp=temp//10
    return rev;
print("Reverse Number is",reverse_num())    
