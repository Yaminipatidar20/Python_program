a=[]
n=eval(input("enter the number of total item of list:-"))
i=1
while i<=n:
    count=eval(input("enter element:-"))
    a.append(count)
    i=i+1
index=a.index(min(a))    
print("minium number=",min(a))
print("index of minimum number",index)
