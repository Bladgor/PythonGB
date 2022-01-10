from random import sample, choices


def get_jokes(num, flag):
    """Making jokes from lists

    :param num: requested number of jokes
    :type num: int
    :param flag: prohibition or permission to use repetition of words
    :type flag: str

    :raise ValueError: if flag == 'нет' and num longer than the length of one of the list

    :rtype: list
    :return list of random jokes
    """
    if flag.lower() == 'нет':
        try:
            first_list = sample(NOUNS, num)
            second_list = sample(ADVERBS, num)
            third_list = sample(ADJECTIVES, num)
        except ValueError:
            return 'Невозможно вывести такое кол-во шуток.'
    else:
        first_list = choices(NOUNS, k=num)
        second_list = choices(ADVERBS, k=num)
        third_list = choices(ADJECTIVES, k=num)

    jokes_list = []
    for i in range(num):
        jokes_list.append(f'{first_list[i]} {second_list[i]} {third_list[i]}')

    return jokes_list


NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

quantity = int(input('Сколько шуток вывести? '))
repetition = input('Разрешить повторы слов в шутка? да/нет ')

print(get_jokes(num=quantity, flag=repetition))
