"""
Name: Zander Santos
Date: March 25th, 2025
Description:

- Create a Weather Processing Application that scrapes
Winnipeg Weather Data (min, max, and mean temperatures) from the Enviornment Canada Website (http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=2018&Month=5).

"""

from html.parser import HTMLParser

class WeatherScraper(HTMLParser):
  def __init__(self, start_year, start_month):
    climate_weather_url = "http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=2018&Month=5"
    climate_weather_error_url = "https://climate.weather.gc.ca/historical_data/search_historic_data_e.html"
    year = start_year
    month = start_month
    climate_weather_data = {}

  def handle_starttag(self, tag, attrs):
    return super().handle_starttag(tag, attrs)

  def handle_endtag(self, tag):
    return super().handle_endtag(tag)

  def handle_data(self, data):
    return super().handle_data(data)

  def scrape_data(self)
