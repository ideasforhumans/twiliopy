import logging
import json
import os
import requests
import sys

#cli-command line interface
#cli = TwilioRestClient(accountSID, authToken)

# logging configuration
logging.basicConfig(level = logging.DEBUG, format='[%(levelname)s] %(asctime)s -- %(message)s')

from twilio.rest import TwilioRestClient

# twilio credentials
twilio_authToken = 'TWILIO_AUTH_TOKEN' in os.environ
twilio_accountSID = 'TWILIO_ACCOUNT_SID' in os.environ

# forecast.io credentials
forecast_api_key = 'FORECAST_API_KEY' in os.environ
forecast_api_baseurl = 'https://api.forecast.io/forecast/'
forecast_api_coord = '37.5333,-77.4667'
forecast_api_url = forecast_api_baseurl + forecast_api_key + '/' + forecast_api_coord

# Dew Point
dewpoint_pleasant = 55
dewpoint_comfortable = 60
dewpoint_gettingsticky = 65
dewpoint_uncomfortable = 70

# Sending request for initial data
forecast_raw_data = requests.get(forecast_api_url)

# Checking for errors
forecast_raw_data.raise_for_status()

# Getting response text
""""currently":{
      "time":1461809073,
      "summary":"Partly Cloudy",
      "icon":"partly-cloudy-night",
      "precipIntensity":0,
      "precipProbability":0,
      "temperature":58.78,
      "apparentTemperature":58.78,
      "dewPoint":51.75,
      "humidity":0.77,
      "windSpeed":12.87,
      "windBearing":211,
      "cloudCover":0.56,
      "pressure":1015.74,
      "ozone":265.66
      }"""
forecast_data = json.loads(forecast_raw_data.text)
dewpoint_data = forecast_data['currently']['dewPoint']


logging.debug(forecast_data['currently']['dewPoint'])

"""twilio_number = '+12403033277'
recipient_number = 'WEATHER_TEXTER_RECIPIENT_NUMBER' in os.environ
message = cli.messages.create(body = 'Hi I like butts and the butts like me', from_ = twilio_number, to = recipient_number)"""
