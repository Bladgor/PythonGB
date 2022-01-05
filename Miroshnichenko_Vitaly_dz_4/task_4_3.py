from bs4 import BeautifulSoup
import requests
import re
from datetime import date
from decimal import Decimal


def currency_rates(currency):
    currency = currency.upper()
    date_req = ''
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    all_currency = soup.findAll('valute')
    request_date = soup.findAll('valcurs')

    for element in str(request_date).split():
        if element.startswith('date'):
            date_req = re.findall(r'\d+', str(element))
            date_req = date(*(map(int, date_req[::-1])))
            break

    for elem in all_currency:
        if currency in str(elem):
            value = elem.findAll('value')
            value = re.findall(r'\d+', str(value))
            num = f'{value[0]}.{value[1]}'
            return f'{date_req} курс {currency} по отношению к рублю {Decimal(num).quantize(Decimal("1.00"))}'


print(currency_rates('usd'))
print(currency_rates('eUr'))
print(currency_rates('USD1'))
