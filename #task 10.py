#task 10

def compare (a ,b):
    s1 = set(a)
    s2 = set(b)
    lst = list(s1 & s2)
    print(lst)


compare("house" , "computers")


