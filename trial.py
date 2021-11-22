class student:
    #num_of_student=0
    num=dict()
    sub=0
    def __init__(self):
        n=eval(input("Enter total subject:-"))
        i=1
        while i<=n:
            bda=eval(input("Enter BDA marks:-"))
            dsa=eval(input("Enter DSA marks:-"))
            pythn=eval(input("Enter PYTHON marks:-"))
            sem=eval(input("Enter SEM marks:-"))
            sub=(bda+dsa+pythn+sem)
            sum=sub/n
            i=i+1
#sprint("Total subject:-",n)
print("Total percantage:-",sum)

















            
