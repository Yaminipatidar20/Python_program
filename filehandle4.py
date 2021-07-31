fin=open("Srecord.txt","r")
str=" "                             #read mode
while str:
    str=fin.readline()
    print(str)
fin.close()