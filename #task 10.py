#task 10

def compare_words(a ,b):
    s1 = set(a)
    s2 = set(b)
    lst = s1 & s2
    print('Common letters:',lst)


compare_words("house" , "computers")


