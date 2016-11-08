# coding: utf-8
import tweepy
import forecast
import send_email
import secrets

def get_api():
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  return api


##################################################################################################


consumer_key = secrets.get_secret('RAINBOT_CONSUMER_KEY')
consumer_secret = secrets.get_secret('RAINBOT_CONSUMER_SECRET')
access_token = secrets.get_secret('RAINBOT_ACCESS_TOKEN')
access_token_secret = secrets.get_secret('RAINBOT_ACCESS_TOKEN_SECRET')

# Получаем апи
try:
  api = get_api()
except Exception as e:
  print("Не удалось подключиться к апи твиттера")
  print(e)


# Прогноз на завтра с твитом
try:
  fcst = forecast.get_tomorrow_forecast()
except Exception as e:
  print("Не удалось получить прогноз на завтра")
  print(e)

try:
  api.update_status(fcst.to_text())
  print("Твит отправлен")
except Exception as e:
  print("Твит не отправлен")
  print(e)

# Будет ли завтра дождь или снег
rain_or_snow = fcst.is_rain_snow_conditions()
rain_or_snow

if rain_or_snow:
  # если будет, отправляем письмо
  try:
    send_email.send("artempugachev1@gmail.com", fcst.to_text())
  except Exception as e:
    print("Не удалось отправить письмо")
    print(e)
else:
  print("Дождь не ожидается, письмо не отправлялось")
