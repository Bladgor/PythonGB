def processing(number):
    ruble = int(number // 1)
    number += 0.0000000000001
    penny = f'{int((number % 1) * 100):02}'
    return f'{ruble} руб {penny} коп'


price_list = [57.8, 46.51, 97, 49.99, 100.09, 2000, 300.09, 299.99, 3000.01, 1000]
id_1 = id(price_list)

print('Цены через запятую:\n',
      ', '.join(map(processing, price_list)), '\n')

print('Цены по возрастанию:\n',
      ', '.join(map(processing, sorted(price_list))), '\n')

id_2 = id(price_list)

if id_1 == id_2:
    print('id списка остался прежним\n')

price_in_descending_order = sorted(price_list, reverse=True)
print('Новый список цен по убыванию:\n',
      price_in_descending_order, '\n')

five_maximum_prices = sorted([sorted(price_list, reverse=True)[i] for i in range(5)], reverse=True)
print('Цены пяти самых дорогих товаров по возрастанию:\n',
      ', '.join(map(processing, five_maximum_prices)))
