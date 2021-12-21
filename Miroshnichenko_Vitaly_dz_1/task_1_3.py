for n in range(1, 101):
    if n % 10 == 1 and n != 11:
        print(n, 'процент')
    elif 1 < n % 10 < 5 and (n < 12 or n > 14):
        print(n, 'процента')
    else:
        print(n, 'процентов')
