import requests
from requests import get, post
from pprint import pprint
from config_data.config import RAPID_API_KEY, URL


def api_request(method_endswith,  # Меняется в зависимости от запроса. locations/v3/search либо properties/v2/list
                params,  # Параметры, если locations/v3/search, то {'q': 'Рига', 'locale': 'ru_RU'}
                method_type,  # Метод\тип запроса GET\POST
                headers
                ):
    url = f"{URL}{method_endswith}"

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
            print('Connect: ok')
            return response.json()
    except (requests.exceptions.InvalidHeader,
            requests.exceptions.ConnectionError,
            requests.exceptions.InvalidURL) as ex:
        print(f'Error: {ex}')


def post_request(header, url, params):
    print('post')


def search_id_location(city):

    method = "locations/v3/search"
    querystring = {"q": f"{city}", "locale": "ru_RU"}
    request_type = 'GET'
    get_headers = {"X-RapidAPI-Key": RAPID_API_KEY,
                   "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
                   }
    my_response = api_request(method, querystring, request_type, get_headers)['sr']

    dict_city = dict()
    for destination in my_response:
        if destination['type'] != 'HOTEL':
            dict_city[destination['regionNames']['fullName']] = destination['gaiaId']

    return dict_city


# def search_list_hotel():


# def city_founding(city):
#     ....
#     response = request_to_api(...
#     if response:
# 		    cities = list()
# 		    for dest in response...:  # Обрабатываем результат
# 						destination = ...
# 		        cities.append({'city_name': destination,
#                             ...
# 		                       }
# 		                     )
#     return cities


# post_headers = {"content-type": "application/json",
#                 "X-RapidAPI-Key": RAPID_API_KEY,
#                 "X-RapidAPI-Host": "hotels4.p.rapidapi.com"}
def api_handler(command, data):

    id_location = search_id_location(data['city'])
    my_response = api_request(method, querystring, request_type, get_headers)
