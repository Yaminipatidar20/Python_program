classbe=dict()
n=int(input("Enter total number of section in BE class:-"))
i=1
while i<=n:
    a=input("Enter section:-")
    b=input("Enter stream name:-")
    classbe[a]=b
    i=i+1
print("class\t", "section\t","stream name\t")
for i in classbe:
    print("BE\t",i,classbe[i])
