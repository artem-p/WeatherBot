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
    assert tokens == ['погода', 'питер']

    message = "Погода в Москве"
    tokens = chat.tokenize(message)
    assert tokens == ['погода', 'москва']

    message = "Сейчас Санкт-Петербург"
    tokens = chat.tokenize(message)
    assert tokens == ['сейчас', 'санкт-петербург']


def test_is_keyword():
    word = "погода"
    assert chat.is_keyword(word) == True

    word = "bad_keyword"
    assert chat.is_keyword(word) == False


def test_get_request_type_by_keyword():
    keyword = "погода"
    assert chat.get_request_type_by_keyword(keyword) == chat.request_type_cur_weather

    keyword = "сейчас"
    assert chat.get_request_type_by_keyword(keyword) == chat.request_type_cur_weather


def test_get_request_type_and_location():
    pass
