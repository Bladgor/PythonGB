import requests

url = "https://hotels4.p.rapidapi.com/properties/v2/list"

payload = {
    "currency": "RUB",
    "eapid": 1,
    "locale": "ru_RU",
    # "siteId": 300000001,
    "destination": {"regionId": "2114"},
    "checkInDate": {
        "day": 10,
        "month": 12,
        "year": 2023
    },
    # "checkOutDate": {
    #     "day": 15,
    #     "month": 12,
    #     "year": 2023
    # },
    "rooms": [
        {
            "adults": 2,
            # "children": [{"age": 5}, {"age": 7}]
        }
    ],
    "resultsStartingIndex": 0,
    "resultsSize": 200,
    "sort": "PRICE_LOW_TO_HIGH",
    "filters": {"price": {
        "max": 1500,
        "min": 10
    }}
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "9adf9fc99fmsh6713e606247ad93p17623ejsn60318b0a84af",
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
