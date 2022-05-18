def conversion(number):
    minutes = number % 60
    hour = number // 60

    if hour == 1:
        desc_hour = " hour"
    else:
        desc_hour = " hours"
    if minutes == 1:
        desc_minutes = " minute"
    else:
        desc_minutes = " minutes"

    print(hour, desc_hour, ",", minutes, desc_minutes)


conversion(781)
