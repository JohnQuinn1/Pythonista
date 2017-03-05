# coding: utf-8


import ui
import clipboard
import console

import datetime
import time

global results
results=""

def get_time():
	return datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')


@ui.in_background
def update_time(sender):
	while True:
		time.sleep(1)
		sender.superview['labelTime'].text= get_time()


def button_tapped(sender):
	# Get the button's title for the following logic:
	t = sender.title
	global results
	# Get the labels:
	label = sender.superview['runnerID']
	resultstxt = sender.superview['resultstxt']
	if t in '0123456789':
		if label.text == '':
			label.text = t
		else:
			# Append number:
			label.text += t
	elif t == 'Del':
		# Delete the last character:
		label.text = label.text[:-1]
		if len(label.text) == 0:
			label.text = ''
	elif t == 'DNF':
		if len(label.text)>0:
			tmp="{:} {:>5s} DNF\n".format(get_time(),label.text)
			results=tmp+results
			resultstxt.text=results
			label.text=""
	elif t == 'Stamp':
		if len(label.text)>0:
			tmp="{:} {:>5s}\n".format(get_time(),label.text)
			results=tmp+results
			resultstxt.text=results
			label.text=""
	elif t == 'Copy':
		clipboard.set(results)
		console.hud_alert('Copied to clipboard')
	elif t == 'Reset':
		res=console.alert('Are you sure?', 'Clear Results','Proceed')
		results=''
		resultstxt.text=results

v = ui.load_view()
update_time(v['labelTime'])
v.present('sheet')

