class BotPluginInterface:

    def __init__(self):
        pass

    def getname(self):
        pass

    def getdescription(self):
        pass

    def getcommands(self):
        pass

    def reply(self, message):
        pass

    def setcallback(self, callbackfunction):
        pass