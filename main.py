#!/usr/bin/env python

import sys
import time
from logger import StreamToLogger
import logging
import logging.handlers
from bot import TelegramBot
import ConfigParser

configparser = ConfigParser.SafeConfigParser()
logger = logging.getLogger("telegrambot")


def init_logger(config):
    logger.setLevel(config.get('logger', 'log_level').upper())
    handler = logging.handlers.TimedRotatingFileHandler(config.get('logger', 'path'), when="midnight", backupCount=7)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    sys.stdout = StreamToLogger(logger, logging.INFO)
    sys.stderr = StreamToLogger(logger, logging.ERROR)


def main():
    configparser.read(sys.argv[1])
    init_logger(configparser)
    bot = TelegramBot(configparser, logger)
    bot.message_loop()
    logger.info("Bot " + bot.getMe()['first_name'] + " started")
    # Keep the program running.
    while 1:
        time.sleep(10)


if __name__ == '__main__':
    main()
