#task 05

#the funtion below is herons formula 

def areaoftriangle(a,b,c):
    perimeter = a + b + c 
    s = perimeter / 2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

a1 = int(3)
b1 = int(5)
c1 = int(6)

area = areaoftriangle(a1,b1,c1)

print ("the area of the triangle is:" + str(area))
