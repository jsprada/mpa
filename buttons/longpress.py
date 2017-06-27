#!/usr/bin/python3
# Track length of GPIO button press. 
# By Johnny Sprada 
# https://github.com/jsprada/mpdbuttons

import time

class NewButton(object):
	def __init__(self, pin):
		self.pin = pin
		self.press_time = 0
		self.release_time = 0
		self.elapsed_time = 0

		
	def set_press_time(self):
		self.press_time = time.time()

	def set_release_time(self):
		self.release_time = time.time()
		self.elapsed_time = int( (self.release_time - self.press_time) * 1000 )

	def reset_press_time(self):
		self.release_time = 0
		self.press_time = 0

