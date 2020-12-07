import requests


def get_len_weather(city):
    city_id = None
    if city == 'Москва':
        city_id = 524894
    elif city == 'Санкт-Петербург':
        city_id = 536203
    elif city == 'Лондон':
        city_id = 2643743

    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru',
                               'APPID': "480c35a44be52d44098d1e98862b3d7a"})

    data = res.json()
    return len(data['list'])



def get_weather_by_id(city):
    new_list = ''
    data = {'list': None}
    city_id = None

    if city == 'Москва':
        city_id = 524894
    elif city == 'Санкт-Петербург':
        city_id = 536203
    elif city == 'Лондон':
        city_id = 2643743


    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru',
                                   'APPID': "480c35a44be52d44098d1e98862b3d7a"})
        data = res.json()
        for i in data['list']:
            new_list += f"{i['dt_txt']}, {'{0:+3.0f}'.format(i['main']['temp'])}, {i['weather'][0]['description']}" + "\n"

    except Exception as e:
        print("Exception (forecast):", e)
        pass

    return new_list

