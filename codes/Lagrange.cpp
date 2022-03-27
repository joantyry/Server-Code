#include <NTL/ZZ.h>

#include<array>
using namespace std;
using namespace NTL;



 
std::array<ZZ, 5> witness(ZZ p, ZZ q, ZZ j,ZZ x1, ZZ B1_0, ZZ B1_1, ZZ BS_0, ZZ BS_1, ZZ Onl_0, ZZ Onl_1)
{
  

  std::array<ZZ, 5> result;


  ZZ OnlineServers [] = {Onl_0, Onl_1} ;

  ZZ product [] = {(B1_0*BS_0)%p, (B1_1*BS_1)%p };

    
  ZZ y_bar =  product[0];
    
  ZZ g_bar = product[1];

  ZZ prod = ZZ(1);


  for (int k = 0; k < 2; ++k)
  {

    ZZ i = OnlineServers[k];

    if (i != j){
      
      prod = prod * ((0-i)%q * InvMod((j-i)% q, q))% q;

    }
    
  }

  

  ZZ a1 = (prod * x1) % q ;

 

  ZZ C_bar1 = PowerMod(g_bar, a1, p); 

    
   //z = PowerMod(x, a, p); // z = x^a % 

  result = {y_bar, C_bar1, a1, prod, g_bar};

  return result;

  

}


int main()

{

	ZZ p,q,j,x1,B1_0,B1_1,BS_0, BS_1, Onl_0, Onl_1;

	std::array<ZZ, 5> result;

	//ZZ result[4];
	 

	//ZZ n[] = {a,x,p};

    cin >> p; 
    cin >> q; 

    cin >> j;
    cin >> x1; 
    cin >> B1_0; 
    cin >> B1_1; 
    cin >> BS_0; 
    cin >> BS_1;
    cin >> Onl_0;
    cin >> Onl_1;

  

  result = witness( p,q,j,x1,B1_0,B1_1,BS_0, BS_1, Onl_0, Onl_1);

  //cout<<"The Array is : ";

  for(int i=0;i<5;i++)

    {
        cout<<result[i]<<",";
    }
     

    return 0;

   
  
   	
   

   
}
