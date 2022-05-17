def conversion(minutes):
    min_value = minutes % 60
    hour_value = minutes // 60



    if hour_value == 0 and min_value == 0:
        print(hour_value, "hours", min_value, "minutes")

    elif hour_value == 0 and min_value == 1:
        print(f'{hour_value} hours , {min_value} minute')

    elif hour_value == 1 and min_value == 1:
        print(f'{hour_value}  hour, {min_value} minute')

    elif hour_value > 1 and min_value > 1:
        print(f'{hour_value} hours, {min_value} minutes')

    else:
        print(f'{hour_value} hour , {min_value} minutes')


conversion(61)
