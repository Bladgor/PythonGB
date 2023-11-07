import requests
from requests import get, post
from pprint import pprint
from config_data.config import RAPID_API_KEY


def api_request(method_endswith,  # Меняется в зависимости от запроса. locations/v3/search либо properties/v2/list
                params,  # Параметры, если locations/v3/search, то {'q': 'Рига', 'locale': 'ru_RU'}
                method_type,  # Метод\тип запроса GET\POST
                headers
                ):
    url = f"https://hotels4.p.rapidapi.com/{method_endswith}"

    # В зависимости от типа запроса вызываем соответствующую функцию
    if method_type == 'GET':
        return get_request(
            headers,
            url=url,
            params=params,
        )
    else:
        return post_request(
            headers,
            url=url,
            params=params,
        )


def get_request(header, url, params):
    try:
        response = get(
            url,
            headers=header,
            params=params,
            timeout=15
        )
        if response.status_code == requests.codes.ok:
            print('ok')
            return response.json()
    except (requests.exceptions.InvalidHeader,
            requests.exceptions.ConnectionError,
            requests.exceptions.InvalidURL) as ex:
        print(f'Error: {ex}')


def post_request(header, url, params):
    print('post')


method = "locations/v2/search"
querystring = {"query": "London", "locale": "ru_RU", "currency": "RUB"}
get_headers = {"X-RapidAPI-Key": RAPID_API_KEY,
               "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
               }
post_headers = {"content-type": "application/json",
                "X-RapidAPI-Key": RAPID_API_KEY,
                "X-RapidAPI-Host": "hotels4.p.rapidapi.com"}
request_type = 'GET'

my_response = api_request(method, querystring, request_type, get_headers)
print(my_response)
pprint(my_response)
