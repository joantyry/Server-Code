#include <NTL/ZZ.h>

#include<array>
using namespace std;
using namespace NTL;



 
std::array<ZZ, 8> witness(ZZ p, ZZ g, ZZ y, ZZ h, ZZ sz1, ZZ sz2, ZZ sz3, ZZ sz4, ZZ sz5, ZZ e_minus, ZZ B_0, ZZ B_1, ZZ V_0, ZZ V_1, ZZ BS_0, ZZ BS_1, ZZ VS_0, ZZ VS_1, ZZ VS_Prime_0, ZZ VS_Prime_1, ZZ VS_PrimePrime_0, ZZ VS_PrimePrime_1)
{
  

  std::array<ZZ, 8> result;
   
  ZZ B_bar [] = {(PowerMod(B_0, sz1, p)* PowerMod(y, sz2, p)*PowerMod(BS_0, e_minus, p))%p, (PowerMod(B_1, sz1, p)* PowerMod(g, sz2, p)*PowerMod(BS_1, e_minus, p))%p};
  ZZ V_bar [] = {(PowerMod(h, sz3, p)* PowerMod(g, sz1, p)*PowerMod(VS_0, e_minus, p))%p, (PowerMod(g, sz3, p)*PowerMod(VS_1, e_minus, p))%p};
  ZZ V_barPrime [] = {(PowerMod(h, sz4, p)* PowerMod(V_0, sz1, p)*PowerMod(VS_Prime_0, e_minus, p))%p, (PowerMod(g, sz4, p)*PowerMod(VS_Prime_1, e_minus, p))%p};
  ZZ V_barPrimePrime [] = {(PowerMod(h, sz5, p)* PowerMod(V_1, sz1, p)*PowerMod(VS_PrimePrime_0, e_minus, p))%p, (PowerMod(g, sz5, p)*PowerMod(VS_PrimePrime_1, e_minus, p))%p};

   //z = PowerMod(x, a, p); // z = x^a % 

  result = {B_bar[0], B_bar[1], V_bar[0], V_bar[1], V_barPrime[0], V_barPrime[1], V_barPrimePrime[0], V_barPrimePrime[1]};

  return result;

  

}


int main()

{

	ZZ p,g,y,h,sz1,sz2,sz3,sz4,sz5,e_minus,B_0,B_1,V_0,V_1,BS_0,BS_1,VS_0,VS_1,VS_Prime_0,VS_Prime_1,VS_PrimePrime_0,VS_PrimePrime_1;

	std::array<ZZ, 8> result;

	//ZZ result[4];
	 

	//ZZ n[] = {a,x,p};

	cin >> p; 
    cin >> g; 
   	cin >> y; 
   	cin >> h;
   	cin >> sz1; 
    cin >> sz2; 
   	cin >> sz3; 
    cin >> sz4;
    cin >> sz5;  
	cin >> e_minus; 
   	cin >> B_0; 
   	cin >> B_1; 
    cin >> V_0; 
   	cin >> V_1; 
   	cin >> BS_0; 
   	cin >> BS_1; 
    cin >> VS_0; 
    cin >> VS_1;
    cin >> VS_Prime_0; 
    cin >> VS_Prime_1;
    cin >> VS_PrimePrime_0; 
    cin >> VS_PrimePrime_1;


  

  result = witness( p,g,y,h,sz1,sz2,sz3,sz4,sz5,e_minus,B_0,B_1,V_0,V_1,BS_0,BS_1,VS_0,VS_1,VS_Prime_0,VS_Prime_1,VS_PrimePrime_0,VS_PrimePrime_1);

  //cout<<"The Array is : ";

  for(int i=0;i<8;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
  
   	
   

   
}
