from datetime import datetime
from random import choice

from botplugin import BotPluginInterface

COMMANDDESCRIPTION = ""
COMMANDS = {'hi' : COMMANDDESCRIPTION, "Hi": COMMANDDESCRIPTION, "Hello": COMMANDDESCRIPTION}

class BotPlugin(BotPluginInterface):

    def __init__(self, logger):
        BotPluginInterface.__init__(self)
        self.commands = COMMANDS
        self.startTime = datetime.now().replace(microsecond=0)

    def getname(self):
        return "Greeter plugin"

    def getdescription(self, command=""):
        if command:
            return self.commands[command]
        return "Greets user with personal message"

    def getcommands(self):
        return self.commands

    def reply(self, message):
        return choice(["Hi", "Hello", "What's up", "How is it going"]) + ", " + message['from']['first_name']