def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("list inside function:-",list1)
list1=[10,30,40,50]
change_list(list1)
print("list outside function:-",list1);
