

def conversion(minutes):
    min_value = minutes % 60
    hour_value = minutes // 60

    #if hour is 0 minues is 0 or mre than 1 what should be printed

    if hour_value == 0 and min_value == 0:
        print(hour_value, "hours", min_value, "minutes")

    elif hour_value == 1 and min_value == 1:
        print(hour_value, "hour", min_value, "minute")

    elif hour_value > 1 and min_value > 1:
        print(hour_value, "hours", min_value, "minutes")

    else:
        print(hour_value, "hour", "," , min_value, "minutes")


conversion(min)
