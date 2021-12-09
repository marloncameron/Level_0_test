#task 08

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return str(hour) + ":" + str(minutes) + ":" + str(seconds)
      

n = 133
print(convert(n))