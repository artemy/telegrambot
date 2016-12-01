from datetime import datetime

from botplugin import BotPluginInterface

COMMANDS = {'/uptime': 'Time this bot is up and running'}

class BotPlugin(BotPluginInterface):
    startTime = 0

    def __init__(self, logger):
        BotPluginInterface.__init__(self)
        self.commands = COMMANDS
        self.startTime = datetime.now().replace(microsecond=0)

    def getname(self):
        return "Uptime tracker"

    def getdescription(self, command=""):
        if command:
            return self.commands[command]
        return "Time this bot is up and running"

    def getcommands(self):
        return self.commands

    def reply(self, message):
        uptime = datetime.now().replace(microsecond=0) - self.startTime
        return str(uptime)