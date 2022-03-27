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



 
std::array<ZZ, 2> witness(ZZ q, ZZ e_Qs, ZZ a1, ZZ mu, ZZ v, ZZ delta)
{
  

  NTL::SetSeed(conv<ZZ>((long) time(0)));
  std::array<ZZ, 2> result;

  

  ///ZZ mu1_i = RandomBnd(q); // random number between 0 and q-1


   
  
   ZZ QsZ1 = (a1 * e_Qs + mu) % q;
   ZZ QsZ2 = (delta * e_Qs + v) % q;
    

    result = {QsZ1, QsZ2};

    return result;

}


  




int main()

{

  ZZ q,e_Qs,a1,mu,v,delta;

  std::array<ZZ,2> result;

  //ZZ result[4];
   

  //ZZ n[] = {a,x,p};

  cin >> q; 
  cin >> e_Qs;
  cin >> a1; 
  cin >> mu; 
  cin >> v; 
  cin >> delta; 
 
     


  

  result = witness(q,e_Qs,a1,mu,v,delta);


  for(int i=0;i<2;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
}