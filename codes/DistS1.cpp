#include <NTL/ZZ.h>

#include<array>
using namespace std;
using namespace NTL;



 
std::array<ZZ, 4> witness(ZZ p, ZZ g, ZZ y, ZZ h, ZZ z1, ZZ z2, ZZ z3, ZZ e_minus, ZZ B_0, ZZ B_1, ZZ V_0, ZZ V_1, ZZ Ec_0, ZZ Ec_1)
{
  

  std::array<ZZ, 4> result;
   

  ZZ B_prime [] = {(PowerMod(y, z1, p)* PowerMod(Ec_0, z2, p)*PowerMod(B_0*g %p , e_minus, p))%p, (PowerMod(g, z1, p)* PowerMod(Ec_1, z2, p)*PowerMod(B_1, e_minus, p))%p};

  ZZ V_prime [] = {(PowerMod(h, z3, p)*PowerMod(g, z2, p)*PowerMod(V_0, e_minus, p))%p, (PowerMod(g, z3, p)*PowerMod(V_1, e_minus, p))%p};


   //z = PowerMod(x, a, p); // z = x^a % 

 result = {B_prime[0], B_prime[1],V_prime[0], V_prime[1] };

  return result;

  

}


int main()

{

	ZZ p,y,g,h,z1,z2,z3,e_minus,B_0,B_1,V_0,V_1,Ec_0,Ec_1;

	std::array<ZZ,4> result;

	//ZZ result[4];
	 

	//ZZ n[] = {a,x,p};

	cin >> p; 
    cin >> g; 
   	cin >> y; 
   	cin >> h;
   	cin >> z1; 
    cin >> z2; 
   	cin >> z3; 
	cin >> e_minus; 
   	cin >> B_0; 
   	cin >> B_1; 
    cin >> V_0; 
   	cin >> V_1; 
   	cin >> Ec_0; 
   	cin >> Ec_1; 


  

  result = witness( p,g,y,h,z1,z2,z3,e_minus,B_0,B_1,V_0,V_1,Ec_0,Ec_1);

  //cout<<"The Array is : ";

  for(int i=0;i<4;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
  
   	
   

   
}
