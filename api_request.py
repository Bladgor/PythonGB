from datetime import datetime, timedelta
import json
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
            header=headers,
            url=url,
            params=params,
        )
    else:
        return post_request(
            headers=headers,
            url=url,
            params=params,
        )


def get_request(header, url, params):
    try:
        response = get(
            url=url,
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


def post_request(headers, url, params):
    try:
        response = post(
            url=url,
            headers=headers,
            json=params
        )
        print(response)
        if response.status_code == requests.codes.ok:
            print('Connect: ok')
            return response.json()
    except (requests.exceptions.InvalidHeader,
            requests.exceptions.ConnectionError,
            requests.exceptions.InvalidURL) as ex:
        print(f'Error: {ex}')


def search_id_location(city):
    method = "locations/v3/search"
    request_type = 'GET'
    querystring = {"q": f"{city}", "locale": "ru_RU"}
    get_headers = {"X-RapidAPI-Key": RAPID_API_KEY,
                   "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
                   }
    my_response = api_request(method_endswith=method,
                              params=querystring,
                              method_type=request_type,
                              headers=get_headers)['sr']

    dict_city = dict()
    for destination in my_response:
        if destination['type'] != 'HOTEL':
            dict_city[destination['regionNames']['fullName']] = destination['gaiaId']

    return dict_city


def search_hotels(city_id, check_in=None, check_out=None, adults=1, children=None, to_the_center=None):
    if check_in is None and check_out is None:
        check_in = datetime.now() + timedelta(days=1)
        check_out = check_in + timedelta(days=1)
    method = "properties/v2/list"
    request_type = 'POST'
    querystring = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {"regionId": city_id},
        "checkInDate": {
            "day": check_in.day,
            "month": check_in.month,
            "year": check_in.year
        },
        "checkOutDate": {
            "day": check_out.day,
            "month": check_out.month,
            "year": check_out.year
        },
        "rooms": [
            {
                "adults": 1,
                "children": []
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": 20,
        "sort": "PRICE_LOW_TO_HIGH",
        "filters": {"price": {
            "max": 100,
            "min": 1
        }}
    }
    # querystring = json.dumps(querystring)

    post_headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    my_response = api_request(method_endswith=method,
                              params=querystring,
                              method_type=request_type,
                              headers=post_headers)

    hotels_dict = dict()
    hotels_list = my_response['data']['propertySearch']['properties']
    # hotels_list = []

    for elem in hotels_list:
        hotels_dict[elem['name']] = {
            'hotel_id': elem['id'],
            'price': elem['price']['lead']['amount'],
            # 'price': elem['price']['strikeOut']['amount'],
            'to_the_center': elem['destinationInfo']['distanceFromDestination']['value'],
            'main_photo': elem['propertyImage']['image']['url']
        }

    hotels_sorted = sorted(hotels_dict.items(), key=lambda item: float(item[1]['price']))

    return hotels_sorted
