def sum_number(number_list):
    total = 0
    for element in number_list:
        number = element
        sum_of_digits = 0
        while number != 0:
            last_num = number % 10
            sum_of_digits += last_num
            number //= 10
        if sum_of_digits % 7 == 0:
            total += element

    return total


cubes_of_odd_numbers = []

for num in range(1, 1001, 2):
    cubes_of_odd_numbers.append(num ** 3)

print(sum_number(cubes_of_odd_numbers))

for index in range(len(cubes_of_odd_numbers)):
    cubes_of_odd_numbers[index] += 17

print(sum_number(cubes_of_odd_numbers))
