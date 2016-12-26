import src.weather_connect
from src import chat


def test_tokenize():
    message = 'message'
    tokens = chat.tokenize(message)
    assert tokens == ['message']

    message = 'message, with punctuation!'
    tokens = chat.tokenize(message)
    assert tokens == ['message', 'with', 'punctuation']

    message = "Погода в Питере"
    tokens = chat.tokenize(message)
    assert tokens == ['погода', 'питере']

    message = "Погода в Москве"
    tokens = chat.tokenize(message)
    assert tokens == ['погода', 'москве']

    message = "Сейчас Санкт-Петербург"
    tokens = chat.tokenize(message)
    assert tokens == ['сейчас', 'санкт-петербург']


def test_is_keyword():
    word = "погода"
    assert chat.is_keyword(word) == True

    word = "bad_keyword"
    assert chat.is_keyword(word) == False


def test_get_request_type_and_location():
    message = "Погода"
    assert chat.get_request_type_and_location(message) == (
    src.weather_connect.request_type_cur_weather, chat.default_location)

    message = "Питер"
    assert chat.get_request_type_and_location(message) == (src.weather_connect.request_type_cur_weather, "питер")

    message = "Погода в Питере"
    assert chat.get_request_type_and_location(message) == (src.weather_connect.request_type_cur_weather, "питер")


def test_get_request_type_by_keywords():
    keywords = ["погода", "питер"]
    assert chat.get_request_type_by_keywords(keywords) == src.weather_connect.request_type_cur_weather

    keywords = ["сейчас"]
    assert chat.get_request_type_by_keywords(keywords) == src.weather_connect.request_type_cur_weather

    keywords = ["питер", "завтра", "погода"]
    assert chat.get_request_type_by_keywords(keywords) == src.weather_connect.request_type_tomorrow


def test_is_locative():
    token = "питер"
    assert chat.is_locative(token) is False

    token = "питере"
    assert chat.is_locative(token) is True

    token = "москва"
    assert chat.is_locative(token) is False

    token = "байкале"
    assert chat.is_locative(token) is True


def test_get_location():
    tokens = ["нет", "формы", "loc2"]
    assert chat.get_location(tokens) == "нет"

    tokens = ["есть", "форма", "loc2", "питере"]
    assert chat.get_location(tokens) == "питер"

    tokens = ["питере"]
    assert chat.get_location(tokens) == "питер"

    tokens = ["петербург"]
    assert chat.get_location(tokens) == "петербург"
