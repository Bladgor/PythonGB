info_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
final_text = ''

index = 0
for i, _ in enumerate(info_list):
    if info_list[index][-1].isdigit():
        if len(info_list[index]) == 1:
            info_list[index] = '0' + info_list[index]
        elif not info_list[index][-2].isdigit():
            info_list[index] = info_list[index][0] + '0' + info_list[index][1]
        info_list.insert(index, '"')
        info_list.insert(index + 2, '"')
    else:
        index = i + 1

for i, elem in enumerate(info_list):
    if elem != '"':
        if i == len(info_list) - 1:
            final_text += f'{elem}'
        elif elem[-1].isdigit() and i == len(info_list) - 2:
            final_text += f'{info_list[i - 1]}{elem}{info_list[i + 1]}'
            break
        elif elem[-1].isdigit():
            final_text += f'{info_list[i - 1]}{elem}{info_list[i + 1]} '
        else:
            final_text += f'{elem} '

print(info_list)
print(final_text)
