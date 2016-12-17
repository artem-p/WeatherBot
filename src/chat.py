import nltk
import string
from nltk.corpus import stopwords
import pymorphy2

request_type_cur_weather = 1
request_type_tomorrow = 2
default_location = "Санкт-Петербург"

g_morph = pymorphy2.MorphAnalyzer()
g_keywords = ["погода", "сейчас", "завтра", "утром", "днем", "вечером"]


def get_request_info_by_message(message):
    """
    Parse chat message. Make url to weather service from it.
    :param message:

    :return: type: request type constant, url: str
    """
    cur_weather_default = 'http://178.62.201.176/api/1.0/current'
    request_type = request_type_cur_weather
    request_url = cur_weather_default
    return request_type, request_url


def get_location_and_request_type(message):
    """
    parse message. Get requested location and request type (current, tomorrow, etc)
    :param message:
    :return: int: request_type, str: location
    """
    tokens = tokenize(message)
    location = default_location
    request_type = request_type_cur_weather

    if len(tokens) == 1:
        token = tokens[0]
        if is_keyword(token):
            # we have keyword, location will be default
            request_type = get_request_type_by_keyword(token)
            location = default_location
        else:
            # assume that it is location, request type current by default
            request_type = request_type_cur_weather
            location = token
    # todo test
    return request_type, location



    # if len(tokens) > 1:
    #     # todo Выделяем ключевые слова отдельно. В остатке проверяем loc2, берем его, если есть. Если нет, просто остаток.
    #     keywords = filter(is_keyword, tokens)
    #     without_keywords = ...
    #     location = ...
    #
    # else:
    #     pass


def is_keyword(word):
    """
    check if word is keyword
    :param word:
    :return:
    """
    return True if word in g_keywords else False


def get_request_type_by_keyword(word):
    request_type = request_type_cur_weather

    if word == "погода" or word == "сейчас":
        request_type = request_type_cur_weather

    elif word == "завтра":
        request_type = request_type_tomorrow

    return request_type


def tokenize(message):
    """
    tokenize message. Delete punctuation, etc. Transform to normal form
    :param message:
    :return: list with tokens
    """
    tokens = nltk.word_tokenize(message)

    # delete punctuations
    tokens = [token for token in tokens if (token not in string.punctuation)]

    # delete stopwords
    stop_words = stopwords.words('russian')
    stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', 'к', 'на'])
    tokens = [token for token in tokens if (token not in stop_words)]

    # to normal form
    tokens = [get_normal_form(token) for token in tokens]

    return tokens


def get_normal_form(word):
    normal_form_word = word
    morphs = g_morph.parse(word)

    if len(morphs) > 0:
        morph = morphs[0]
        normal_form_word = morph.normal_form

    return normal_form_word
