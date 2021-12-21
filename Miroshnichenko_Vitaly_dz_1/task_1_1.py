duration_list = [53, 153, 4153, 400153]

for duration in duration_list:
    if duration < 60:
        print(duration, 'сек')
    elif duration < 3600:
        minutes = duration // 60
        duration %= 60
        print(minutes, 'мин', duration, 'сек')
    elif duration < 86400:
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        duration %= 60
        print(hours, 'час', minutes, 'мин', duration, 'сек')
    else:
        days = duration // 86400
        hours = (duration % 86400) // 3600
        minutes = (duration % 3600) // 60
        duration %= 60
        print(days, 'дн', hours, 'час', minutes, 'мин', duration, 'сек')
