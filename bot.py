# coding=utf8
import telepot
import sys
from datetime import datetime

from pluginloader import PluginLoader


class HelpPlugin():
    def __init__(self, commands):
        self.commands = commands

    def reply(self, message):
        return '\n'.join([k + ": " + v for k,v in  self.commands.items()])


class TelegramBot(telepot.Bot):
    restricted = False
    allowedusers = {}
    botinfo = None
    plugins = {}
    useplugins = False
    commands = {}

    def __init__(self, config, logger):
        super(TelegramBot, self).__init__(config.get('telegrambot', 'token'))
        self.logger = logger

        self.restricted = config.getboolean('telegrambot', 'restrict_contacts')
        self.allowedusers = config.get('telegrambot', 'allowed_contacts').split(',')
        self.botinfo = self.getMe()

        self.logger.info('Bot "' + self.botinfo['first_name'] + '" initialized. Bot id: ' + str(self.botinfo['id']))
        self.logger.info("Listening...")
        self.useplugins = config.getboolean('telegrambot', 'loadplugins')
        if (self.useplugins):
            pluginloader = PluginLoader(self.logger)
            self.plugins = pluginloader.loadPlugins(self.callback)
            self.logger.info("Plugins are loaded")
            for k,v in self.plugins.iteritems():
                if (k.startswith('/')):
                    self.commands[k] = v.getdescription(k)
            self.plugins['/help'] = HelpPlugin(self.commands)
            self.logger.info("Help is: " + str(self.commands))



    def handle(self, msg):
        self.logger.info("Incoming message: " + msg['text'])
        if self.restricted and str(msg['from']['id']) not in self.allowedusers:
            # outcomingmessage = report_unknown_contact()
            # self.sendMessage(msg['chat']['id'], outcomingmessage)
            self.logger.error('Unknown contact: ' + str(msg['from']['first_name']) + ' id: ' + str(msg['from']['id']))
        else:
            command = msg['text'].split(" ")[0]
            self.logger.debug("Command " + command + " found:" + str(command in self.plugins))
            if (self.useplugins and command in self.plugins):
                outcomingmessage = self.plugins[command].reply(msg)
                self.sendMessage(msg['chat']['id'], outcomingmessage)


    def callback(self, message):
        for user in self.allowedusers:
            self.sendMessage(user, message)

    def sendMessage(self, chat_id, text,
                    parse_mode=None, disable_web_page_preview=None,
                    disable_notification=None, reply_to_message_id=None, reply_markup=None):
        self.logger.info("Outcoming message to " + str(chat_id) + " : " + repr(text))
        super(TelegramBot, self).sendMessage(chat_id, text)