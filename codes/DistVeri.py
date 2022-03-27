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
import time
import sys
from datetime import datetime

import hashlib
import csv

import DistVerifyS1 as Ds1
import DistVerifyS2 as Ds2
import DistVerifyS3 as Ds3
import DistVerifyS4 as Ds4

print("Content-type: text/html\r \n")


phaseID = sys.argv[1]
OnlineServers = [int(sys.argv[2]), int(sys.argv[3])]
#OnlineServers = sys.argv[2]

def DistVeri():

	
	
	totalS1 = Ds1.Step1(OnlineServers, phaseID)

	#time.sleep(0.01)

	totalS2 = Ds2.Step2(OnlineServers, phaseID)
	
	

	#time.sleep(0.01)

	totalS3 = Ds3.Step3(OnlineServers, phaseID)
	


	#time.sleep(0.1)

	totalS4 = Ds4.Step4(OnlineServers, phaseID)
	
	

	data = totalS1, totalS2, totalS3, totalS4

	print([totalS1, totalS2, totalS3, totalS4])


	with open('/Applications/XAMPP/htdocs/LocalServer/Database/time.csv', 'a+', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)

		# write the header
		#writer.writerow(header)

		# write the data
		writer.writerow(data)


if __name__ == '__main__':

	

	DistVeri()

	