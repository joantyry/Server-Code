#!/usr/local/bin/python3

import cgi;
import cgitb;


import requests
import json
import random 
from math import ceil 
from decimal import *
import numpy
from sympy import mod_inverse
import numpy as np
import sys

import hashlib

from random import randint
from datetime import datetime, date


from ctypes import *
from subprocess import *

import time
import Condition as cond


print("Content-type: text/html\r \n")

VerifyQt = "/Applications/XAMPP/htdocs/LocalServer/codes/VerifyQt.o"
SessionKey = "/Applications/XAMPP/htdocs/LocalServer/codes/SessionKey.o"


phaseID = sys.argv[1]
OnlineServers = [int(sys.argv[2]), int(sys.argv[3])]

def Step4(OnlineServers, phaseID):
	#global x1_prime



	today = date.today()
	now = datetime.now()
	sessionID = today.strftime("%Y%m%d")+ now.strftime("%H%M%S") +''.join(["{}".format(randint(0, 9)) for num in range(0, 5)]) 


	f = open('../Database/SetUp.json', "r")
        
	#data = json.load(f)

	data = [json.loads(line) for line in f]	
        
	for i in data:

		if i['Name'] == 'Step1-setup' and i['src'] == 'User':

			p =i['p']
			q = int(i['q'])
			g = i['g']
			h = i['h']
			h_prime = i['h_prime']


			share_x = i['share_x']
			ID = int(share_x[0])



		if i['Name'] == 'Step1-setup' and i['src'] == 'HomeServer':

			x1_prime =  i['x_prime']



		if i['Name'] == 'Step2-setup' and i['src'] == 'User':

				share = i['share_pr']
				#share = [int(j) for j in share.split(",")]

				shareID_pr = int(share[0])
				share_pr = share[1]
	




	#I = [3,2]

	'''
	Read all C_bars and append them in a list then check if the product of all C_bars = y_bar
	'''

	C_bars = []
	#x1_prime =  []

	for i_onl in OnlineServers:

		if (i_onl!=ID):
			server = i_onl

	#print(server)		



	if server == 2:
		server_name = "CloudServer1"
	else:
		server_name = "CloudServer2"	


	#f_2 = open('../Database/Recon.json', "r")
	
		#data = json.load(f)

	#data_2 = [json.loads(line) for line in f_2]	

	#print(data_2)


	file_str = '../Database/Recon.json'	


	data = cond.fileCondition(file_str)


	#check whether the other server has completed	

	result = cond.DataExists(data, "DVP3", phaseID, server_name)

	#print(result)

	

	i = 0

	while result != True:

		time.sleep(0.1)

		data = cond.fileCondition(file_str)

		result = cond.DataExists(data, "DVP3", phaseID, server_name)

		i = i+1
		print(f'Tried {i} times')


	
	
	if result == True:
		startS4 =datetime.now()	

		
		for i2 in data:

		

			if i2['Name'] == 'DVP2' and i2['phaseID'] == phaseID:



				if (server == 2):	

					#print(i2)

					if i2['src'] == 'CloudServer1':

						

						Newdata = i2

						#print(Newdata)

						CS_bar = Newdata['C_bar2']
						C_bars.append(CS_bar)

						sigma_Qs = Newdata['sigma_Qs']
						

				else:

					if i2['src'] == 'CloudServer2':

						Newdata = i2

						CS_bar = Newdata['C_bar3']
						C_bars.append(CS_bar)

						sigma_Qs = Newdata['sigma_Qs']
						#print(C_bars)


			if i2['Name'] == 'DVP2' and i2['phaseID'] == phaseID and i2['src'] == 'HomeServer':	

				y_bar=i2['y_bar']
				g_bar =i2['g_bar']
				C_bar1 = i2['C_bar1']
				tau_prime = i2['tau_prime']
				C_bars.append(C_bar1)	




			if i2['Name'] == 'DVP3' and i2['phaseID'] == phaseID:



				if (server == 2):	

					#print(i2)

					if i2['src'] == 'CloudServer1':

						

						Newdata = i2

						sigma_Qt = Newdata['sigma_Qt']
						#print(sigma_Qt)


				else:

					if i2['src'] == 'CloudServer2':

						Newdata = i2

						sigma_Qt = Newdata['sigma_Qt']



			if i2['Name'] == 'Reconstruction2' and i2['phaseID'] == phaseID:

				tau =  i2['Tau']
				#tau = [int(j) for j in tau.split(",")]
				y_til = int(tau[0])

				#print(tau)
	


	#VerifyQt


	e_hashQt = sigma_Qt[0]
	e_Qt = (int.from_bytes(bytes.fromhex(e_hashQt), byteorder='big'))% q
	eQt_minus = (0 - e_Qt)% q

	z1_Qt = sigma_Qt[1]
	z2_Qt = sigma_Qt[2]

	R1 = sigma_Qs[3]
	C1 = sigma_Qs[4]

	'''

	R_PrimeQt  = [(pow(h, z2_Qt, p)* pow(h_prime, z1_Qt, p) *  pow(R1[0], eQt_minus, p))%p, (pow(g, z2_Qt, p)*pow(R1[1],eQt_minus, p))%p]

	W_bar = (pow(g_bar, z1_Qt, p)* pow(CS_bar, eQt_minus, p))%p

	W = (pow(g, z1_Qt, p)* pow(C1, eQt_minus, p))%p
	'''

	proc = Popen(VerifyQt, stdin=PIPE, stdout=PIPE)

	out, err = proc.communicate(input= p.encode()+b'\n'+g.encode()+b'\n'+g_bar.encode()+b'\n'+h.encode()+b'\n'+h_prime.encode() +b'\n'+str(eQt_minus).encode()+b'\n'+z1_Qt.encode()+b'\n'+z2_Qt.encode()+b'\n'+C1.encode()+b'\n'+CS_bar.encode()+b'\n'+R1[0].encode()+b'\n'+R1[1].encode())

	BV_prime = out.decode().strip() #strip removes \n at the end of the string  

	j = BV_prime.split(",")

	m = [ i for i in j]


	R_PrimeQt = [m[0], m[1]]
	W_bar = m[2]
	W = m[3]


	HashQt_Values = [server] + tau_prime + [g_bar] +[CS_bar]+[C1]+R1+[W_bar]+[W]+R_PrimeQt

	
	hashQt_verify = hashlib.sha256(str.encode(str(HashQt_Values))).hexdigest()



	#print(e_hashQt, hashQt_verify)
	#print(HashQt_Values, tau_prime	)	

	if (e_hashQt == hashQt_verify):	


		'''

		#print(C_bars)
		result1 = numpy.prod(C_bars) % p
		#print(y_bar, result1 )



		if  y_bar == result1:



			y1_til = pow(y_til, x1_prime, p)

			#tau = [tau_0, tau_1, tau_2]

			lst = OnlineServers + tau 	
			lst.append(y1_til)	

			key = sum(lst) % p

			if (key == 0):

				key_inv = 1


			else:	

				key_inv = mod_inverse(key, p)
			#key = hash(str(lst)) % Zq #hash returns a different value everytime.

			#print(key)	

			
			EncShare = key_inv * share_pr % p

			EShare = [shareID_pr, EncShare]

			'''



		proc = Popen(SessionKey, stdin=PIPE, stdout=PIPE)

		out, err = proc.communicate(input= p.encode()+b'\n'+str(y_til).encode()+b'\n'+str(y_bar).encode()+b'\n'+str(x1_prime).encode()+b'\n'+str(share_pr).encode()+b'\n'+str(OnlineServers[0]).encode() +b'\n'+ str(OnlineServers[1]).encode()+b'\n'+str(tau[0]).encode()+b'\n'+str(tau[1]).encode()+b'\n'+str(tau[2]).encode()+b'\n'+str(C_bars[0]).encode()+b'\n'+str(C_bars[1]).encode())

		EncShare = out.decode().strip() #strip removes \n at the end of the string  

		totalS4 = datetime.now() - startS4	

		#print(EShare)

		'''
		write to user's messages
		'''

		
		Userdata = {'Name':'Reconstruction3','src': 'HomeServer', 'dst':'User','EShare': EncShare,  'phaseID': phaseID, 'sessionID': sessionID}

		
		with open('../Database/userMessages.json', 'w') as outfile:
			json.dump(Userdata, outfile)


		

	else:

		Userdata = {'Name':'Error Message','src': 'HomeServer', 'dst':'User','Message': 'S4_Proof Failed!', 'phaseID': phaseID,'sessionID': sessionID}

		
		with open('../Database/userMessages.json', 'w') as outfile:
			json.dump(Userdata, outfile)	
		print("Protocol aborted!")	


	
	return totalS4




if __name__ == '__main__':
		Step4(OnlineServers, phaseID)	