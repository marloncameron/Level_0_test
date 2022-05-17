def area_of_a_triangle(side_1, side_2, side_3):
    perimeter = side_1 + side_2 + side_3
    semi_perimeter = perimeter / 2
    area = (semi_perimeter*(semi_perimeter-side_1)*(semi_perimeter-side_2)*(semi_perimeter-side_3))**0.5
    return area

print(f" Area of triangle {area_of_a_triangle(3,5,6)}")
