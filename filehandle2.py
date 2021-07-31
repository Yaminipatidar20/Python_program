fout=open("Student1.txt","w")
list1=[]
for i in range(5):
    name=input("Enter Name of Student:-")
    list1.append(name+'/n')
fout.writelines(list1)
fout.close()