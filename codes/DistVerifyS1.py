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
from random import randint
from datetime import datetime, date

import sys
import time

import hashlib

from ctypes import *
from subprocess import *


print("Content-type: text/html\r \n")


DistS1 = "/Applications/XAMPP/htdocs/LocalServer/codes/DistS1.o"
DistS1_i = "/Applications/XAMPP/htdocs/LocalServer/codes/DistS1_i.o"
ProofQr = "/Applications/XAMPP/htdocs/LocalServer/codes/ProofQr.o"
ProofQr_i = "/Applications/XAMPP/htdocs/LocalServer/codes/ProofQr_i.o"



phaseID = sys.argv[1]
OnlineServers = [int(sys.argv[2]), int(sys.argv[3])]


def Step1(OnlineServers, phaseID):


	today = date.today()
	now = datetime.now()
	sessionID = today.strftime("%Y%m%d")+ now.strftime("%H%M%S") +''.join(["{}".format(randint(0, 9)) for num in range(0, 5)]) 

	# read values sent by user

	f = open('../Database/SetUp.json', "r")
	
	#data = json.load(f)

	data = [json.loads(line) for line in f]

	
	for i in data:

		if i['Name'] == 'Step1-setup' and i['src'] == 'User':

			p = i['p']
			q = int(i['q'])
			g = i['g']
			y = i['y']
			h = i['h']

			share_x = i['share_x']
			ID = int(share_x[0])

		if i['Name'] == 'Step2-setup' and i['src'] == 'User':
			Ec = i['Ec']
			#Ec = [int(Ec[0]), int(Ec[1])]



	ff = open('../Database/Recon.json', "r")
	
	#data = json.load(f)

	dataf = [json.loads(line) for line in ff]

	for ii in dataf:


		if ii['Name'] == 'Reconstruction2' and ii['phaseID'] == phaseID:

			B = ii['B']	
			#B = [int(j) for j in B.split(",")]
			#B_0 = int(B[0])
			#B_1 = int(B[1])

			

			
			V = ii['V']
			#V = [int(j) for j in V.split(",")]
			#V_0 = int(V[0])
			#V_1 = int(V[1])

			tau = ii['Tau']

			Sigma = ii['Sigma']

			e_hash = Sigma[0]

			#e = int(Sigma[1])
			z1 = Sigma[2]
			z2 = Sigma[3]
			z3 = Sigma[4]


	startS1 =datetime.now()

	#verify user's proof
	#print (type(Ec[0]))

	e = (int.from_bytes(bytes.fromhex(e_hash), byteorder='big'))% int(q)

	e_minus = (0 - e) % int(q) 


	proc = Popen(DistS1, stdin=PIPE, stdout=PIPE)
	out, err = proc.communicate(input= p.encode()+b'\n'+g.encode()+b'\n'+y.encode()+b'\n'+h.encode() +b'\n'+z1.encode()+b'\n'+z2.encode()+b'\n'+z3.encode()+b'\n'+str(e_minus).encode()+b'\n'+B[0].encode()+b'\n'+B[1].encode()+b'\n'+V[0].encode()+b'\n'+V[1].encode()+b'\n'+Ec[0].encode()+b'\n'+Ec[1].encode())

	BV_prime = out.decode().strip() #strip removes \n at the end of the string  

	j = BV_prime.split(",")

	m = [ i for i in j]


	B_prime = [m[0], m[1]]
	V_prime = [m[2], m[3]]
	

	

			
	#B_prime = [(pow(y, z1, p)* pow(Ec[0], z2, p)*pow(B_0*g %p , e_minus, p))%p, pow(g, z1, p)* (pow(Ec[1], z2, p)*pow(B_1, e_minus, p))%p]
	#V_prime = [(pow(h, z3, p)*pow(g, z2, p)*pow(V_0, e_minus, p))%p, (pow(g, z3, p)*pow(V_1, e_minus, p))%p]

	
	#The user app hashes these values as BigIntegers thus the conversion to int.
	e_values = [int(tau[0]), int(tau[1]), int(tau[2])]+[int(Ec[0]), int(Ec[1])]+[int(B[0]), int(B[1])]+[int(V[0]), int(V[1])]+[int(B_prime[0]), int(B_prime[1])]+[int(V_prime[0]), int(V_prime[1])]

	e_string = str(e_values)

	hassh= hashlib.sha256(str.encode(e_string)).hexdigest()

	#hassh= hashlib.sha256(b"[17, 1, 28, 20, 19, 1, 1, 55, 53, 46, 49, 48, 57]").hexdigest()

	#print(e_hash, hassh)
	#print (Sigma[5])
	#print(e_values)



	#print (e_values, Sigma[6], Sigma[5], Sigma)
	
	if(e_hash == hassh):



		#Generate random values and store them 
			
		r1 = random.randrange(1, q)	
		r1_prime = random.randrange(1, q)
		gamma1 = random.randrange(1, q)
		gamma1_prime = random.randrange(1, q)
		gamma1_primePrime = random.randrange(1, q)
		

		r1 = r1	
		r1_prime = r1_prime
		gamma1 = gamma1
		gamma1_prime = gamma1_prime
		gamma1_primePrime = gamma1_primePrime

		#print("r1, r1_prime:")
		#print(r1, r1_prime)



		proc = Popen(DistS1_i, stdin=PIPE, stdout=PIPE)
		out, err = proc.communicate(input= p.encode()+b'\n'+g.encode()+b'\n'+y.encode()+b'\n'+h.encode() +b'\n'+str(r1).encode()+b'\n'+str(r1_prime).encode()+b'\n'+str(gamma1).encode()+b'\n'+str(gamma1_prime).encode()+b'\n'+str(gamma1_primePrime).encode()+b'\n'+B[0].encode()+b'\n'+B[1].encode()+b'\n'+V[0].encode()+b'\n'+V[1].encode())

		BV_prime = out.decode().strip() #strip removes \n at the end of the string  

		j = BV_prime.split(",")

		m = [ i for i in j]


		B1 = [str(m[0]), str(m[1])]
		V1 = [str(m[2]), str(m[3])]
		V1_prime= [str(m[4]), str(m[5])]
		V1_primeprime= [str(m[6]), str(m[7])]


		#B1 = [pow(B_0, r1, p)* pow(y , r1_prime, p) % p, pow(B_1, r1, p)* pow(g , r1_prime, p) % p]
		#V1 = [pow(h, gamma1)*pow(g, r1) % p, pow(g, gamma1, p) ]
		#V1_prime = [pow(h, gamma1_prime)*pow(V_0, r1) % p, pow(g, gamma1_prime, p)]
		#V1_primeprime = [pow(h, gamma1_primePrime)*pow(V_1, r1) % p, pow(g, gamma1_primePrime, p)]

		#print(B1)

		
		
		#Broadcast B1, V1, V1_prime, V1_primeprime to the servers online.
		#For this case i assume only homeserver and cloud1 are online
		

		#url = {'http://40.117.176.226/CloudServer1/PostProcess/PostProcess.php', "http://40.76.203.48/CloudServer2/PostProcess/PostProcess.php" }



		#proofQr
		mu1 = random.randrange(1, q)	
		mu2 = random.randrange(1, q)
		v1 = random.randrange(1, q)
		v2 = random.randrange(1, q)
		v3 = random.randrange(1, q)
		

		mu1 = mu1	
		mu2 = mu2
		v1 = v1
		v2 = v2
		v3 = v3



		proc = Popen(ProofQr, stdin=PIPE, stdout=PIPE)
		out, err = proc.communicate(input= p.encode()+b'\n'+g.encode()+b'\n'+y.encode()+b'\n'+h.encode() +b'\n'+B[0].encode()+b'\n'+B[1].encode()+b'\n'+V[0].encode()+b'\n'+V[1].encode()+b'\n'+str(mu1).encode()+b'\n'+str(mu2).encode()+b'\n'+str(v1).encode()+b'\n'+str(v2).encode()+b'\n'+str(v3).encode())

		BV_prime = out.decode().strip() #strip removes \n at the end of the string  

		j = BV_prime.split(",")

		m = [ i for i in j]


		B_bar = [m[0], m[1]]
		V_bar = [m[2], m[3]]
		V_barPrime= [m[4], m[5]]
		V_barPrimePrime= [m[6], m[7]]


		'''
		B_bar = [pow(B_0, mu1, p)* pow(y , mu2, p) % p, pow(B_1, mu1, p)* pow(g , mu2, p) % p]
		V_bar = [pow(h, v1, p)* pow(g , mu1, p) % p, pow(g, v1, p)]
		V_barPrime = [pow(h, v2, p)* pow(V_0 , mu1, p) % p, pow(g, v2, p)]
		V_barPrimePrime = [pow(h, v3, p)* pow(V_1 , mu1, p) % p, pow(g, v3, p)]
		'''


		serv_values = [ID]+B+V+B1+V1+V1_prime+V1_primeprime+B_bar+V_bar+V_barPrime+V_barPrimePrime

		serv_string = str(serv_values)

		serv_hash= hashlib.sha256(str.encode(serv_string)).hexdigest()

		serv_e = (int.from_bytes(bytes.fromhex(serv_hash), byteorder='big'))% q

		
		'''
		sz1 = (r1*serv_e + mu1) % q
		sz2 = (r1_prime*serv_e + mu2) % q
		sz3 = (gamma1*serv_e + v1) % q
		sz4 = (gamma1_prime*serv_e + v2) % q
		sz5 = (gamma1_primePrime*serv_e + v3) % q
		'''

		proc = Popen(ProofQr_i, stdin=PIPE, stdout=PIPE)
		out, err = proc.communicate(input= str(q).encode()+b'\n'+str(serv_e).encode()+b'\n'+str(r1).encode()+b'\n'+str(r1_prime).encode() +b'\n'+str(gamma1).encode()+b'\n'+str(gamma1_prime).encode()+b'\n'+str(gamma1_primePrime).encode()+b'\n'+str(mu1).encode()+b'\n'+str(mu2).encode()+b'\n'+str(v1).encode()+b'\n'+str(v2).encode()+b'\n'+str(v3).encode())

		BV_prime = out.decode().strip() #strip removes \n at the end of the string  

		j = BV_prime.split(",")

		m = [ i for i in j]


		sz1 = m[0]
		sz2 = m[1]
		sz3 = m[2]
		sz4=  m[3]
		sz5=  m[4]
		

		serv_sigma = [serv_hash,sz1,sz2,sz3,sz4,sz5]

		totalS1 = datetime.now() - startS1	

		#print(serv_sigma)


		for i in OnlineServers:

			if (i!=ID):
				server = i


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

		myobj = {'Name':'DVP1','src': 'HomeServer', 'dst': dst, 'serv_sigma':serv_sigma,'B1': B1, 'V1': V1,'V1_prime': V1_prime, 'V1_primeprime': V1_primeprime, 'phaseID':phaseID, 'sessionID': sessionID}
			
		session.post(url, json = myobj, headers=headers,verify=False)

		
				


		data = {'Name':'DVP1', 'src': 'HomeServer', 'dst': 'HomeServer','B1': B1, 'V1': V1,'V1_prime': V1_prime, 'V1_primeprime': V1_primeprime, 'phaseID':phaseID, 'sessionID' : sessionID}

		f = open('../Database/Recon.json', 'a') 
		f.write(json.dumps(data)+ "\n")

	else:
	

		Userdata = {'Name':'Reconstruction3','src': 'HomeServer', 'dst':'User','Message': 'M', 'EShare': "Wrong Password!", 'phaseID': phaseID,'sessionID': sessionID}

		
		with open('../Database/userMessages.json', 'w') as outfile:
			json.dump(Userdata, outfile)	

		print("Protocol Aborted!")		


	
	return totalS1
			


if __name__ == '__main__':
	Step1(OnlineServers, phaseID)

