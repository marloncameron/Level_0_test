#task 06

def maximumvalue(list1):
    max = list1[0]
    for x in list1:
        if x > max :
             max = x
    return max
    


list1 = [1,22,3,2]

print(maximumvalue(list1))
