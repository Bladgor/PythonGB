import utils


def request_curr_rate(argv):
    if isinstance(argv, str):
        if argv == '':
            print('Параметр не задан.')
        else:
            print(utils.currency_rates(argv))
    else:
        program, *args = argv
        try:
            print(utils.currency_rates(args[0]))
        except IndexError:
            print('Параметр не задан.')


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        exit(request_curr_rate(sys.argv))
    else:
        param = input('Введите искомую валюту: ')
        exit(request_curr_rate(param))
