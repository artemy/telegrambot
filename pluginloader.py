import imp
import os

PluginFolder = "./plugins"
MainModule = "__init__"


class PluginLoader():
    def __init__(self, logger):
        self.logger = logger

    def __listPlugins(self):
        """
        List available plugins

        :return: list of available plugins
        """
        plugins = []
        possibleplugins = os.listdir(PluginFolder)
        for i in possibleplugins:
            location = os.path.join(PluginFolder, i)
            if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
                continue
            info = imp.find_module(MainModule, [location])
            plugins.append({"name": i, "info": info})
        return plugins

    def __loadPlugin(self, plugin):
        """
        Loads (initializes) specified plugin

        :param plugin: initialized plugin instance
        """
        return getattr(imp.load_module(MainModule, *plugin["info"]), "BotPlugin")(self.logger)

    def loadPlugins(self, callbackfunction):
        """
        Load all available plugins and sets callback for them

        :param callbackfunction: function that plugins can call to relay messages to bot
        :return: dict with initialized plugin instances
        """
        pluginlist = {}
        for i in self.__listPlugins():
            plugin = self.__loadPlugin(i)
            self.logger.info("Loaded plugin " + plugin.getname() + (" with commands: " + ', '.join([e for e in plugin.getcommands().keys()]) if plugin.getcommands() else "" ))
            plugin.setcallback(callbackfunction)
            if plugin.getcommands():
                for command in plugin.getcommands():
                    pluginlist[command] = plugin
        return pluginlist