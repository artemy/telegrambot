import imp
import os

import time

PluginFolder = "./plugins"
MainModule = "__init__"


class PluginLoader():
    def __init__(self, logger):
        self.logger = logger

    def __listPlugins(self):
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
        return getattr(imp.load_module(MainModule, *plugin["info"]), "BotPlugin")(self.logger)


    def loadPlugins(self):
        return self.loadPlugins(self, True)

    def loadPlugins(self, callbackfunction):
        pluginlist = {}
        for i in self.__listPlugins():
            plugin = self.__loadPlugin(i)
            self.logger.info("Loaded plugin " + plugin.getname() + (" with commands: " + ', '.join([e for e in plugin.getcommands().keys()]) if plugin.getcommands() else "" ))
            plugin.setcallback(callbackfunction)
            if plugin.getcommands():
                for command in plugin.getcommands():
                    pluginlist[command] = plugin
        return pluginlist

def main():
    pluginloader = PluginLoader()
    plugins = pluginloader.loadPlugins(printcallback)
    while 1:
        time.sleep(10)

def printcallback(plugin):
    print "Callback is called by" + plugin

if __name__ == '__main__':
    main()