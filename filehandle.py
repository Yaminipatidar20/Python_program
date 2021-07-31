fout=open("Srecord.txt","w")
print("File Object:-",fout);
for i in range(5):
    name=input("Enter Name of Student:-")
    fout.write(name)
    fout.write("\n")
fout.close()