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



 
std::array<ZZ, 4> witness( ZZ p, ZZ g, ZZ g_bar, ZZ h, ZZ h_prime, ZZ eQt_eMinus, ZZ z1_Qt, ZZ z2_Qt, ZZ C1, ZZ CS_bar, ZZ R1_0, ZZ R1_1)
{
  

  //NTL::SetSeed(conv<ZZ>((long) time(0)));
  std::array<ZZ, 4> result;

  

  ///ZZ mu1_i = RandomBnd(q); // random number between 0 and q-1


   

  ZZ R_PrimeQt []  = {(PowerMod(h, z2_Qt, p)* PowerMod(h_prime, z1_Qt, p) *  PowerMod(R1_0, eQt_eMinus, p))%p, (PowerMod(g, z2_Qt, p)*PowerMod(R1_1,eQt_eMinus, p))%p};

  ZZ W_bar  = (PowerMod(g_bar, z1_Qt, p)* PowerMod(CS_bar, eQt_eMinus, p))%p;

  ZZ W  = (PowerMod(g, z1_Qt, p)* PowerMod(C1, eQt_eMinus, p))%p;

 result = {R_PrimeQt[0], R_PrimeQt[1], W_bar, W};


  return result;
}


  




int main()

{

	ZZ  p, g, g_bar,  h,  h_prime, eQt_eMinus, z1_Qt, z2_Qt, C1, CS_bar, R1_0, R1_1;

	std::array<ZZ, 4> result;

	//ZZ result[4];
	 

	//ZZ n[] = {a,x,p};

	 cin >> p; 
   cin >> g; 
   cin >> g_bar;
  
   	cin >> h;
    cin >> h_prime;

    cin >> eQt_eMinus;
   
   cin >> z1_Qt; 
   	cin >> z2_Qt; 
    
   	cin >> C1; 
    cin >> CS_bar;
    cin >> R1_0;
    cin >> R1_1;
  
   	 


  

  result = witness( p, g, g_bar,  h,  h_prime, eQt_eMinus, z1_Qt, z2_Qt, C1, CS_bar, R1_0, R1_1);


  for(int i=0;i<4;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
 

   
  
   	
   

   
}
