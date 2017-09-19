from weather import Weather


def get_weather(city='St. Petersburg'):
    weather = Weather()
    location = weather.lookup_by_location(city)
    condition = location.condition()
    condition.pop('date')
    return condition


if __name__ == '__main__':
    cur_weather = get_weather()
    assert 'temp' in cur_weather
    assert 'code' in cur_weather
    assert 'text' in cur_weather
