#include <NTL/ZZ.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>


#include<array>
//#include "cryptlib.h"
//#include "sha.h"


//using namespace CryptoPP;

using namespace std;
using namespace NTL;



 
std::array<ZZ, 4> witness(ZZ p, ZZ g, ZZ g_bar, ZZ h, ZZ h_prime, ZZ mu, ZZ v)
{
  

 // NTL::SetSeed(conv<ZZ>((long) time(0)));
  std::array<ZZ, 4> result;

  

  ///ZZ mu1_i = RandomBnd(q); // random number between 0 and q-1


   
    ZZ W_Qt = PowerMod(g, mu, p);
    ZZ W_bar = PowerMod(g_bar,mu,p);

    ZZ R_primeQt [] = {(PowerMod(h, v, p)* PowerMod(h_prime, mu, p))%p, PowerMod(g, v, p)};


    result = {R_primeQt[0], R_primeQt[1], W_Qt, W_bar};


  return result;
}


  




int main()

{

	ZZ p,g,g_bar,h,h_prime, mu, v;

	std::array<ZZ,4> result;

	//ZZ result[4];
	 

	//ZZ n[] = {a,x,p};

	cin >> p; 
  cin >> g; 
  cin >> g_bar;
   	 
   	cin >> h;
    cin >> h_prime;
   
   cin >> mu; 
   	cin >> v; 
    
 


  

  result = witness(p,g,g_bar,h,h_prime, mu, v);


  for(int i=0;i<4;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
 

   
  
   	
   

   
}
