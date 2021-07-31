count=int(input("How Many Students are there in the class:-"))
fileout=open("Marks.det","w")
for i in range(count):                                #write mode
    print("Enter Details for Student",(i+1),"Below")
    rollno=input("Roll No.:-")
    name=input("Name:-")
    marks=eval(input("Enter Marks:-"))
    age=input("Age:-")
    gender=input("Enter Gender:-")
    rec=rollno+","+name+","+str(marks)+","+age+","+gender+'\n'
    fileout.write(rec)
fileout.close()
fin=open("Marks.det","r")                          #read mode
while str:
    str=fin.readline()
    print(str)
fin.close()