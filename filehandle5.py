fin=open("Srecord.txt","r")
fout=open("Copy.txt","w")          #write mode copy data
for i in fin:
    fout.write(i)
fin.close()
fout.close()
fin=open("Copy.txt","r")
str=fin.read()
print(str)
fin.close()