from ctypes import *
from subprocess import *

import sympy as ss
file = "/Applications/XAMPP/htdocs/LocalServer/codes/Generator.so"

#my_functions = CDLL(file)

#print(type(my_functions))

lis_Values = ["23","3", "4"]

#l = lis_Values[0].encode +b'\n'+bytes(lis_Values[1])+b'\n'+bytes(lis_Values[2])

#print(b'23\n3\n4')

#for i in lis_Values:
proc = Popen(file, stdin=PIPE, stdout=PIPE)
#out,err = proc.communicate(input=i)

out, err = proc.communicate(input= lis_Values[0].encode()+b'\n'+lis_Values[1].encode()+b'\n'+lis_Values[2].encode())

print(out.decode())


#print(my_functions.main())


#p = 3542660321

#p= 2767

#a = p-1

#b = a//6

#print([ss.isprime(b), b])

p = 16603
q = 2767
g = 29

y= 3984
h = 4890

alpha = 446
Ec =[1744,8188]

B = [13637, 15625]

V =  [13740, 9084]



z1 = 274
z2= 293
z3 = 399




mu1 = 2297
mu2 = 965 
v = 809
h = 4890
beta = 18
gamma = 481
pi = 73


e = 1886
#e_minus = (0 - e) % q 

#cz1 = [((e*beta)+mu1) %(p-1), ((e*pi)+mu2) %(p-1) , ((e*gamma)+v) %(p-1)  ]
			
#B_prime = [(pow(y, (e*beta)+mu1, p)* pow(Ec[0], (e*pi)+mu2, p)*pow(B[0]*g %p , e_minus, p))%p, pow(g, (e*beta)+mu1, p)* (pow(Ec[1], (e*pi)+mu2, p)*pow(B[1], e_minus, p))%p]
#V_prime = [(pow(h, (e*gamma)+v, p)*pow(g, (e*pi)+mu2, p)*pow(V[0], e_minus, p))%p, (pow(g, (e*gamma)+v, p)*pow(V[1], e_minus, p))%p]



#B1_prime = [(pow(y, mu1, p)* pow(Ec[0], mu2, p))%p, pow(g, mu1, p)* (pow(Ec[1], mu2, p))%p]

#V1_prime = [(pow(h, v, p)*pow(g, mu2, p))%p, (pow(g, v, p))%p]



#print(B_prime,V_prime)
#print(B1_prime, V1_prime)

#print(cz1)

#print([pow(g, cz1[0], p), pow(g, z1, p)], [pow(g, cz1[1], p), pow(g, z2, p)], [pow(g, cz1[2], p), pow(g, z3, p)])

#print(ss.isprime(3413))

aim = 16603


#zipm = (16603*4)+1

#print(ss.isprime(zipm), zipm)

#h_prime = [(pow(g, mu1, p)* pow(g, mu2, p))%p, pow(g, mu1+mu2, p)]

#print(h_prime)


	


#q = 23

t = 113
n = 113


s = set(range(1, n))
results = []
for a in range(1,t):
	g = set()
	for x in s:
		g.add((a**x) % n)
		if g == s:
			results.append(a)
print(results)


'''
s = set(range(1, n))
results = []
for a in range(1,n):
	g = set()
	
	g.add((47**a) % n)
	
if g == s:
	print(True)
else:
	print(False)	
'''


#print("results")

'''
gen = []
lis=[]
mim = [i for i in range(1,q)]

for i in range(1,p):

	#for a in range(1,q):


	a = pow(29, i, p)
	
	lis.append(a)

	lis.sort()

	if (lis == mim):

		#gen.append(a)	
		print(lis)				
'''
'''
a = []
b= []
c =[]
d = []
for i in range(1,n):

	b.append(6**i%n)
	b.sort()

	c.append(7**i%n)
	c.sort()

	d.append(8**i%n)
	d.sort()

print(b,c,d)	

'''

