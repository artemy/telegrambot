# -*- coding: utf-8 -*-
# from sensor import DS18B20
import ConfigParser
import os

from botplugin import BotPluginInterface

COMMANDS = {'/temp': 'Temperature from ds18b20'}

class BotPlugin(BotPluginInterface):

    sensors = {}

    def __init__(self, logger):
        self.logger = logger
        configparser = ConfigParser.SafeConfigParser()
        configparser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)),'plugin.cfg'))
        self.sensors = dict(configparser.items("sensors"))
        self.logger.debug("Sensors found: " + str(self.sensors))
        self.logger = logger
        self.commands = COMMANDS

    def getname(self):
        return "DS18B20 sensor plugin"

    def getdescription(self, command=""):
        if command:
            return self.commands[command]
        return "Retrieves temperature from DS18B20 sensors"

    def getcommands(self):
        return self.commands

    def reply(self, message):
        sensorsdata = []
        # for name,sensor in self.sensors.items():
        #     dstemp = DS18B20.DS18B20(sensor).temperature()
        #     sensorsdata.append(name.capitalize() + ' temperature is {:.1f}°C'.format(dstemp.C))
        return '\n'.join(sensorsdata)




