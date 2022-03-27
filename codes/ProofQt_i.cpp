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



 
std::array<ZZ, 2> witness(ZZ q, ZZ a1, ZZ delta, ZZ e_Qt, ZZ mu, ZZ v)
{
  

  NTL::SetSeed(conv<ZZ>((long) time(0)));
  std::array<ZZ, 2> result;

  

  ///ZZ mu1_i = RandomBnd(q); // random number between 0 and q-1


   
  
    ZZ QtZ1 = (a1 * e_Qt + mu)% q;
    ZZ QtZ2 = (delta * e_Qt + v)% q;

    result = {QtZ1, QtZ2};

    return result;

}


  




int main()

{

	ZZ q,a1,delta, e_Qt, mu,v;

	std::array<ZZ,2> result;

	//ZZ result[4];
	 

	//ZZ n[] = {a,x,p};

	cin >> q; 
  cin >> a1;
  cin >> delta; 
  cin >> e_Qt;
  cin >> mu; 
  cin >> v; 
  
 
   	 


  

  result = witness(q,a1,delta, e_Qt, mu,v);


  for(int i=0;i<2;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
}
