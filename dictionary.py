scl=dict()
i=1
flag=0
n=int(input("Enter number of entries:-"))
while i<=n:
    adm=input("\nEnter Admission no. of student:-")
    nm=input("Enter Name of the student:-")
    sem=input("Enter semester of class:-")
    per=eval(input("Enter percantage of a student:-"))
    b=(nm,sem,per)
    scl[adm]=b
    i=i+1
l=scl.keys()
for i in l:
    print(" \nAdmno:-",i,":")
    z=scl[i]
    print("Name\t","class\t","per\t")
    for j in z:
        print(j,end='\t')
