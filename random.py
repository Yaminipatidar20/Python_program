from random import randint
def fill_list(list,limit_num,low,high):
    for i in range(limit_num):
        list.append(randint(low,high))
min=int(input("Enter Low Limit:-"))
max=int(input("Enter High Limit:- "))
n=int(input("Number Limit:-"))
a=[]
fill_list(a,n,min,max)
print(a)
