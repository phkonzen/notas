#include <omp.h>
#include <stdio.h>
#include <math.h>

double f(double x)
{
  return exp(-x*x);
}

int main(int argc, char *argv[]) {

  // limite de integração
  double a = -1.0;
  double b = 1.0;
  // num. de subintervalos
  int n = 9999999;
  // tamanho dos subintervalos
  double h = (b-a)/(2*n);

  double s1 = 0;
  double s2 = 0;
  #pragma omp parallel reduction(+: s1) reduction(+: s2)
  {

    #pragma omp for nowait
    for (int i=1; i<n; i++)
      s1 += f(a + 2*i*h);

    #pragma omp for
    for (int i=1; i<n; i++)
      s2 += f(a + (2*i-1)*h);
  }
  
  double s = h/3*(f(a) + 2*s1 + \
		  4*s2 + f(b));

  printf('%f\n',s);
  
  return 0;
}

