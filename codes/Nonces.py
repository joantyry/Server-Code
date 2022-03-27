#!/usr/bin/python3

from ctypes import *
import cgi;
import cgitb;

import random
from random import randint
import json
import sys
from datetime import datetime, date

print("Content-type: text/html\r \n")

phaseID = sys.argv[1]


def Nonces(phaseID):

	f = open('../Database/SetUp.json', "r")
	
	#data = json.load(f)

	data = [json.loads(line) for line in f]
	
	for i in data:

		if i['Name'] == 'Step1-setup' and i['src'] == 'User':

			p = int(i['p'])
			sharex = i['share_x']
			ID = int(sharex[0])


	nonce = random.randint(0, p)

	nonce1 = [ID, str(nonce)]	

	today = date.today()
	now = datetime.now()
	sessionID = today.strftime("%Y%m%d")+ now.strftime("%H%M%S") +''.join(["{}".format(randint(0, 9)) for num in range(0, 5)]) 


	Userdata = {'Name':'Reconstruction1','src': 'HomeServer', 'dst':'User','Nonce': nonce1 , 'phaseID': phaseID, 'sessionID' : sessionID}	 

	with open('../Database/userMessages.json', 'w') as outfile:
			json.dump(Userdata, outfile)


if __name__ == '__main__':
	Nonces(phaseID)			