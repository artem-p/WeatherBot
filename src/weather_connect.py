import requests


weather_service_base = 'http://178.62.201.176/api/1.0/'


def get_request_url(request_type):
    """
    getting request url based on type and location
    :param request_type:
    :param location:
    :return: str
    """
    current_url = weather_service_base + "current/"
    default_url = current_url

    if request_type == request_type_cur_weather:
        url = current_url
    else:
        url = ""

    return url

request_type_none = 0
request_type_cur_weather = 1
request_type_tomorrow = 2
request_type_default = request_type_cur_weather
