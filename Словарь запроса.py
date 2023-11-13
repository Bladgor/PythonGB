from pprint import pprint

dict_request = {'q': 'London',
                'rc': 'OK',
                'rid': 'ad2e6429acc84f8f81afcca7ccf802bc',
                'sr': [{'@type': 'gaiaRegionResult',
                        'coordinates': {'lat': '51.50746', 'long': '-0.127673'},
                        'essId': {'sourceId': '2114', 'sourceName': 'GAI'},
                        'gaiaId': '2114',
                        'hierarchyInfo': {'airport': {'airportCode': 'LON',
                                                      'airportId': '6139104',
                                                      'metrocode': 'LON',
                                                      'multicity': '178279'},
                                          'country': {'isoCode2': 'GB',
                                                      'isoCode3': 'GBR',
                                                      'name': 'Великобритания'}},
                        'index': '0',
                        'regionNames': {'displayName': 'Лондон, Англия, Великобритания',
                                        'fullName': 'Лондон, Англия, Великобритания',
                                        'lastSearchName': 'Лондон',
                                        'primaryDisplayName': 'Лондон',
                                        'secondaryDisplayName': 'Англия, Великобритания',
                                        'shortName': 'Лондон'},
                        'type': 'CITY'},
                       {'@type': 'gaiaRegionResult',
                        'coordinates': {'lat': '51.515618', 'long': '-0.091998'},
                        'essId': {'sourceId': '800056', 'sourceName': 'GAI'},
                        'gaiaId': '800056',
                        'hierarchyInfo': {'airport': {'airportCode': 'LON',
                                                      'airportId': '6139104',
                                                      'metrocode': 'LON',
                                                      'multicity': '178279'},
                                          'country': {'isoCode2': 'GB',
                                                      'isoCode3': 'GBR',
                                                      'name': 'Великобритания'},
                                          'relation': ['alias']},
                        'index': '1',
                        'regionNames': {'displayName': 'Лондонский Сити ("City Of London"), '
                                                       'Лондон, Англия, Великобритания',
                                        'fullName': 'Лондонский Сити, Лондон, Англия, '
                                                    'Великобритания',
                                        'lastSearchName': 'Лондонский Сити ("City Of London")',
                                        'primaryDisplayName': 'Лондонский Сити ("City Of '
                                                              'London")',
                                        'secondaryDisplayName': 'Лондон, Англия, '
                                                                'Великобритания',
                                        'shortName': 'Лондонский Сити'},
                        'type': 'NEIGHBORHOOD'},
                       {'@type': 'gaiaRegionResult',
                        'coordinates': {'lat': '51.508362', 'long': '-0.129026'},
                        'essId': {'sourceId': '6195474', 'sourceName': 'GAI'},
                        'gaiaId': '6195474',
                        'hierarchyInfo': {'airport': {'airportCode': 'LON',
                                                      'airportId': '6139104',
                                                      'metrocode': 'LON',
                                                      'multicity': '178279'},
                                          'country': {'isoCode2': 'GB',
                                                      'isoCode3': 'GBR',
                                                      'name': 'Великобритания'},
                                          'relation': ['alias']},
                        'index': '2',
                        'regionNames': {'displayName': 'Центральный район Лондона ("Central '
                                                       'London"), Лондон, Англия, '
                                                       'Великобритания',
                                        'fullName': 'Центральный район Лондона, Лондон, '
                                                    'Англия, Великобритания',
                                        'lastSearchName': 'Центральный район Лондона '
                                                          '("Central London")',
                                        'primaryDisplayName': 'Центральный район Лондона '
                                                              '("Central London")',
                                        'secondaryDisplayName': 'Лондон, Англия, '
                                                                'Великобритания',
                                        'shortName': 'Центральный район Лондона'},
                        'type': 'NEIGHBORHOOD'},
                       {'@type': 'gaiaRegionResult',
                        'coordinates': {'lat': '51.470878', 'long': '-0.449753'},
                        'essId': {'sourceId': '5392460', 'sourceName': 'GAI'},
                        'gaiaId': '5392460',
                        'hierarchyInfo': {'airport': {'airportCode': 'LHR',
                                                      'airportId': '5392460',
                                                      'metrocode': 'LON',
                                                      'multicity': '178279'},
                                          'country': {'isoCode2': 'GB',
                                                      'isoCode3': 'GBR',
                                                      'name': 'Великобритания'}},
                        'index': '3',
                        'isMinorAirport': 'false',
                        'regionNames': {'displayName': 'Лондон (LHR - Хитроу), Великобритания',
                                        'fullName': 'Лондон, Великобритания (LHR-Хитроу)',
                                        'lastSearchName': 'Лондон (LHR - Хитроу)',
                                        'primaryDisplayName': 'Лондон (LHR - Хитроу)',
                                        'secondaryDisplayName': 'Великобритания',
                                        'shortName': 'Лондон (LHR-Хитроу)'},
                        'type': 'AIRPORT'},
                       {'@type': 'gaiaRegionResult',
                        'coordinates': {'lat': '39.886448', 'long': '-83.44825'},
                        'essId': {'sourceId': '55800', 'sourceName': 'GAI'},
                        'gaiaId': '55800',
                        'hierarchyInfo': {'airport': {'airportCode': 'CMH',
                                                      'airportId': '6139077',
                                                      'metrocode': 'CMH',
                                                      'multicity': '178251'},
                                          'country': {'isoCode2': 'US',
                                                      'isoCode3': 'USA',
                                                      'name': 'Соединенные Штаты'}},
                        'index': '4',
                        'regionNames': {'displayName': 'Лондон, Огайо, США',
                                        'fullName': 'Лондон, Огайо, США',
                                        'lastSearchName': 'Лондон',
                                        'primaryDisplayName': 'Лондон',
                                        'secondaryDisplayName': 'Огайо, США',
                                        'shortName': 'Лондон'},
                        'type': 'CITY'},
                       {'@type': 'gaiaRegionResult',
                        'coordinates': {'lat': '51.52995251445876',
                                        'long': '-0.12402339913938085'},
                        'essId': {'sourceId': '6047476', 'sourceName': 'GAI'},
                        'gaiaId': '6047476',
                        'hierarchyInfo': {'airport': {'airportCode': 'LON',
                                                      'airportId': '6139104',
                                                      'metrocode': 'LON',
                                                      'multicity': '178279'},
                                          'country': {'isoCode2': 'GB',
                                                      'isoCode3': 'GBR',
                                                      'name': 'Великобритания'}},
                        'index': '5',
                        'regionNames': {'displayName': 'Кингс-Кросс Сент-Панкрасс, Лондон, '
                                                       'Англия, Великобритания',
                                        'fullName': 'Кингс-Кросс Сент-Панкрасс, Лондон, '
                                                    'Англия, Великобритания',
                                        'lastSearchName': 'Кингс-Кросс Сент-Панкрасс',
                                        'primaryDisplayName': 'Кингс-Кросс Сент-Панкрасс',
                                        'secondaryDisplayName': 'Лондон, Англия, '
                                                                'Великобритания',
                                        'shortName': 'Кингс-Кросс Сент-Панкрасс'},
                        'type': 'NEIGHBORHOOD'},
                       {'@type': 'gaiaRegionResult',
                        'coordinates': {'lat': '42.98971141621233',
                                        'long': '-81.24414965398488'},
                        'essId': {'sourceId': '6358345', 'sourceName': 'GAI'},
                        'gaiaId': '6358345',
                        'hierarchyInfo': {'airport': {'airportCode': 'YXU',
                                                      'airportId': '5593177',
                                                      'multicity': '4127'},
                                          'country': {'isoCode2': 'CA',
                                                      'isoCode3': 'CAN',
                                                      'name': 'Канада'}},
                        'index': '6',
                        'regionNames': {'displayName': 'Центр Лондона, Лондон, Онтарио, '
                                                       'Канада',
                                        'fullName': 'Центр Лондона, Лондон, Онтарио, Канада',
                                        'lastSearchName': 'Центр Лондона',
                                        'primaryDisplayName': 'Центр Лондона',
                                        'secondaryDisplayName': 'Лондон, Онтарио, Канада',
                                        'shortName': 'Центр Лондона'},
                        'type': 'NEIGHBORHOOD'},
                       {'@type': 'gaiaRegionResult',
                        'coordinates': {'lat': '51.878796', 'long': '-0.376453'},
                        'essId': {'sourceId': '5133388', 'sourceName': 'GAI'},
                        'gaiaId': '5133388',
                        'hierarchyInfo': {'airport': {'airportCode': 'LTN',
                                                      'airportId': '5133388',
                                                      'metrocode': 'LON',
                                                      'multicity': '178279'},
                                          'country': {'isoCode2': 'GB',
                                                      'isoCode3': 'GBR',
                                                      'name': 'Великобритания'}},
                        'index': '7',
                        'isMinorAirport': 'false',
                        'regionNames': {'displayName': 'Лондон (LTN - Лютон), Великобритания',
                                        'fullName': 'Лондон, Великобритания (LTN-Лютон)',
                                        'lastSearchName': 'Лондон (LTN - Лютон)',
                                        'primaryDisplayName': 'Лондон (LTN - Лютон)',
                                        'secondaryDisplayName': 'Великобритания',
                                        'shortName': 'Лондон (LTN-Лютон)'},
                        'type': 'AIRPORT'},
                       {'@type': 'gaiaRegionResult',
                        'coordinates': {'lat': '51.515972', 'long': '-0.174943'},
                        'essId': {'sourceId': '800049', 'sourceName': 'GAI'},
                        'gaiaId': '800049',
                        'hierarchyInfo': {'airport': {'airportCode': 'LON',
                                                      'airportId': '6139104',
                                                      'metrocode': 'LON',
                                                      'multicity': '178279'},
                                          'country': {'isoCode2': 'GB',
                                                      'isoCode3': 'GBR',
                                                      'name': 'Великобритания'}},
                        'index': '8',
                        'regionNames': {'displayName': 'Паддингтон, Лондон, Англия, '
                                                       'Великобритания',
                                        'fullName': 'Паддингтон, Лондон, Англия, '
                                                    'Великобритания',
                                        'lastSearchName': 'Паддингтон',
                                        'primaryDisplayName': 'Паддингтон',
                                        'secondaryDisplayName': 'Лондон, Англия, '
                                                                'Великобритания',
                                        'shortName': 'Паддингтон'},
                        'type': 'NEIGHBORHOOD'},
                       {'@type': 'gaiaRegionResult',
                        'coordinates': {'lat': '51.889432', 'long': '0.262148'},
                        'essId': {'sourceId': '5133395', 'sourceName': 'GAI'},
                        'gaiaId': '5133395',
                        'hierarchyInfo': {'airport': {'airportCode': 'STN',
                                                      'airportId': '5133395',
                                                      'metrocode': 'LON',
                                                      'multicity': '178279'},
                                          'country': {'isoCode2': 'GB',
                                                      'isoCode3': 'GBR',
                                                      'name': 'Великобритания'}},
                        'index': '9',
                        'isMinorAirport': 'false',
                        'regionNames': {'displayName': 'Лондон (STN - Станстед), '
                                                       'Великобритания',
                                        'fullName': 'Лондон, Великобритания (STN-Станстед)',
                                        'lastSearchName': 'Лондон (STN - Станстед)',
                                        'primaryDisplayName': 'Лондон (STN - Станстед)',
                                        'secondaryDisplayName': 'Великобритания',
                                        'shortName': 'Лондон (STN-Станстед)'},
                        'type': 'AIRPORT'}]}

print(dict_request['sr'][2]['gaiaId'])
print(dict_request['sr'][2]['regionNames']['fullName'])

city_dict = dict()
for elem in dict_request['sr']:
    city_dict[elem['regionNames']['fullName']] = elem['gaiaId']

pprint(city_dict)

# url = "https://hotels4.p.rapidapi.com/properties/v2/list"
#
# payload = {
#     "currency": "RUB",
#     "eapid": 1,
#     "locale": "ru_RU",
#     "destination": {"regionId": "2114"},
#     "checkInDate": {
#         "day": 13,
#         "month": 12,
#         "year": 2023
#     },
#     "checkOutDate": {
#         "day": 14,
#         "month": 12,
#         "year": 2023
#     },
#     "rooms": [
#         {
#             "adults": 1,
#             "children": []
#         }
#     ],
#     "resultsStartingIndex": 0,
#     "resultsSize": 20,
#     "sort": "PRICE_LOW_TO_HIGH",
#     "filters": {"price": {
#         "max": 150,
#         "min": 1
#     }}
# }
# headers = {
#     "content-type": "application/json",
#     "X-RapidAPI-Key": "9adf9fc99fmsh6713e606247ad93p17623ejsn60318b0a84af",
#     "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(response.json())
