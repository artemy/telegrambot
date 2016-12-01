#!/usr/bin/env python
import sys
import logging
import logging.handlers

class StreamToLogger(object):
	"""
	Taken from
	https://www.electricmonk.nl/log/2011/08/14/redirect-stdout-and-stderr-to-a-logger-in-python/

	"""
	def __init__(self, logger, log_level=logging.INFO):
		self.logger = logger
		self.log_level = log_level

	def write(self, msg):
		if msg.rstrip() != "":
			self.logger.log(self.log_level, msg.rstrip())
