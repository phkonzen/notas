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

  double a = 0;
  double b = 9999999;
  int n = 999999998;

  double h = (b-a)/n;

  double s1 = 0;
  for (int j=1; j<n/2; j++)
    s1 += fun(a+2*j*h);

  double s2 = 0;
  for (int j=1; j<=n/2; j++)
    s2 += fun(a+(2*j-1)*h);

  std::cout << std::setprecision(10)
	    << h/3*(fun(a)+2*s1+4*s2+fun(b))
	    << std::endl
	    << b*sin(b)+cos(b)-(a*sin(a)+cos(a))
	    << std::endl;

  return 0;
}
