a=[]
n=eval(input("enter the total item no of the list:-"))
i=1
while i<=n:
    element=eval(input("enter the element:-"))
    a.append(element)
    i=i+1
avg=sum (a)/n
print("average of list:-",avg)
