#include <NTL/ZZ.h>

#include<array>
using namespace std;
using namespace NTL;



 
std::array<ZZ, 8> witness(ZZ p, ZZ g, ZZ y, ZZ h, ZZ r1, ZZ r1_prime,ZZ gamma1, ZZ gamma1_prime, ZZ gamma1_primePrime, ZZ B_0, ZZ B_1, ZZ V_0, ZZ V_1)
{
  

  std::array<ZZ, 8> result;
   

   ZZ B1 [] = {PowerMod(B_0, r1, p)* PowerMod(y , r1_prime, p) % p, PowerMod(B_1, r1, p)* PowerMod(g , r1_prime, p) % p};
   ZZ V1 []= {PowerMod(h, gamma1, p)*PowerMod(g, r1, p) % p, PowerMod(g, gamma1, p) };
   ZZ V1_prime [] = {PowerMod(h, gamma1_prime, p)*PowerMod(V_0, r1, p) % p, PowerMod(g, gamma1_prime, p)};
  ZZ V1_primeprime [] = {PowerMod(h, gamma1_primePrime, p)*PowerMod(V_1, r1, p) % p, PowerMod(g, gamma1_primePrime, p)};


   //z = PowerMod(x, a, p); // z = x^a % 

 result = {B1[0], B1[1],V1[0], V1[1], V1_prime[0], V1_prime[1], V1_primeprime[0], V1_primeprime[1]};

  return result;

  

}


int main()

{

	ZZ p,y,g,h,r1,r1_prime,gamma1,gamma1_prime, gamma1_primePrime,B_0,B_1,V_0,V_1;

	std::array<ZZ,8> result;

	//ZZ result[4];
	 

	//ZZ n[] = {a,x,p};

	 cin >> p; 
    cin >> g; 
   	cin >> y; 
   	cin >> h;
   	cin >> r1; 
    cin >> r1_prime; 
   	cin >> gamma1; 
	 cin >> gamma1_prime; 
    cin >> gamma1_primePrime;
   	cin >> B_0; 
   	cin >> B_1; 
    cin >> V_0; 
   	cin >> V_1; 
   	 


  

  result = witness( p,g,y,h,r1,r1_prime,gamma1,gamma1_prime, gamma1_primePrime,B_0,B_1,V_0,V_1);

  //cout<<"The Array is : ";

  for(int i=0;i<8;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
  
   	
   

   
}
