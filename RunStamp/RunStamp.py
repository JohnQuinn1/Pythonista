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
so_far=[]

def get_time():
	return datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
	
	
def update_results(no, id, MSG=''):
	global results
	global results_csv
	global runners
	
	name=runners.get(id)
	name=name if name else ','
	tmp="{:3d} {:} {:>4s} {:} {:}\n".format(no,get_time(),id, name, MSG)
	tmp_csv="{:3d}, {:}, {:>4s}, {:}, {:}\n".format(no,get_time(),id, name, MSG)
	logging.info(tmp_csv)
	results=tmp+results
	results_csv=tmp_csv+results_csv
	

@ui.in_background
def update_time(sender):
	while True:
		sender.superview['labelTime'].text= get_time()
		time.sleep(1)


def subview_button_tapped(sender):
	global results
	global results_csv
	global so_far
	global runners
	
	t = sender.title
	displaytxt=sender.superview['results_textview']

	if t == 'In':
		displaytxt.text=results_csv
	elif t == 'Not':
		i=0
		txt=""
		tmp=sorted(runners.keys(),key=int)
		for id in tmp:
			if id not in so_far:
				i+=1
				txt+="{:3d}, {:>4s}, {:}\n".format(i,id,runners[id])
		displaytxt.text=txt
	elif t == 'DNF':
		line=results_csv.split('\n')
		i=0
		txt=""
		for res in line:
			#print(res.split(','))
			if res.split(',')[-1].strip() == 'DNF':
				i+=1
				txt+=res+'\n'
		displaytxt.text=txt
	elif t == 'Copy':
		clipboard.set(displaytxt.text)
		console.hud_alert('Copied to clipboard')



def button_tapped(sender):
	# Get the button's title for the following logic:
	t = sender.title
	
	global results
	global results_csv
	global so_far
	
	# Get the labels:
	label = sender.superview['runnerID']
	
	resultstxt =sender.superview['resultstxt']
	
	erase_button=sender.superview['buttonErase']
	
	if t in '0123456789':
		if label.text == '':
			label.text = t
			erase_button.tint_color='red'
		else:
			# Append number:
			label.text += t
	elif t == 'Del':
		# Delete the last character:
		label.text = label.text[:-1]
		if len(label.text) == 0:
			label.text = ''
			erase_button.tint_color='magenta'
	elif t == 'DNF' or t == 'Stamp':
		if len(label.text)>0:
			MSG='DNF' if t == 'DNF' else ''
			if not label.text in so_far:
				so_far.append(label.text)
			update_results(len(so_far), label.text,MSG)
			resultstxt.text=results
			label.text=""
			erase_button.tint_color='magenta'
	elif t == 'View':
		#v2=ui.load_view('Test/Test_subview.pyui')
		v2=ui.load_view('RunStamp_subview.pyui')
		sender.superview.add_subview(v2)
		v2.present('fullscreen')
		#sender.superview.remove_subview(v2)
	elif t == 'Erase':
		if len(label.text)==0:
			res=console.alert('Are you sure?', 'Clear Results','Proceed')
			results=''
			resultstxt.text=results
			results_csv=''
			so_far=[]
		else:
			if label.text in so_far:
				so_far.remove(label.text)
				update_results(len(so_far),label.text,"ERR")
				resultstxt.text=results
				label.text=''
				erase_button.tint_color='magenta'
	


########################
# map numbers to names

runners={}

import os
path=os.path.join(os.path.expanduser('~'),'Documents/Git/Pythonista/RunStamp')
os.chdir(path)


try:
	with open("runners.txt","r") as f:
		for line in f:
			fields=line.split('\t')
			id=fields[0].strip()
			name=fields[1].strip()
			if not ',' in name:
				name+=','
			runners[id]=name
except FileNotFoundError:
	pass


#import csv
#try:
#	with open('runners.txt','r') as csvfile:
#		reader=csv.reader(csvfile)
#		for row in reader:
#			if len(row)>0: # empty last line crash
#				runners[row[0].strip()]=row[1].strip()
#except FileNotFoundError:
#	pass
	
##################################


v = ui.load_view()
update_time(v['labelTime'])
v.present('fullscreen', orientations=['portrait'])

