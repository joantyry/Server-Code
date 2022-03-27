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



 
std::array<ZZ, 3> witness( ZZ p, ZZ g, ZZ h, ZZ h_prime, ZZ Qs_eMinus, ZZ QsZ1, ZZ QsZ2, ZZ C1_Qs, ZZ R1_Qs_0, ZZ R1_Qs_1)
{
  

  //NTL::SetSeed(conv<ZZ>((long) time(0)));
  std::array<ZZ, 3> result;

  

  ///ZZ mu1_i = RandomBnd(q); // random number between 0 and q-1


   

  ZZ R_primeQs [] = {(PowerMod(h, QsZ2, p)* PowerMod(h_prime, QsZ1, p)*PowerMod(R1_Qs_0, Qs_eMinus, p) )%p, (PowerMod(g, QsZ2, p)*PowerMod( R1_Qs_1, Qs_eMinus,p))%p};
  ZZ W_Qs  = (PowerMod(g, QsZ1, p)* PowerMod(C1_Qs, Qs_eMinus, p))%p;

  result = {R_primeQs[0], R_primeQs[1], W_Qs};


  return result;
}


  




int main()

{

	ZZ  p,g,h,h_prime,Qs_eMinus,QsZ1,QsZ2,C1_Qs,R1_Qs_0,R1_Qs_1;

	std::array<ZZ,3> result;

	//ZZ result[4];
	 

	//ZZ n[] = {a,x,p};

	 cin >> p; 
   cin >> g; 
  
   	cin >> h;
    cin >> h_prime;

    cin >> Qs_eMinus;
   
   cin >> QsZ1; 
   	cin >> QsZ2; 
    
   	cin >> C1_Qs; 
    cin >> R1_Qs_0;
    cin >> R1_Qs_1;
  
   	 


  

  result = witness( p,g,h,h_prime,Qs_eMinus,QsZ1,QsZ2,C1_Qs,R1_Qs_0,R1_Qs_1);


  for(int i=0;i<3;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
 

   
  
   	
   

   
}
