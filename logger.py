#!/usr/bin/env python
import sys
import logging
import logging.handlers

class StreamToLogger(object):
	def __init__(self, logger, log_level=logging.INFO):
		self.logger = logger
		self.log_level = log_level

	def write(self, msg):
		if msg.rstrip() != "":
			self.logger.log(self.log_level, msg.rstrip())
