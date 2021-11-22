import math
def area_circle():
    r=eval(input("enter the radius of circle:-"))
    area=math.pi*r*r;
    print("area of circle:-",area)

def area_rectangle():
    l=eval(input("enter length:-"))
    b=eval(input("enter breadth:-"))
    area=l*b;
    print("area of rectangle",area)
    return area;

area_circle()
area_rectangle()


