def maximumvalue(*list1):
    maximum_num = list1[0]
    for num in list1:
        if num > maximum_num :
             maximum_num = num
    return maximum_num

print(maximumvalue(1, 22 ,3,  2))
