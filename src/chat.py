import string
import requests
import nltk
import pymorphy2
from nltk.corpus import stopwords

from src.weather_connect import request_type_none, request_type_cur_weather, request_type_tomorrow, request_type_default
import src.weather_connect as weather_connect


default_location = "Санкт-Петербург"

g_morph = pymorphy2.MorphAnalyzer()
g_keywords = ["погода", "сейчас", "завтра", "утром", "днем", "вечером"]


def get_response(message):
    """
    response to message
    :param message:
    :return: str
    """
    request_type, url, location = get_request_info_by_message(message)

    if request_type is not request_type_none:
        weather_request = requests.get(url, {'location': location})

        if weather_request.status_code == 200:
            return weather_request.json()
        else:
            return "Не удалось получить данные"
    else:
        return "Не удалось распознать запрос"


def get_request_info_by_message(message):
    """
    Parse chat message. Make url to weather service from it.
    :param message:

    :return: type: request type constant, url: str
    """

    request_type, location = get_request_type_and_location(message)
    request_url = weather_connect.get_request_url(request_type)

    return request_type, request_url, location


def get_request_type_and_location(message):
    """
    parse message. Get requested location and request type (current, tomorrow, etc)
    :param message:
    :return: int: request_type, str: location
    """
    tokens = tokenize(message)
    location = default_location
    request_type = request_type_none

    if len(tokens) > 0:
        if len(tokens) == 1:
            token = tokens[0]
            if is_keyword(token):
                # we have keyword, location will be default
                request_type = get_request_type_by_keywords(token)
                location = default_location
            else:
                # assume that it is location, request type current by default
                request_type = request_type_default
                location = token
        else:
            keywords = list(filter(is_keyword, tokens))
            without_keywords = list(filter(lambda token: not is_keyword(token), tokens))

            if len(keywords) > 0:
                request_type = get_request_type_by_keywords(keywords)
            else:
                request_type = request_type_default

            location = get_location(without_keywords)

    return request_type, location


def get_location(tokens_without_keywords):
    """
    getting location. find token in locative form. If no, get first
    :param tokens_without_keywords:
    :return:
    """
    location = default_location

    if len(tokens_without_keywords) > 0:
        locative_tokens = list(filter(is_locative, tokens_without_keywords))
        if len(locative_tokens) > 0:
            location = locative_tokens[0]
            location = get_normal_form(location)
        else:
            location = tokens_without_keywords[0]

    return location


def is_locative(token):
    """
    check if token is in locative form (loct или loc2)
    :param token:
    :return:
    """
    parse = g_morph.parse(token)
    first_parse = parse[0]
    tag = first_parse.tag

    if 'loct' in tag or 'loc2' in tag:
        return True
    else:
        return False


def get_request_type_by_keywords(keywords):
    #   getting request type by few keywords
    request_type = request_type_none
    if "погода" or "сейчас" in keywords:
        request_type = request_type_cur_weather

    if "завтра" in keywords:
        request_type = request_type_tomorrow

    return request_type


def is_keyword(word):
    """
    check if word is keyword
    :param word:
    :return:
    """
    return True if word in g_keywords else False


def tokenize(message):
    """
    tokenize message. Delete punctuation, etc. Transform to lower case
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

    tokens = [token.lower() for token in tokens]

    return tokens


def get_normal_form(word):
    normal_form_word = word
    morphs = g_morph.parse(word)

    if len(morphs) > 0:
        morph = morphs[0]
        normal_form_word = morph.normal_form

    return normal_form_word
