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



 
std::array<ZZ, 8> witness(ZZ p, ZZ g, ZZ y, ZZ h, ZZ B_0, ZZ B_1, ZZ V_0, ZZ V_1, ZZ mu1, ZZ mu2, ZZ v1, ZZ v2, ZZ v3)
{
  

  NTL::SetSeed(conv<ZZ>((long) time(0)));
  std::array<ZZ, 8> result;

  

  ///ZZ mu1_i = RandomBnd(q); // random number between 0 and q-1


   

  ZZ B_bar []= {PowerMod(B_0, mu1, p)* PowerMod(y , mu2, p) % p, PowerMod(B_1, mu1, p)* PowerMod(g , mu2, p) % p};
  ZZ V_bar [] = {PowerMod(h, v1, p)* PowerMod(g , mu1, p) % p, PowerMod(g, v1, p)};
  ZZ V_barPrime [] = {PowerMod(h, v2, p)* PowerMod(V_0 , mu1, p) % p, PowerMod(g, v2, p)};
  ZZ V_barPrimePrime [] = {PowerMod(h, v3, p)* PowerMod(V_1 , mu1, p) % p, PowerMod(g, v3, p)};

  result = {B_bar[0], B_bar[1], V_bar[0], V_bar[1],V_barPrime[0],V_barPrime[1],V_barPrimePrime[0], V_barPrimePrime[1]};


  return result;
}


  




int main()

{

	ZZ p,g,y,h,B_0,B_1,V_0,V_1,mu1,mu2,v1,v2,v3;

	std::array<ZZ,8> result;

	//ZZ result[4];
	 

	//ZZ n[] = {a,x,p};

	 cin >> p; 
    cin >> g; 
   	cin >> y; 
   	cin >> h;
   
   cin >> B_0; 
   	cin >> B_1; 
    cin >> V_0; 
   	cin >> V_1; 
    cin >> mu1;
    cin >> mu2;
   cin >> v1;
   cin >> v2;
   cin >> v3;
   	 


  

  result = witness( p,g,y,h,B_0,B_1,V_0,V_1,mu1,mu2,v1,v2,v3);


  for(int i=0;i<8;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
 

   
  
   	
   

   
}
