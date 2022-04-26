#task 05

#the funtion below is herons formula 

def area_of_a_triangle(side_1, side_2, side_3):
    perimeter = side_1 + side_2 + side_3
    s = perimeter / 2
    area = (s*(s-side_1)*(s-side_2)*(s-side_3))**0.5
    return area

length_of_first_side = 3
length_of_second_side = 5
length_of_third_side = 6

area = area_of_a_triangle(length_of_first_side, length_of_second_side, length_of_third_side)

print ("the area of the triangle is:" + str(area))
