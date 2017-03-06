# coding: utf-8


import ui
import clipboard
import console

import logging
import datetime
import time

# Turn on logging in case of a crash
logging.basicConfig(filename='RunStamp.log',level=logging.INFO)

#global results
results=''
results_csv=''
so_far=0

def get_time():
	return datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
	
	
def update_results(no, id, DNF=False):
	global results
	global results_csv
	global runners
	
	DNF_str='DNF' if DNF else ''
	name=runners.get(id)
	name=name if name else ''
	tmp="{:3d} {:} {:>4s} {:} {:}\n".format(no,get_time(),id, name, DNF_str)
	tmp_csv="{:3d}, {:}, {:>4s}, {:}, {:}\n".format(no,get_time(),id, name, DNF_str)
	logging.info(tmp_csv)
	results=tmp+results
	results_csv=tmp_csv+results_csv
	

@ui.in_background
def update_time(sender):
	while True:
		time.sleep(1)
		sender.superview['labelTime'].text= get_time()


def button_tapped(sender):
	# Get the button's title for the following logic:
	t = sender.title
	global results
	global results_csv
	global so_far
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
	elif t == 'DNF' or t == 'Stamp':
		if len(label.text)>0:
			DNF=True if t == 'DNF' else False
			so_far+=1
			update_results(so_far, label.text,DNF)
			resultstxt.text=results
			label.text=""
	elif t == 'Copy':
		clipboard.set(results_csv)
		console.hud_alert('Copied to clipboard')
	elif t == 'Reset':
		res=console.alert('Are you sure?', 'Clear Results','Proceed')
		results=''
		results_csv=''
		so_far=0
		resultstxt.text=results


########################
# map numbers to names

runners={}

import csv
try:
	with open('runners.txt','r') as csvfile:
		reader=csv.reader(csvfile)
		for row in reader:
			if len(row)>0: # empty last line crash
				runners[row[0].strip()]=row[1].strip()
except FileNotFoundError:
	pass
##################################


v = ui.load_view()
update_time(v['labelTime'])
v.present('sheet')

