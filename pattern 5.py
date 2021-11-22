i,j,k,l=0,0,0,0;
for i in range(0,7):
    for k in range(6,i,-1):
        print(end=" ")
    for j in range(1,i):
        print(j,end=" ")
    for l in range(j,0,-1):
        print(l,end=" ")
    print()    
