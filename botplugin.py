class BotPluginInterface:

    def __init__(self):
        pass

    def getname(self):
        """Returns plugin name"""
        pass

    def getdescription(self):
        """
        Returns command/plugin description

        :return: description string
        """
        pass

    def getcommands(self):
        """
        Returns a list of available commands
        :return: list of commands
        """
        pass

    def reply(self, message):
        """
        Returns reply to the message

        :param message: message to reply to
        :return: bot reply
        """
        pass

    def setcallback(self, callbackfunction):
        """
        Sets callback for daemon-type of plugins

        :param callbackfunction: callback function that plugin may call
        :return:
        """
        pass