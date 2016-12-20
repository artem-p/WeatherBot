import nltk
import string
from nltk.corpus import stopwords
import pymorphy2

request_type_none = 0
request_type_cur_weather = 1
request_type_tomorrow = 2
request_type_default = request_type_cur_weather

default_location = "Санкт-Петербург"

g_morph = pymorphy2.MorphAnalyzer()
g_keywords = ["погода", "сейчас", "завтра", "утром", "днем", "вечером"]


def get_response(message):
    """
    response to message
    :param message:
    :return: str
    """
    request_type, url = get_request_info_by_message(message)

    if request_type is not request_type_none:
        # todo owm request
        pass
    else:
        # todo return cannot parse request
        pass


def get_request_info_by_message(message):
    """
    Parse chat message. Make url to weather service from it.
    :param message:

    :return: type: request type constant, url: str
    """
    request_type = request_type_none
    request_url = ""

    request_type, location = get_request_type_and_location(message)

    if request_type is not request_type_none:
        # todo make request url from type and location
        pass

    return request_type, request_url


def get_request_type_and_location(message):
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
            request_type = get_request_type_by_keywords(token)
            location = default_location
        else:
            # assume that it is location, request type current by default
            request_type = request_type_default
            location = token
    else:
        keywords = list(filter(is_keyword, tokens))
        without_keywords = list(filter(not is_keyword, tokens))

        if len(keywords) > 0:
            request_type = get_request_type_by_keywords(keywords)
        else:
            request_type = request_type_default

    # todo get location
    return request_type, location

    # if len(tokens) > 1:
    #     # todo Выделяем ключевые слова отдельно. В остатке проверяем loc2, берем его, если есть. Если нет, просто остаток.
    #     keywords = filter(is_keyword, tokens)
    #     without_keywords = ...
    #     location = ...
    #
    # else:
    #     pass


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
