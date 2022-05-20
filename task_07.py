def fahrenheit_to_celcuis(temperature):
    celcuis = (temperature-32)*5/9
    return celcuis


def celcuis_to_fahrenheit(temperature):
    fahrenheit = (temperature*1.8) + 32
    return fahrenheit


print(f"the temperature is: {fahrenheit_to_celcuis(100)} Degrees ")

print(f"the temperature is: {celcuis_to_fahrenheit(100)} Fahrenheit")





    
