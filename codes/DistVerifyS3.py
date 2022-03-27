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

from random import randint
from datetime import datetime, date

import hashlib


from ctypes import *
from subprocess import *

import time
import Condition as cond


print("Content-type: text/html\r \n")

VerifyQs = "/Applications/XAMPP/htdocs/LocalServer/codes/VerifyQs.o"
ProofQt = "/Applications/XAMPP/htdocs/LocalServer/codes/ProofQt.o"
ProofQt_i = "/Applications/XAMPP/htdocs/LocalServer/codes/ProofQt_i.o"


phaseID = sys.argv[1]
OnlineServers = [int(sys.argv[2]), int(sys.argv[3])]


def Step3(OnlineServers, phaseID):


	today = date.today()
	now = datetime.now()
	sessionID = today.strftime("%Y%m%d")+ now.strftime("%H%M%S") +''.join(["{}".format(randint(0, 9)) for num in range(0, 5)]) 

	
	f = open('../Database/SetUp.json', "r")

	#data = json.load(f)

	data = [json.loads(line) for line in f]

	for i in data:

		if i['Name'] == 'Step1-setup' and i['src'] == 'User':

			p = i['p']
			q = int(i['q'])
			h = i['h']
			h_prime = i['h_prime']
			g = i['g']
			y = i['y']


			share_x = i['share_x']
			ID = int(share_x[0])
			x1 = share_x[1]	



	for iz in OnlineServers:

		if (iz!=ID):
			server = iz



	
	if server == 2:
		server_name = "CloudServer1"
	else:
		server_name = "CloudServer2"				



	#f = open('../Database/Recon.json', "r")
	#data = [json.loads(line) for line in f]	


	file_str = '../Database/Recon.json'	


	data = cond.fileCondition(file_str)


	#check whether the other server has completed	

	result = cond.DataExists(data, "DVP2", phaseID, server_name)

	#print(result)

	

	i = 0

	while result != True:

		time.sleep(0.1)

		data = cond.fileCondition(file_str)

		result = cond.DataExists(data, "DVP2", phaseID, server_name)

		i = i+1
		print(f'Tried {i} times')

	

	
	if result == True:	

		startS3 =datetime.now()	


	

		for i in data:

			if i['Name'] == 'Reconstruction2' and i['phaseID'] == phaseID:

				B = i['B']	
				#B = [int(B[0]), int(B[1])]

				V = i['V']
				#V = [int(V[0]), int(V[1])]

				tau = i['Tau']

				#print(tau)


			if i['Name'] == 'DVP2' and i['phaseID'] == phaseID:

				if (server == 2):	

					if i['src'] == 'CloudServer1':

						Newdata = i

						sigma_Qs = Newdata['sigma_Qs']
						#proofQs_values = Newdata['proofQs_values']

						

				else:

					if i['src'] == 'CloudServer2':

						Newdata = i

						sigma_Qs = Newdata['sigma_Qs']


			if i['Name'] == 'DVP1' and i['phaseID'] == phaseID:

				if (server == 2):	

					if i['src'] == 'CloudServer1':

						Newdata = i


						BS = Newdata['B2']
						VS = Newdata['V2']
						

				else:

					if i['src'] == 'CloudServer2':

						Newdata = i

						BS = Newdata['B3']	
						VS = Newdata['V3']

			if i['Name'] == 'DVP2' and i['phaseID'] == phaseID and i['src'] == 'HomeServer':	
			
				g_bar = i['g_bar'] 

				C_bar = i['C_bar1']

				delta = i['delta']

				a1 = i['a1']

				sigma_Qst = i['sigma_Qs']

				C1_Qt = sigma_Qst[4]
				R1_Qt = sigma_Qst[3]

				tau_prime = i['tau_prime']
			
					

	
	#verifyQs	

	hashQs = sigma_Qs[0]
	QsZ1 = 	sigma_Qs[1]
	QsZ2 = sigma_Qs[2]
	R1_Qs  = sigma_Qs[3]
	C1_Qs  = sigma_Qs[4]


	e_Qs = (int.from_bytes(bytes.fromhex(hashQs), byteorder='big'))% q
	Qs_eMinus = (0 - e_Qs)%q


	'''
	R_primeQs = [(pow(h, QsZ2, p)* pow(h_prime, QsZ1, p)*pow(R1_Qs[0], Qs_eMinus, p) )%p, (pow(g, QsZ2, p)*pow( R1_Qs[1], Qs_eMinus,p))%p]
	W_Qs = (pow(g, QsZ1, p)* pow(C1_Qs, Qs_eMinus, p))%p
	'''

	proc = Popen(VerifyQs, stdin=PIPE, stdout=PIPE)

	out, err = proc.communicate(input= p.encode()+b'\n'+g.encode()+b'\n'+h.encode()+b'\n'+h_prime.encode() +b'\n'+str(Qs_eMinus).encode()+b'\n'+QsZ1.encode()+b'\n'+QsZ2.encode()+b'\n'+C1_Qs.encode()+b'\n'+R1_Qs[0].encode()+b'\n'+R1_Qs[1].encode())

	BV_prime = out.decode().strip() #strip removes \n at the end of the string  

	j = BV_prime.split(",")

	m = [ i for i in j]


	R_primeQs = [m[0], m[1]]
	W_Qs = m[2]
	
	
	hashQs_values = [server]+tau_prime+ [g_bar] +[C1_Qs]+R1_Qs+[W_Qs]+R_primeQs

	#print(len(hashQs_values))

	hashQs_verify = hashlib.sha256(str.encode(str(hashQs_values))).hexdigest()		

	#print("VerifyQs:")
	#print(hashQs_verify, hashQs)
	#print(hashQs_values)


	if (hashQs_verify == hashQs):
		
		#proofQt

		mu = random.randrange(1, q)	
		v = random.randrange(1, q)
		

		mu = mu
		v = v
		

		'''
		W_Qt = pow(g, mu, p)
		W_bar = pow(g_bar,mu,p)

		R_primeQt = [(pow(h, v, p)* pow(h_prime, mu, p))%p, pow(g, v, p)]

		'''


		proc = Popen(ProofQt, stdin=PIPE, stdout=PIPE)

		out, err = proc.communicate(input= p.encode()+b'\n'+g.encode()+b'\n'+str(g_bar).encode()+b'\n'+h.encode()+b'\n'+h_prime.encode() +b'\n'+str(mu).encode()+b'\n'+str(v).encode())

		BV_prime = out.decode().strip() #strip removes \n at the end of the string  

		j = BV_prime.split(",")

		m = [ i for i in j]


		R_primeQt = [m[0], m[1]]
		W_Qt = m[2]
		W_bar =m[3]


		hashQt_values=[ID] + tau_prime +[g_bar]+[C_bar]+[C1_Qt]+R1_Qt+[W_bar]+[W_Qt]+R_primeQt

		#print(hashQt_values)

		e_hashQt = hashlib.sha256(str.encode(str(hashQt_values))).hexdigest()

		e_Qt = (int.from_bytes(bytes.fromhex(e_hashQt), byteorder='big'))% q


		'''
		QtZ1 = (a1*e_Qt + mu)%q
		QtZ2 = (delta*e_Qt + v)%q
		'''


		proc = Popen(ProofQt_i, stdin=PIPE, stdout=PIPE)

		out, err = proc.communicate(input= str(q).encode()+b'\n'+str(a1).encode()+b'\n'+str(delta).encode()+b'\n'+str(e_Qt).encode()+b'\n'+str(mu).encode() +b'\n'+str(v).encode())

		BV_prime = out.decode().strip() #strip removes \n at the end of the string  

		j = BV_prime.split(",")

		m = [ i for i in j]


		
		QtZ1  = m[0]
		QtZ2 =m[1]


		
		sigma_Qt = [e_hashQt, QtZ1, QtZ2]

		totalS3 = datetime.now() - startS3


		f = open('/Applications/XAMPP/htdocs/LocalServer/codes/config.json', "r")
		servers  = json.load(f)

		#for k in servers:

		if(server==2):
			dst = "CloudServer1"
			url = servers['CloudServer1']
		else:
			dst = "CloudServer2"
			url = servers['CloudServer2']  		


		headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json'}


		session = requests.Session() 

		myobj = {'Name':'DVP3','src': 'HomeServer', 'dst': dst, 'sigma_Qt': sigma_Qt,'phaseID': phaseID, 'sessionID': sessionID }

		session.post(url, json = myobj, headers=headers, verify=False)

	else:

		Userdata = {'Name':'Error Message','src': 'HomeServer', 'dst':'User','Message': 'S3_Proof Failed!', 'phaseID': phaseID,'sessionID': sessionID}

		
		with open('../Database/userMessages.json', 'w') as outfile:
			json.dump(Userdata, outfile)	
		print("Protocol Aborted!")		


	
	return totalS3

	

if __name__ == '__main__':
	Step3(OnlineServers, phaseID)




		
