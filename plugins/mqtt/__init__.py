# coding=utf8
import ConfigParser
import os
import time
import paho.mqtt.client as mqtt

from botplugin import BotPluginInterface

class BotPlugin(mqtt.Client, BotPluginInterface):
    callback = {}
    channels = []

    def __init__(self, logger):
        configparser = ConfigParser.SafeConfigParser()
        configparser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)),'plugin.cfg'))
        self.channels = [e.strip() for e in configparser.get('mqtt', 'channels').split(',')]
        self.server = configparser.get('mqtt', 'server')
        self.port = configparser.getint('mqtt', 'port')
        self.keepalive = configparser.getint('mqtt', 'keepalive')
        self.clientid = configparser.get('mqtt', 'clientid')
        self.logger = logger
        mqtt.Client.__init__(self, client_id=self.clientid)


    def getname(self):
        return "MQTT listener"

    def getdescription(self, command=""):
        return "Notifies user of incoming MQTT messages"

    def setcallback(self, callbackfunction):
        self.callback = callbackfunction
        self.connect(self.server, self.port, self.keepalive)
        self.subscribe([(channel,0) for channel in self.channels])

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        self.loop_start()

    def on_message(self, client, userdata, msg):
        self.logger.info("Incoming message: " + msg.topic+" "+str(msg.payload))
        self.callback('[MQTT] {}: {}'.format('from ' + msg.topic if len(self.channels) > 1 else '', msg.payload))


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        self.logger.info("Connected with result code "+str(rc))

    def on_log(self, mqttc, obj, level, string):
        self.logger.debug(string)
