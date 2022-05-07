#task 10

def characters(x,y):
    str1=x.lower()
    str2=y.lower()
    s=list(set(str1)&set(str2))
    print("The common letters are:")
    for i in s:
        i = ', '.join(s)
    print("Common characters: ",i)


characters("housE", "computers");


