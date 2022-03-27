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

import hashlib

from ctypes import *
from subprocess import *




print("Content-type: text/html\r \n")


def fileCondition(file_str):

	f = open(file_str, "r")

	data = [json.loads(line) for line in f]


	return data

	f.close()


def DataExists(data, name, phaseID, server_name):

	#new_i['src'] != 'HomeServer'


		
	for i in data:
	


		if i['Name'] == name and i['phaseID'] == phaseID and i['src'] == server_name:

			new_i = i

			return bool(new_i)

			'''
			if new_i != {}:

				return True 

			else:

				return False 
			'''		

if __name__ == '__main__':

				fileCondition(file_name)
				DataExists(data, name, phaseID, server_name)

			