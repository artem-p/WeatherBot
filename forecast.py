# coding: utf-8
import requests
import datetime

class Forecast:
  def __init__(self, forecast_response_days):
    self.timestamp = forecast_response_days['date']['epoch']
    self.weekday = forecast_response_days['date']['weekday']
    self.max_temp = forecast_response_days['high']['celsius']
    self.min_temp = forecast_response_days['low']['celsius']
    self.conditions = forecast_response_days['conditions']
    self.condition_id = forecast_response_days['icon']

  def to_text(self):
    time = datetime.datetime.fromtimestamp(int(self.timestamp))
    s_time = "%s, %s" % (self.weekday, time.strftime("%d"))
    s_max_temp = "Макс: %s °C" % self.max_temp
    s_min_temp = "Мин: %s °C" % self.min_temp
    text = """%s
%s
%s
%s""" % (s_time, s_max_temp, s_min_temp, self.conditions )
    return text

  def is_rain_snow_conditions(self):
    # Ожидается ли дождь, снег или
    rain_snow_conditions = [
                          'chanceflurries',
                          'chancerain',
                          'chancerain',
                          'chancesleet',
                          'chancesleet',
                          'chancesnow',
                          'chancetstorms',
                          'chancetstorms',
                          'flurries',
                          'rain',
                          'sleet',
                          'snow',
                          'tstorms',
                          'tstorms'
    ]

    is_rain_snow = False

    if self.condition_id in rain_snow_conditions:
      is_rain_snow = True

    return is_rain_snow


def get_tomorrow_forecast():
  forecast_response = requests.get('http://api.wunderground.com/api/67baf1d645fb0443/forecast/lang:RU/q/Russia/St_Petersburg.json')

  result = forecast_response.json()
  forecasts = result['forecast']
  simple_forecast = forecasts['simpleforecast']
  days_forecast = simple_forecast['forecastday']
  tomorrowForecast = Forecast(days_forecast[1])
  return tomorrowForecast


# forecast_response = requests.get('http://api.wunderground.com/api/67baf1d645fb0443/forecast/q/Russia/St_Petersburg.json')

# result = forecast_response.json()
# forecasts = result['forecast']
# simple_forecast = forecasts['simpleforecast']
# days_forecast = simple_forecast['forecastday']
# days_forecast[1]
# tomorrowForecast = Forecast(days_forecast[1])

# tomorrowForecast.to_text()
# fcst = Forecast({'minhumidity': 0, 'date': {'year': 2016, 'epoch': '1463846400', 'tz_long': 'Europe/Moscow', 'ampm': 'PM', 'tz_short': 'MSK', 'sec': 0, 'weekday_short': 'Sat', 'month': 5, 'hour': 19, 'monthname_short': 'May', 'isdst': '0', 'min': '00', 'weekday': 'Saturday', 'monthname': 'May', 'pretty': '7:00 PM MSK on May 21, 2016', 'yday': 141, 'day': 21}, 'low': {'fahrenheit': '48', 'celsius': '9'}, 'period': 2, 'pop': 90, 'high': {'fahrenheit': '60', 'celsius': '16'}, 'maxhumidity': 0, 'conditions': 'Rain', 'avehumidity': 78, 'maxwind': {'mph': 10, 'kph': 16, 'degrees': 359, 'dir': 'N'}, 'icon': 'rain', 'icon_url': 'http://icons.wxug.com/i/c/k/rain.gif', 'snow_allday': {'in': 0.0, 'cm': 0.0}, 'snow_night': {'in': 0.0, 'cm': 0.0}, 'snow_day': {'in': 0.0, 'cm': 0.0}, 'qpf_allday': {'in': 0.27, 'mm': 7}, 'qpf_day': {'in': 0.25, 'mm': 6}, 'skyicon': '', 'avewind': {'mph': 8, 'kph': 13, 'degrees': 359, 'dir': 'N'}, 'qpf_night': {'in': 0.02, 'mm': 1}})
# fcst.is_rain_snow_conditions()

# if __name__ == "__main__":
#   print(tomorrowForecast.to_text())
# if (days_forecast and len(days_forecast) > 1 ):
#   days_forecast[1]



# Chance of Rain
# Chance Rain
# Chance of Freezing Rain
# Chance of Sleet мокрый снег
# Chance of Snow
# Chance of Thunderstorms
# Chance of a Thunderstorm
# Freezing Rain

# Rain
# Sleet
# Snow
# Thunderstorms
# Thunderstorm

# chanceflurries
# chancerain
# chancerain
# chancesleet
# chancesleet
# chancesnow
# chancetstorms
# chancetstorms
# flurries
# rain
# sleet
# snow
# tstorms
# tstorms
