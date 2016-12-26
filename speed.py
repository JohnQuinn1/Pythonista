from scene import *

import location
import time

def getspeed():
	l=location.get_location()
	if l is not None:
		s=['speed']
		speed="{:.2f} m/s \n{:.2f} km/hr\n{:.2f} mph".format(s,s*3.6,s*2.24)
	else:
		speed="🛰?"
	return speed


from scene import *

import string

class Speed (Scene):
	def setup(self):
		location.start_updates()
		self.text=LabelNode("", font=('Helvetica',80),parent=self)
#		self.add_child(self.text)


	def stop(self):
		location.stop_updates()

	def should_rotate(self, orientation):
		return True

	def draw(self):
		#background(0, 0, 0)

		txt=getspeed()
		self.text.text=txt
		self.text.position=(self.size.w/2,self.size.h/2)
		aspect=self.text.size.h/self.text.size.w

		self.text.size=(self.size.w, self.size.w*aspect)

		if self.text.size.h>self.size.h:
			self.text.size=(self.size.h/aspect, self.size.h)

run(Speed(),frame_interval=30)
