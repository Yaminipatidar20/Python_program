file=open("image.jpg","rb")
file1=open("newpick.jpg","wb")
for i in file:
    file1.write(i)
file.close()
file1.close()