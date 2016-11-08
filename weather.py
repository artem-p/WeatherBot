# coding: utf-8
import requests
import datetime
import wind

class CurrentWeather:
  def __init__(self, current_weather_json):
    self.json_weather = current_weather_json

  def parse(self):
    # parse response result
    self.city = None
    self.time = None
    self.conditions = None
    self.temp = None
    self.feelslike = None
    self.wind_dir = None
    self.wind_kph = None

    if self.json_weather:
      current_observation = self.json_weather['current_observation']
      self.city = current_observation['display_location']['city']
      timestamp = int(current_observation['observation_epoch'])
      self.time = time_str_from_epoch(timestamp)
      self.conditions = current_observation['weather']
      self.temp = current_observation['temp_c']
      self.feelslike = int(current_observation['feelslike_c'])
      self.wind_dir = current_observation['wind_degrees']
      self.wind_kph = current_observation['wind_kph']

  def to_text(self):
    # Преобразуем в текст для вывода
    self.parse()
    self.wind = wind.Wind(self.wind_kph, self.wind_dir)
    textPart = """%s
%s
%s
Температура: %d °C
Ощущается как: %d °C
Ветер: """ %(self.city, self.time, self.conditions, self.temp, self.feelslike)
    text = textPart + self.wind.to_text()
    return text


def get_current_weather():
  query = 'http://api.wunderground.com/api/67baf1d645fb0443/conditions/lang:RU/q/Russia/St_Petersburg.json'
  # todo если сервер не отвечает
  current_weather_response = requests.get(query)
  current_weather_response.json()['current_observation']

  current_weather = CurrentWeather(current_weather_response.json())
  return current_weather.to_text()

def time_str_from_epoch(time_epoch):
    time_from_epoch = datetime.datetime.fromtimestamp(time_epoch)
    return time_from_epoch.strftime("%d.%m.%Y %H:%M")


if __name__ == "__main__":
  print(get_current_weather())

# Сделать из метки нормальное время с юнит-тестом
# "observation_epoch":"1462644000",
# "observation_time_rfc822":"Sat, 07 May 2016 21:00:00 +0300",

# Прогноз
# forecast_response = requests.get('http://api.wunderground.com/api/67baf1d645fb0443/forecast/q/Russia/St_Petersburg.json')
# forecast_response.text

# result = forecast_response.json()
# forecasts = result['forecast']
# simple_forecast = forecasts['simpleforecast']
# days_forecast = simple_forecast['forecastday']

# for day_forecast in days_forecast:
#   year = day_forecast['date']['year']
#   month = day_forecast['date']['month']

# year
