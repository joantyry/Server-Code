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



 
std::array<ZZ, 6> witness(ZZ p, ZZ g, ZZ h, ZZ h_prime, ZZ a1, ZZ prod, ZZ y_i, ZZ mu, ZZ v, ZZ delta)
{
  

  NTL::SetSeed(conv<ZZ>((long) time(0)));
  std::array<ZZ, 6> result;

  

  ///ZZ mu1_i = RandomBnd(q); // random number between 0 and q-1


   

   ZZ W = PowerMod(g, mu, p);

   ZZ R_prime [] = {(PowerMod(h, v, p)* PowerMod(h_prime, mu, p))%p, PowerMod(g, v, p)};

   ZZ R1 [] = {(PowerMod(h, delta, p)* PowerMod(h_prime, a1, p))%p, PowerMod(g, delta, p)};

   ZZ C1 = PowerMod(y_i, prod, p);


  result = {W, R_prime[0], R_prime[1], R1[0], R1[1], C1};


  return result;
}


  




int main()

{

  ZZ p,g,h,h_prime,a1,prod,y_i, mu, v, delta;

  std::array<ZZ,6> result;

  //ZZ result[4];
   

  //ZZ n[] = {a,x,p};

   cin >> p; 
    cin >> g; 
     
    cin >> h;
    cin >> h_prime;
   
   cin >> a1; 
    cin >> prod; 
    
    cin >> y_i; 
    cin >> mu;
    cin >> v;
   cin >> delta;
  
     


  

  result = witness( p,g,h,h_prime,a1,prod,y_i, mu, v, delta);


  for(int i=0;i<6;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
 

   
  
    
   

   
}