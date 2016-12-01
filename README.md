# telegrambot
Ordinary everyday normal telegram bot with plugin support

##Description:
Telegram bot that replies to the user messages or relays notifications from enabled plugins. 

Telegram API is used via [telepot](https://github.com/nickoala/telepot) library.

##Architecture
Bot uses plugins to extend its functionality. 

Plugins can reply to incoming message or make use of callback to propagate events back to bot to relay to the subscribed users.
For reference about plugin architecture, refer to botplugin.py

Included plugins:
- ds18b20

   reports temperature from configured DS18B20 sensors
- greetings

   replies to kind users with greetings
- mqtt

   listens to configured mqtt channels and propagates messages to the bot
- uptime

   reports bot uptime
- weather

   reports weather for configured city
   
   
The bot has one integrated plugin that loads at last - HelpPlugin.
HelpPlugin collects all the commands from available plugins (only the ones that start with "/") and replies back with list of those commands and their descriptions 

For the plugin configuration, see plugin folders for code & configuration examples.
   
##Configuration
```[logger]
log_level=INFO #Log level (CRITICAL, ERROR, WARNING, INFO, DEBUG)
path=bot.log #path to the log file

[telegrambot]
loadplugins=true #plugins enabled
restrict_contacts=true #only reply to the contacts from the list below
allowed_contacts=1234567890 #contacts that bot will reply to
callback_contacts=1234567890 #contacts that will receive callback messages from plugins
token=0987654321 #bot token
```

##Usage
`main.py path-to-configuration`

##Running as a daemon
It's possible to run this bot as a linux daemon. File init.script contains example configuration of init script 

##TODO
- [x] complete this readme
- [ ] extend weather plugin to report weather for arbitrary cities
- [ ] ?????
- [ ] PROFIT

##Credits
- [telepot](https://github.com/nickoala/telepot) - Telegram API library
- [sensor](https://github.com/nickoala/sensor) - Sensor library for temperature/humidity/pressure sensors
- [paho-mqtt](https://github.com/eclipse/paho.mqtt.python) - MQTT library
- [pyowm](https://github.com/csparpa/pyowm) - OpenWeatherMap API library