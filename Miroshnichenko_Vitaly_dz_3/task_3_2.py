

def num_translate(num, flag=False):
    if num[0].isupper():
        flag = True
    if num.lower() in TRANSLATE_DICT:
        if flag:
            return TRANSLATE_DICT[num.lower()].title()
        return TRANSLATE_DICT[num]


TRANSLATE_DICT = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

number = input('Введите число на английском: ')

print(num_translate(number))
