#include <iomanip>
#include <iostream>
#include <cmath>
#include <assert.h>

// função objetivo
double fun(double x) {
  return x*cos(x);
}

// código principal
int main() {

  // limites de integração
  double a = 0;
  double b = 9999999;

  // sub-intervalos da quadratura
  int n = 999999998;
  double h = (b-a)/n;

  // computa s0
  double s0 = 0;
  for (int j=1; j<n/2; j++)
    s0 += fun(a+2*j*h);

  // computa s1
  double s1 = 0;
  for (int j=1; j<=n/2; j++)
    s1 += fun(a+(2*j-1)*h);

  // imprime a solução
  std::cout << "Simpson = "
	    << h/3*(fun(a)+2*s0+4*s1+fun(b)) << std::endl
	    << "Analítica = "
	    << b*sin(b)+cos(b)-(a*sin(a)+cos(a)) << std::endl;

  return 0;
}
