request_type_cur_weather = 1


def get_request_info_by_message(message):
    """
    Parse chat message. Make url to weather service from it.
    :param message:
    :return: type: request type constant, url: str
    """
    cur_weather_default = 'http://178.62.201.176/api/1.0/current'

    return request_type_cur_weather, cur_weather_default
