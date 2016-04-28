import logging
import json
import requests
import sys

#cli-command line interface
#cli = TwilioRestClient(accountSID, authToken)

#logging configuration
logging.basicConfig(level = logging.DEBUG, format='[%(levelname)s] %(asctime)s -- %(message)s')

from twilio.rest import TwilioRestClient

#twilio credentials
twilio_authToken = '8f7e01727d917c9e2513f565168f1a12'
twilio_accountSID = 'AC0c9fac97f90a39692aca9a7da6dbbbaa'

#forecast.io credentials
forecast_api_key = 'e1f801c2b84d4402143e23cf8ef8bb11'
forecast_api_baseurl = 'https://api.forecast.io/forecast/'
forecast_api_coord = '37.5333,-77.4667'
forecast_api_url = forecast_api_baseurl + forecast_api_key + '/' + forecast_api_coord

#Dew Point
dewpoint_pleasant = 55
dewpoint_comfortable = 60
dewpoint_gettingsticky = 65
dewpoint_uncomfortable = 70

#sending request for initial data
forecast_raw_data = requests.get(forecast_api_url)

#checking for errors
forecast_raw_data.raise_for_status()

#getting response text
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
recipient_number = '+15712398512'
message = cli.messages.create(body = 'Hi I like butts and the butts like me', from_ = twilio_number, to = recipient_number)"""
