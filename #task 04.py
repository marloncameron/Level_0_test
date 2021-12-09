#task 04

def even_or_odd(number):
    if number%2 == 0:
        numbertype ="even"
    else:
        numbertype ="odd"
    return numbertype

number = int (3)
numbertype = even_or_odd(number)
print( numbertype )