#task 07

# the is to convert Fahrenheit to celcuis 
def Fahrenheit_to_celcuis(a):
    cel = (a-32)*5/9
    return cel

# this is to convert celcuis to Fahrenheit
def celcuis_to_Fahrenheit(a):
    fer = (a*1.8) + 32
    return fer

fh = 150

celsuis =Fahrenheit_to_celcuis(fh)
Fahrenheit =celcuis_to_Fahrenheit(fh)

print("the temp is:" + str(celsuis))

print("the temp is:" + str(Fahrenheit))





    