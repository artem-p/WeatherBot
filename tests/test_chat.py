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
