import weather
import wind

def test_time_from_epoch():
    time_epoch = 1462644000
    assert weather.time_str_from_epoch(time_epoch) == "07.05.2016 21:00"
    time_epoch = 1462656600
    assert weather.time_str_from_epoch(time_epoch) == "08.05.2016 00:30"


def test_get_wind_rhumbs():
  check_wind_rhumbs(360, None)
  check_wind_rhumbs(0, "С")
  check_wind_rhumbs(359, "С")
  check_wind_rhumbs(1, "С")
  check_wind_rhumbs(180, "Ю")
  check_wind_rhumbs(90, "В")
  check_wind_rhumbs(270, "З")
  check_wind_rhumbs(25, "СВ")
  check_wind_rhumbs(136, "ЮВ")
  check_wind_rhumbs(216, "ЮЗ")
  check_wind_rhumbs(301, "СЗ")


def check_wind_rhumbs(wd, rhumbs_expected):
  cur_wind = wind.Wind(1, wd)
  assert cur_wind.to_rhumbs() == rhumbs_expected


def test_mps_by_kph():
  cur_wind = wind.Wind(0, 0)
  assert cur_wind.get_mps_by_kph(7) == 1.9444460000000001
  assert cur_wind.get_mps_by_kph(10) == 2.7777800000000004
  assert cur_wind.get_mps_by_kph(60) == 16.666680000000003


def test_format_wind_mps():
  cur_wind = wind.Wind(0, 0)
  assert cur_wind.format_wind_mps(3.8888920000000002) == "3.9"
  assert cur_wind.format_wind_mps(1.9444460000000001) == "1.9"
  assert cur_wind.format_wind_mps(2.7777800000000004) == "2.8"
  assert cur_wind.format_wind_mps(16.666680000000003) == "16.7"


def test_wind_output():
  cur_wind = wind.Wind(0, 0)
  assert cur_wind.to_text () == "С 0.0 м/с"

  cur_wind = wind.Wind(10, 90)
  assert cur_wind.to_text () == "В 2.8 м/с"

  cur_wind = wind.Wind(7, 216)
  assert cur_wind.to_text () == "ЮЗ 1.9 м/с"

  cur_wind = wind.Wind(60, 301)
  assert cur_wind.to_text () == "СЗ 16.7 м/с"


def test_current_weather_output():
  json_response = {'current_observation': {'heat_index_c': 'NA', 'local_epoch': '1463149232', 'observation_epoch': '1463148000', 'temp_f': 66, 'dewpoint_c': 1, 'wind_kph': 14, 'nowcast': '', 'weather': 'Ясно', 'wind_dir': 'South', 'forecast_url': 'http://www.wunderground.com/global/stations/26063.html', 'observation_time_rfc822': 'Fri, 13 May 2016 17:00:00 +0300', 'temperature_string': '66 F (19 C)', 'local_tz_short': 'MSK', 'relative_humidity': '30%', 'local_tz_long': 'Europe/Moscow', 'display_location': {'elevation': '4.00000000', 'city': 'Санкт-Петербург', 'longitude': '30.29999924', 'state_name': 'Russia', 'wmo': '26063', 'state': '', 'magic': '1', 'latitude': '59.97000122', 'country_iso3166': 'RU', 'country': 'RS', 'zip': '00000', 'full': 'Санкт-Петербург, Russia'}, 'solarradiation': '--', 'precip_today_in': '0.00', 'wind_gust_mph': 0, 'feelslike_f': '66', 'windchill_c': 'NA', 'icon': 'clear', 'image': {'url': 'http://icons.wxug.com/graphics/wu2/logo_130x80.png', 'title': 'Weather Underground', 'link': 'http://www.wunderground.com'}, 'observation_time': 'Last Updated on Май 13, 5:00 PM MSK', 'pressure_in': '29.77', 'precip_today_string': '0.00 in (0.0 mm)', 'UV': '-1', 'heat_index_f': 'NA', 'pressure_trend': '0', 'station_id': 'ULLI', 'wind_degrees': 180, 'wind_string': 'From the South at 9 MPH', 'visibility_km': 'N/A', 'wind_gust_kph': 0, 'local_time_rfc822': 'Fri, 13 May 2016 17:20:32 +0300', 'precip_1hr_string': '-9999.00 in (-9999.00 mm)', 'ob_url': 'http://www.wunderground.com/cgi-bin/findweather/getForecast?query=59.79840088,30.26664925', 'temp_c': 19, 'local_tz_offset': '+0300', 'windchill_string': 'NA', 'observation_location': {'country': 'RS', 'city': 'St. Petersburg', 'longitude': '30.26664925', 'latitude': '59.79840088', 'state': '', 'elevation': '75 ft', 'full': 'St. Petersburg, ', 'country_iso3166': 'RU'}, 'precip_1hr_metric': '--', 'feelslike_c': '19', 'icon_url': 'http://icons.wxug.com/i/c/k/clear.gif', 'history_url': 'http://www.wunderground.com/history/airport/ULLI/2016/5/13/DailyHistory.html', 'precip_today_metric': '0.0', 'wind_mph': 9, 'heat_index_string': 'NA', 'estimated': {}, 'windchill_f': 'NA', 'dewpoint_f': 34, 'pressure_mb': '1008', 'precip_1hr_in': '-9999.00', 'dewpoint_string': '34 F (1 C)', 'visibility_mi': 'N/A', 'feelslike_string': '66 F (19 C)'}, 'response': {'termsofService': 'http://www.wunderground.com/weather/api/d/terms.html', 'features': {'conditions': 1}, 'version': '0.1'}}
  current_weather = weather.CurrentWeather(json_response)
  assert current_weather.to_text() == """Санкт-Петербург
13.05.2016 17:00
Ясно
Температура: 19 °C
Ощущается как: 19 °C
Ветер: Ю 3.9 м/с"""
