post_name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for post_name in post_name_list:
    print('Привет,', f'{post_name.split()[-1].title()}!')
