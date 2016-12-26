from scene import *

import location
import time




def getelev():
    x=location.get_location()
    #print(x)
    loc="{:.1f} +/- {:.1f} m".format(x['altitude'],x['vertical_accuracy'])
    return loc



from scene import *



import string

class Elevation (Scene):
    def setup(self):
        location.start_updates()
self.text=LabelNode("", font=('Helvetica',40),parent=self)
#self.add_child(self.text)


def stop(self):
    location.stop_updates()
    
    def should_rotate(self, orientation):
        return True
    
    def draw(self):
        background(0, 0, 0)

txt="Elevation:\n"+getelev()
self.text.text=txt
self.text.position=(self.size.w/2,self.size.h/2)
aspect=self.text.size.h/self.text.size.w
self.text.size=(self.size.w, self.size.w*aspect)


run(Elevation(),frame_interval=60)
