odd=[]
even=[]
n=int(input("enter the total item of list:-"))
i=1
while i<=n:
    a=int(input("enter the element:-"))
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)
    i=i+1
print("even list:-",even)
print("odd list:-",odd)
