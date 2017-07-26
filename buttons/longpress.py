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
		self.release_time = 0
		self.elapsed_time = 0
		self.print_all()

	def set_release_time(self):
		if (self.press_time != 0 ):
			self.release_time = time.time()
			self.elapsed_time = int( (self.release_time - self.press_time) * 1000 )
			#self.reset_press_time()
			self.print_all()

	def reset_press_time(self):
		self.release_time = 0
		self.press_time = 0
		self.elapsed_time = 0

	def print_all(self):
		print("    -   time: %s" % time.time())
		print("    -    pin: %s" % self.pin)
		print("    -  press: %s" % self.press_time)
		print("    -release: %s" % self.release_time)
		print("    -elapsed: %s" % self.elapsed_time)

