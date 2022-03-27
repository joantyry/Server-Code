#!/usr/local/bin/python3

from ctypes import *
import cgi;
import cgitb;


import requests
import json
import sys
import random 
from math import ceil 
from decimal import *
import numpy
from sympy import mod_inverse

import hashlib
import time
import csv

from random import randint
from datetime import datetime, date


from ctypes import *
from subprocess import *


print("Content-type: text/html\r \n")

#sessionID = sys.argv[1]

file = "/Applications/XAMPP/htdocs/LocalServer/codes/PowerMod.o"




def Setup():

	'''
	Read values sent by the user from file

	'''

	today = date.today()
	now = datetime.now()
	sessionID = today.strftime("%Y%m%d")+ now.strftime("%H%M%S") +''.join(["{}".format(randint(0, 9)) for num in range(0, 5)]) 

	
	global y1
	global y1_prime

	f = open('../Database/SetUp.json', "r")
	
	#data = json.load(f)

	data = [json.loads(line) for line in f]
	
	#print(data)

	for i in data:

		if i['Name'] == 'Step1-setup' and i['src'] == 'User':

			p = i['p']
			g = i['g']
			x11 = i['share_x']
			#x1 = [int(j) for j in x11.split(",")]
			#x1 = x1[1]
			x1 = x11[1]
			SetupID = i['SetupID']
	f.close	

	time_start = time.time_ns()		

	x1_prime = random.randrange(1, int(p))
	#print(x1, x1_prime)

	x1_prime = str(x1_prime)

	proc = Popen(file, stdin=PIPE, stdout=PIPE)
	
	out, err = proc.communicate(input= p.encode()+b'\n'+g.encode()+b'\n'+x1.encode())

	y1 = out.decode().strip() #strip removes \n at the end of the string  

			
	#y1 = g ** x1 % p


	proc2 = Popen(file, stdin=PIPE, stdout=PIPE)
	
	out, err = proc2.communicate(input= p.encode()+b'\n'+g.encode()+b'\n'+x1_prime.encode())

	y1_prime = out.decode().strip() 
	#y1_prime = g ** x1_prime % p

	y1 = str(y1)
	y1_prime = str(y1_prime)

	total_time =  time.time_ns() - time_start, 1	


	with open('/Applications/XAMPP/htdocs/LocalServer/Database/SetupTime.csv', 'a+', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)

		# write the header
		#writer.writerow(header)

		# write the data
		writer.writerow(total_time)



	'''
	store y1, y1_prime in personal database

	'''
	

	
	#f.write("\n")


	#with open('../Database/personal.json', 'w') as outfile:
		#json.dump(data, outfile)


	#print(y1 )

	data = {'Name':'Step1-setup','src': 'HomeServer', 'dst': 'HomeServer','y': y1, 'y_prime': y1_prime, 'x_prime': x1_prime, 'SetupID': SetupID, 'sessionID' : sessionID }

	f = open('../Database/SetUp.json', 'a') 
	f.write(json.dumps(data)+ "\n")		



def sendValues():	

	'''
	Send values to the other servers.
	'''

	today = date.today()
	now = datetime.now()
	sessionID = today.strftime("%Y%m%d")+ now.strftime("%H%M%S") +''.join(["{}".format(randint(0, 9)) for num in range(0, 5)]) 

	
	#servers = {'https://40.117.176.226/CloudServer1/PostProcess/PostProcess2.php' : 'CloudServer1', 'https://40.76.203.48/CloudServer2/PostProcess/PostProcess2.php': 'CloudServer2'}

	
	f = open('/Applications/XAMPP/htdocs/LocalServer/codes/config.json', "r")
	servers  = json.load(f)

	headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json'}


	for key,value in servers.items():

		url = value
		dst = key


		myobj = {'Name':'Step1-setup','src': 'HomeServer', 'dst': dst, 'y': y1, 'y_prime': y1_prime, 'SetupID': SetupID,'sessionID' : sessionID}
		session = requests.Session() 

		session.post(url, json = myobj, headers=headers,  verify=False)


	
	
		#info1 = requests.post(url, json = myobj, headers=headers)

		#print(info1.text)

		#print (myobj)
	


	'''
	Store in database for user (message for user)
	'''

	

	Userdata = {'Name':'Step1-setup','src': 'HomeServer', 'dst':'User','y': y1, 'y_prime': y1_prime, 'SetupID': SetupID, 'sessionID' : sessionID }

	with open('../Database/userMessages.json', 'w') as outfile:
		json.dump(Userdata, outfile)






if __name__ == '__main__':
	
	Setup()
	sendValues()
