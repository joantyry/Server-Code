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



 
std::array<ZZ, 5> witness(ZZ q, ZZ serv_e, ZZ r1, ZZ r1_prime,ZZ gamma1, ZZ gamma1_prime, ZZ gamma1_primePrime, ZZ mu1, ZZ mu2, ZZ v1, ZZ v2, ZZ v3)
{
  

  NTL::SetSeed(conv<ZZ>((long) time(0)));
  std::array<ZZ, 5> result;

  

  ///ZZ mu1_i = RandomBnd(q); // random number between 0 and q-1


   

    ZZ sz1 = (r1 * serv_e + mu1) % q;
    ZZ sz2 = (r1_prime * serv_e + mu2) % q;
    ZZ sz3 = (gamma1 * serv_e + v1) % q;
    ZZ sz4 = (gamma1_prime * serv_e + v2) % q;
    ZZ sz5 = (gamma1_primePrime * serv_e + v3) % q;

    

    result = {sz1,sz2,sz3,sz4,sz5};

    return result;

}


  




int main()

{

	ZZ q,serv_e, r1,r1_prime,gamma1,gamma1_prime, gamma1_primePrime,mu1,mu2,v1,v2,v3;

	std::array<ZZ,5> result;

	//ZZ result[4];
	 

	//ZZ n[] = {a,x,p};

	cin >> q; 
  cin >> serv_e;
  cin >> r1; 
  cin >> r1_prime; 
  cin >> gamma1; 
  cin >> gamma1_prime; 
  cin >> gamma1_primePrime;
  cin >> mu1;
  cin >> mu2;
   cin >> v1;
   cin >> v2;
   cin >> v3;
   	 


  

  result = witness(q,serv_e,r1,r1_prime,gamma1,gamma1_prime, gamma1_primePrime,mu1,mu2,v1,v2,v3);


  for(int i=0;i<5;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
}
