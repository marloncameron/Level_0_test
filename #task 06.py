#task 06

def maximumvalue(list1):
    maximum = list1[0]
    for x in list1:
        if x > maximum :
             maximum = x
    return maximum
    


list1 = [1,22,3,2]

print(maximumvalue(list1))
