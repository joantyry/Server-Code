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



 

ZZ bars(ZZ C_bars_0, ZZ C_bars_1, ZZ p){



   ZZ result1 = C_bars_0 * C_bars_1 % p ;
 
   return result1;


}



ZZ witness( ZZ p, ZZ y_til, ZZ x1_prime, ZZ share_pr, ZZ OnlineServers_0, ZZ OnlineServers_1, ZZ tau_0, ZZ tau_1, ZZ tau_2)


{
  

  //NTL::SetSeed(conv<ZZ>((long) time(0)));
  //std::array<ZZ, 4> result;
   ZZ y1_til = PowerMod(y_til, x1_prime, p);

  ZZ lst [] = {OnlineServers_0, OnlineServers_1, tau_0, tau_1, tau_2, y1_til};

    ZZ sum = ZZ(0);
    
    for (int i = 0; i < 6; i++) {

            sum = sum + lst[i]; 

           }   



    
   ZZ key = sum % p ;

   ZZ key_inv = (ZZ(0) - key) % p;


   ZZ EncShare = (key_inv + share_pr) % p;
   





 
    return EncShare;
}


  




int main()

{

	ZZ  p, y_til, y_bar, x1_prime, share_pr, OnlineServers_0, OnlineServers_1, tau_0, tau_1, tau_2, C_bars_0,C_bars_1;

	//std::array<ZZ, 4> result;

	//ZZ result[4];
	 

	//ZZ n[] = {a,x,p};

	 cin >> p; 
   cin >> y_til; 
   cin >> y_bar;
  
   	cin >> x1_prime;
    cin >> share_pr;

    cin >> OnlineServers_0;
    cin >> OnlineServers_1; 

   	cin >> tau_0; 
    cin >> tau_1;
    cin >> tau_2;

    cin >> C_bars_0;
    cin >> C_bars_1;
   
   	 


  ZZ result1 = bars(C_bars_0, C_bars_1, p);    


  if  (y_bar == result1){


     ZZ result = witness(  p, y_til, x1_prime, share_pr, OnlineServers_0, OnlineServers_1, tau_0, tau_1, tau_2);



    cout<< result <<"\n";


  }
  
else{


  cout<< "Wrong Password!" <<"\n";
}


}
