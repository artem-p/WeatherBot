import src.weather_connect as weather_connect


def test_get_request_url():
    request_type = weather_connect.request_type_cur_weather
    assert weather_connect.get_request_url(request_type) == weather_connect.weather_service_base +'current/'

    request_type = weather_connect.request_type_none
    assert weather_connect.get_request_url(request_type) == ''
