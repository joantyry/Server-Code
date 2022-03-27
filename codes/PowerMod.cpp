#include <NTL/ZZ.h>


using namespace std;
using namespace NTL;



ZZ witness(ZZ p, ZZ x, ZZ a)
{
  
   ZZ z; 

   //ZZ arr = 

   z = PowerMod(x, a, p); // z = x^a % p
  
  return z;
}


int main()

{

	ZZ z,x,a,p;

	//ZZ n[] = {a,x,p};

	cin >> p; 
	cin >> x; 
   	cin >> a; 

	//ZZ p1= conv<ZZ>(p);
	//ZZ x1= conv<ZZ>(x);
	//ZZ a1= conv<ZZ>(a);

	//conv(z,p); //converts int to zz
	//conv(z,x);
	//conv(z,a);

  

   z = witness(p, x, a);

   

   cout << z << "\n";
}