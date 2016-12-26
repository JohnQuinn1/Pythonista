# coding: utf-8
# coding: utf-8

import ui
import datetime
import time

def get_time():
	return datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')

def update_time(sender):
	sender.superview['label1'].text=get_time()

@ui.in_background
def button2_tapped(sender):
	for i in range(10):
		time.sleep(1)
		sender.superview['label2'].text= get_time()
	
def subview(sender):
	v2=ui.load_view('Test_subview.pyui')
	sender.superview.add_subview(v2)
	v2.present('sheet')
	
v = ui.load_view('Test.pyui')
button2_tapped(v['label2'])

v.present('sheet')