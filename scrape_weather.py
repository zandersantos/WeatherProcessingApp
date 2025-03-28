"""
Name: Zander Santos
Date: March 25th, 2025
Description:

- Create a Weather Processing Application that scrapes
Winnipeg Weather Data (min, max, and mean temperatures) from the Enviornment Canada Website (http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=2018&Month=5).

"""

from html.parser import HTMLParser

class WeatherScraper():
  def __init__(self):
