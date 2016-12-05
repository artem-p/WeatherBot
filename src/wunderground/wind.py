# coding: utf-8
class Wind():
  def __init__(self, kph, wind_dir):
    self.wd = wind_dir
    self.kph = kph

  def to_rhumbs(self):
    #   Получаем направление ветра в румбах по градусам
    WD_MIN = 0
    WD_MAX = 359

    NORTH_MIN = 338
    NORTH_MAX = 23
    NORTH_TEXT = "С"

    NORTH_OST_MIN = 24
    NORTH_OST_MAX = 67
    NORTH_OST_TEXT = "СВ"

    OST_MIN = 68
    OST_MAX = 112
    OST_TEXT = "В"

    SOUTH_OST_MIN = 113
    SOUTH_OST_MAX = 157
    SOUTH_OST_TEXT = "ЮВ"

    SOUTH_MIN = 158
    SOUTH_MAX = 202
    SOUTH_TEXT = "Ю"

    SOUTH_WEST_MIN = 203
    SOUTH_WEST_MAX = 247
    SOUTH_WEST_TEXT = "ЮЗ"

    WEST_MIN = 248
    WEST_MAX = 292
    WEST_TEXT = "З"

    NORTH_WEST_MIN = 293
    NORTH_WEST_MAX = 337
    NORTH_WEST_TEXT = "СЗ"

    rhumbWind = None
    if self.wd is not None:
        if WD_MIN <= self.wd and self.wd <= WD_MAX:

            if NORTH_MIN <= self.wd <= WD_MAX or 0 <= self.wd <= NORTH_MAX:
                rhumbWind = NORTH_TEXT
            elif NORTH_OST_MIN <= self.wd <= NORTH_OST_MAX:
                rhumbWind = NORTH_OST_TEXT
            elif OST_MIN <= self.wd <= OST_MAX:
                rhumbWind = OST_TEXT
            elif SOUTH_OST_MIN <= self.wd <= SOUTH_OST_MAX:
                rhumbWind = SOUTH_OST_TEXT
            elif SOUTH_MIN <= self.wd <= SOUTH_MAX:
                rhumbWind = SOUTH_TEXT
            elif SOUTH_WEST_MIN <= self.wd <= SOUTH_WEST_MAX:
                rhumbWind = SOUTH_WEST_TEXT
            elif WEST_MIN <= self.wd <= WEST_MAX:
                rhumbWind = WEST_TEXT
            elif NORTH_WEST_MIN <= self.wd <= NORTH_WEST_MAX:
                rhumbWind = NORTH_WEST_TEXT
    return rhumbWind

  def to_text(self):
    self.to_rhumbs()
    return "%s %s м/с" % (self.to_rhumbs(), self.format_wind_mps(self.get_mps_by_kph(self.kph)))


  def get_mps_by_kph(self, kph):
    mps = kph*0.277778
    return mps


  def format_wind_mps(self, wind_mps):
    # Форматируем скорость ветра для вывода. Оставляем 1 знак после запятой
    return "{:.1f}".format(wind_mps)

