

def thesaurus_adv(*name_surname):
    name_surname_dict = dict()
    name_surname_list = list(name_surname)
    print(name_surname_list)
    for element in name_surname_list:
        first_letter_surname = element.split()[1][0]
        first_letter_name = element.split()[0][0]
        if first_letter_surname in name_surname_dict:
            if element[0] in name_surname_dict[first_letter_surname]:
                elem_app = name_surname_dict[first_letter_surname][first_letter_name]
                elem_app.append(element)
                name_surname_dict[first_letter_surname][first_letter_name] = elem_app
            else:
                name_surname_dict[first_letter_surname][first_letter_name] = [element]
        else:
            name_surname_dict[first_letter_surname] = {first_letter_name: [element]}

    name_surname_dict = sorted(name_surname_dict.items(), key=lambda x: x[0])

    return dict(name_surname_dict)


name_surname_1 = "Иван Сергеев"
name_surname_2 = "Инна Серова"
name_surname_3 = "Петр Алексеев"
name_surname_4 = "Илья Иванов"
name_surname_5 = "Анна Савельева"


print(thesaurus_adv(name_surname_1, name_surname_2, name_surname_3, name_surname_4, name_surname_5))
