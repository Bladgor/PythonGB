import datetime

my_dict = {1: 'qw', 2: 'er', 3: 'ty'}

date_today = '22.11.2024'
date_2 = '25.11.2023'

date_today = list(map(int, date_today.split('.')))
date_2 = list(map(int, date_2.split('.')))

date_min = datetime.datetime(date_today[2], date_today[1], date_today[0])
date_max = datetime.datetime(date_2[2], date_2[1], date_2[0])

print(date_min < date_max)
