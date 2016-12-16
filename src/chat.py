request_type_cur_weather = 1
import nltk
import string
from nltk.corpus import stopwords
import pymorphy2
g_morph = pymorphy2.MorphAnalyzer()


def get_request_info_by_message(message):
    """
    Parse chat message. Make url to weather service from it.
    :param message:

    :return: type: request type constant, url: str
    """
    cur_weather_default = 'http://178.62.201.176/api/1.0/current'
    request_type = request_type_cur_weather
    request_url = cur_weather_default

    tokens = tokenize(message)

    if len(tokens) == 1:
        # assume that it is location
        request_url = cur_weather_default + "?location=" + message
        request_type = request_type_cur_weather
    if len(tokens) > 1:
        # todo Выделяем ключевые слова отдельно. В остатке проверяем loc2, берем его, если есть. Если нет, просто остаток.
        keywords = ...
        without_keywords = ...
        location = ...



        if "погода" in tokens or "сейчас" in tokens:
            request_type = request_type_cur_weather
            request_url = cur_weather_default + "?location=" + tokens[len(tokens) - 1]

    return request_type, request_url


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
