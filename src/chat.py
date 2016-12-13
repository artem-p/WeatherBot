request_type_cur_weather = 1
import nltk
import string
from nltk.corpus import stopwords

def get_request_info_by_message(message):
    """
    Parse chat message. Make url to weather service from it.
    :param message:

    :return: type: request type constant, url: str
    """
    cur_weather_default = 'http://178.62.201.176/api/1.0/current'

    # by default assume that all message is location
    cur_weather_location = cur_weather_default + "?location=" + message

    return request_type_cur_weather, cur_weather_location


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

    return tokens
