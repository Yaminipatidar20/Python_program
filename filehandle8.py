import pickle
file1=open("dict.log","wb")
d={12:"Yamini",13:"Yash"}
pickle.dump(d,file1)
file1.close()
file2=open("dict.log","rb")
d1=pickle.load(file2)
print(d1)