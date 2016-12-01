# coding=utf8
import ConfigParser
import os
from datetime import datetime

import pyowm

from botplugin import BotPluginInterface

COMMANDS = {'/weather': 'Weather report'}


class BotPlugin(BotPluginInterface):
    starttime = 0

    def __init__(self, logger):
        BotPluginInterface.__init__(self)
        configparser = ConfigParser.SafeConfigParser()
        configparser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)),'plugin.cfg'))
        self.apikey = configparser.get('owm', 'apikey')
        self.defaultcity = configparser.get('owm', 'city')
        self.commands = COMMANDS
        self.startTime = datetime.now().replace(microsecond=0)

    def getname(self):
        return "Weather reporter"

    def getdescription(self, command=""):
        if command:
            return self.commands[command]
        return "Reports weather"

    def getcommands(self):
            return self.commands

    def reply(self, message):
        owm = pyowm.OWM(self.apikey)

        forecaster = owm.three_hours_forecast(self.defaultcity)
        forecast = forecaster.get_forecast()
        now = pyowm.timeutils.now()
        w = forecast.get(0)

        wind = w.get_wind()  # {'speed': 4.6, 'deg': 330}
        humidity = w.get_humidity()  # 87
        temperature = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        rain = w.get_rain()  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        status = w.get_detailed_status()  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        location = forecast.get_location().get_name()

        text_forecast = "Today's forecast for " + location + " is:\n"
        text_forecast += 'Avg temperature: ' + str(temperature['temp']) + u" \u2103\n"
        text_forecast += 'Rain: ' + (str(rain['3h']) if rain != {} else "0") + " mm in the coming three hours\n"
        text_forecast += 'Detailed status: ' + status
        return text_forecast