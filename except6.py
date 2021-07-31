try:
    fileptr=open("file2.txt","w")
    fileptr.write("Hi i am good")
except:
    print("Error")
finally:
    fileptr.close();
    print("File Close")