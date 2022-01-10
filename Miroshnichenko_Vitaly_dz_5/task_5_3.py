tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Виктор', 'Станислав'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

name_klass_gen = ((tutors[i], klasses[i]) if len(klasses) > i else (tutors[i], None) for i in range(len(tutors)))

print(name_klass_gen)

for elem in name_klass_gen:
    print(elem)
