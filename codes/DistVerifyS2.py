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

VerifyQr = "/Applications/XAMPP/htdocs/LocalServer/codes/VerifyQr.o"

Lagrange = "/Applications/XAMPP/htdocs/LocalServer/codes/Lagrange.o"

ProofQs = "/Applications/XAMPP/htdocs/LocalServer/codes/ProofQs.o"

ProofQs_i = "/Applications/XAMPP/htdocs/LocalServer/codes/ProofQs_i.o"



phaseID = sys.argv[1]
OnlineServers = [int(sys.argv[2]), int(sys.argv[3])]

def Step2(OnlineServers, phaseID):


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

		if i['Name'] == 'Step1-setup' and i['src'] == 'HomeServer':	

			y_i = i['y']



	
	
	#Read Bi, Vi  from file

	for iz in OnlineServers:

		if (iz!=ID):
			server = iz


	file_str = '../Database/Recon.json'	


	#f = open('../Database/Recon.json', "r")
	#data = [json.loads(line) for line in f]	

	data = cond.fileCondition(file_str)


	#check whether the other server has completed

	if server == 2:
		server_name = "CloudServer1"
	else:
		server_name = "CloudServer2"	

	result = cond.DataExists(data, "DVP1", phaseID, server_name)

	#print(result)

	

	i = 0

	while result != True:

		time.sleep(0.1)

		data = cond.fileCondition(file_str)

		result = cond.DataExists(data, "DVP1", phaseID, server_name)

		i = i+1
		print(f'Tried {i} times')

		

	
	if result == True:	

		startS2 =datetime.now()	

		for i in data:

			if i['Name'] == 'DVP1' and i['phaseID'] == phaseID:

				if (server == 2):	

					if i['src'] == 'CloudServer1':

						Newdata = i


						BS = Newdata['B2']
						VS = Newdata['V2']
						VS_Prime = Newdata['V2_prime']
						VS_PrimePrime = Newdata['V2_primeprime']

						serv_sigma = Newdata['serv_sigma']

						

				else:

					if i['src'] == 'CloudServer2':

						Newdata = i

						BS = Newdata['B3']	
						VS = Newdata['V3']
						VS_Prime = Newdata['V3_prime']
						VS_PrimePrime = Newdata['V3_primeprime']

						serv_sigma = Newdata['serv_sigma']


			if i['Name'] == 'DVP1' and i['phaseID'] == phaseID and i['src'] == 'HomeServer':	

				B1 = i['B1']
				V1 = i['V1']


			if i['Name'] == 'Reconstruction2' and i['phaseID'] == phaseID:

				B = i['B']	
				#B = [int(B[0]), int(B[1])]

				V = i['V']
				#V = [int(V[0]), int(V[1])]

				tau = i['Tau']


			
	#verify ProofQr

	#print("BS:")
	#print(BS)

	e = (int.from_bytes(bytes.fromhex(serv_sigma[0]), byteorder='big'))% q

	e_minus = (0 - e) % q 

	sz1 = serv_sigma[1]
	sz2 = serv_sigma[2]
	sz3 = serv_sigma[3]
	sz4 = serv_sigma[4]
	sz5 = serv_sigma[5]

	'''
	B_bar = [(pow(B[0], sz1, p)* pow(y, sz2, p)*pow(BS[0], e_minus, p))%p, (pow(B[1], sz1, p)* pow(g, sz2, p)*pow(BS[1], e_minus, p))%p]
	V_bar = [(pow(h, sz3, p)* pow(g, sz1, p)*pow(VS[0], e_minus, p))%p, (pow(g, sz3, p)*pow(VS[1], e_minus, p))%p]
	V_barPrime = [(pow(h, sz4, p)* pow(V[0], sz1, p)*pow(VS_Prime[0], e_minus, p))%p, (pow(g, sz4, p)*pow(VS_Prime[1], e_minus, p))%p]
	V_barPrimePrime = [(pow(h, sz5, p)* pow(V[1], sz1, p)*pow(VS_PrimePrime[0], e_minus, p))%p, (pow(g, sz5, p)*pow(VS_PrimePrime[1], e_minus, p))%p]
	'''



	proc = Popen(VerifyQr, stdin=PIPE, stdout=PIPE)
	out, err = proc.communicate(input= p.encode()+b'\n'+g.encode()+b'\n'+y.encode()+b'\n'+h.encode() +b'\n'+sz1.encode()+b'\n'+sz2.encode()+b'\n'+sz3.encode()+b'\n'+sz4.encode()+b'\n'+sz5.encode()+b'\n'+str(e_minus).encode()+b'\n'+B[0].encode()+b'\n'+B[1].encode()+b'\n'+V[0].encode()+b'\n'+V[1].encode()+b'\n'+BS[0].encode()+b'\n'+BS[1].encode()+b'\n'+VS[0].encode()+b'\n'+VS[1].encode()+b'\n'+VS_Prime[0].encode()+b'\n'+VS_Prime[1].encode()+b'\n'+VS_PrimePrime[0].encode()+b'\n'+VS_PrimePrime[1].encode())

	BV_prime = out.decode().strip() #strip removes \n at the end of the string  

	j = BV_prime.split(",")

	m = [ i for i in j]


	B_bar = [m[0], m[1]]
	V_bar = [m[2], m[3]]
	V_barPrime = [m[4], m[5]]
	V_barPrimePrime = [m[6], m[7]]
	



	e_values = [server]+B+V+BS+VS+VS_Prime+VS_PrimePrime+B_bar+V_bar+V_barPrime+V_barPrimePrime

	e_string = str(e_values)

	hassh= hashlib.sha256(str.encode(e_string)).hexdigest()

	#print( e_values)

	#print(hassh, serv_sigma[0])



	if (hassh == serv_sigma[0]):

		'''
		multiply B2 and BS(from the other server)


		'''
		'''
		product = np.multiply(B1, BS) % p

		
		y_bar =  int(product[0])
		
		g_bar = int(product[1])


		prod = Decimal(1) 
		j = ID

		for i in OnlineServers:
			if i != j:
			
					prod *= ((0-i)%q * mod_inverse((j-i)% q, q))% q


		a1 = int(prod * x1 % (q))

		print('a1:')
		print( a1)
		print(y_bar, g_bar)

		C_bar1 = pow(g_bar, a1, p) 
		'''


		proc = Popen(Lagrange,  stdin=PIPE, stdout=PIPE)
		out, err = proc.communicate(input= p.encode()+b'\n'+str(q).encode()+b'\n'+str(ID).encode()+b'\n'+str(x1).encode() +b'\n'+str(B1[0]).encode()+b'\n'+str(B1[1]).encode()+b'\n'+str(BS[0]).encode()+b'\n'+str(BS[1]).encode()+b'\n'+str(OnlineServers[0]).encode()+b'\n'+str(OnlineServers[1]).encode())

		BV_prime = out.decode().strip() #strip removes \n at the end of the string  

		j = BV_prime.split(",")

		m = [ i for i in j]


		y_bar = m[0]
		C_bar1 = m[1]
		a1 = m[2]
		prod = m[3]
		g_bar = m[4]


		#print("a1:")
		#print(a1)


		

		#proofQs
		mu = random.randrange(1, q)	
		v = random.randrange(1, q)
		delta = random.randrange(1, q)

		mu = mu
		v = v
		delta = delta

		'''
		W = pow(g, mu, p)

		R_prime = [(pow(h, v, p)* pow(h_prime, mu, p))%p, pow(g, v, p)]

		R1 = [(pow(h, delta, p)* pow(h_prime, a1, p))%p, pow(g, delta, p)]

		C1 = pow(y_i, int(prod), p)
		

		print("mu v delta")
		print([mu,  v , delta])

		print("y_i, prod")
		print([y_i, prod])

		'''



		proc = Popen(ProofQs,  stdin=PIPE, stdout=PIPE)
		out, err = proc.communicate(input= p.encode()+b'\n'+g.encode()+b'\n'+h.encode()+b'\n'+h_prime.encode() +b'\n'+a1.encode()+b'\n'+prod.encode()+b'\n'+y_i.encode()+b'\n'+str(mu).encode()+b'\n'+str(v).encode()+b'\n'+str(delta).encode())

		BV_prime = out.decode().strip() #strip removes \n at the end of the string  

		j = BV_prime.split(",")

		m = [ i for i in j]


		W = m[0]
		R_prime  = [m[1],m[2]]
		R1 = [m[3], m[4]]
		C1 = m[5]



		tau_prime = tau+B+V+B1+BS+V1+VS

		#print(len(tau_prime))

		#print("tau_prime:")
		#print(B1,BS)



		proofQs_values = [ID]+tau_prime+[g_bar]+[C1]+R1+[W]+R_prime

		#print("C1  W")

		#print([C1, W ])

		#print(len(proofQs_values))

		#print(proofQs_values)

		hashQs = hashlib.sha256(str.encode(str(proofQs_values))).hexdigest()

		e_Qs = (int.from_bytes(bytes.fromhex(hashQs), byteorder='big'))% q

		#print("e_Qs")
		#print(e_Qs)



		'''
		QsZ1 = (a1*e_Qs + mu)%q
		QsZ2 = (delta*e_Qs + v)%q
		'''


		proc = Popen(ProofQs_i,  stdin=PIPE, stdout=PIPE)
		out, err = proc.communicate(input=str(q).encode()+b'\n'+str(e_Qs).encode()+b'\n'+str(a1).encode() +b'\n'+str(mu).encode()+b'\n'+str(v).encode()+b'\n'+str(delta).encode())

		BV_prime = out.decode().strip() #strip removes \n at the end of the string  

		j = BV_prime.split(",")

		m = [ i for i in j]


		QsZ1 = m[0]
		QsZ2  = m[1]
		



		sigma_Qs = [hashQs, QsZ1, QsZ2, R1, C1]

		totalS2 = datetime.now() - startS2	


		#print("QsZ1, QsZ2")
		#print([QsZ1, QsZ2])


		'''
		Broadcast C_bar to the servers online.
		
		'''

		#url= {'http://40.76.203.48/CloudServer2/PostProcess/PostProcess.php', 'http://40.117.176.226/CloudServer1/PostProcess/PostProcess.php' }
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

		myobj = {'Name':'DVP2','src': 'HomeServer', 'dst': dst, 'C_bar1': C_bar1, 'sigma_Qs': sigma_Qs,'phaseID': phaseID, 'sessionID': sessionID }

		session.post(url, json = myobj, headers=headers, verify=False)


		

		'''
		Write C_bar1 to personal file
		'''


		data = {'Name':'DVP2', 'src': 'HomeServer', 'dst': 'HomeServer','tau_prime': tau_prime, 'C_bar1': C_bar1, 'y_bar': y_bar, 'sigma_Qs': sigma_Qs,'g_bar': g_bar, 'delta': delta, 'a1':a1, 'phaseID':phaseID, 'sessionID': sessionID}

		
		f = open('../Database/Recon.json', 'a') 
		f.write(json.dumps(data)+ "\n")

	else:

		Userdata = {'Name':'Error Message','src': 'HomeServer', 'dst':'User','Message': 'S2_Proof Failed!', 'phaseID': phaseID,'sessionID': sessionID}

		
		with open('../Database/userMessages.json', 'w') as outfile:
			json.dump(Userdata, outfile)	

		print("Protocol Aborted!")	


		
	

	return totalS2
	

if __name__ == '__main__':
	Step2(OnlineServers, phaseID)
