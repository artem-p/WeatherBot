# import telegram
import time

import requests
import telepot

from src import secrets, forecast
from src.wunderground import weather

AVAILABLE_COMMANDS = """Доступные команды:

/ping: pong
/weather: текущая погода
/tomorrow: прогноз на завтра"""

weather.get_current_weather()


def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    command = msg['text']
    if command == '/ping':
        bot.sendMessage(chat_id, 'pong')
    elif command == "/weather":
        cur_weather_request = requests.get('http://178.62.201.176/api/1.0/current')
        if cur_weather_request.status_code == 200:
            bot.sendMessage(chat_id, cur_weather_request.json())
        else:
            bot.sendMessage(chat_id, "Не удалось получить текущую погоду")
    elif command == "/tomorrow":
        # Прогноз на завтра
        try:
            fcst = forecast.get_tomorrow_forecast()
            bot.sendMessage(chat_id, fcst.to_text())
        except Exception as e:
            print("Не удалось получить прогноз на завтра")
            print(e)
            bot.sendMessage(chat_id, "Не удалось получить прогноз на завтра. Попробуйте позже")

    else:
        bot.sendMessage(chat_id, AVAILABLE_COMMANDS)

#   bot.sendMessage(chat_id, msg['text'])

bot = telepot.Bot(token=secrets.get_secret("TELEGRAM_TOKEN"))

bot.message_loop(handle_message)
print('Listening...')

while True:
    time.sleep(10)


# last_update_id = bot.getUpdates()[-1].update_id  # Get lastest update

# updates = bot.getUpdates(offset=last_update_id, timeout=10)
# update = updates[0]
# text = update.message.text
# chat_id = update.message.chat_id
# update_id = update.update_id

# text
# chat_id
# update_id

# if text:
#   bot.sendMessage(chat_id=chat_id, text="От бота: " + text)
#   last_update_id = update_id + 1
# while True:
#   for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
#     text = update.message.text
#     chat_id = update.message.chat_id
#     update_id = update.update_id


# message_sent = bot.getUpdates()
# message_sent
# message_sent[1].message.text
