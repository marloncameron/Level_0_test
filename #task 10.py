#task 10

def compare_words(a ,b):
    s1 = set(a.lower())
    s2 = set(b.lower())
    lst = s1 & s2
    print('Common letters:', lst)


compare_words("housE", "computers")


