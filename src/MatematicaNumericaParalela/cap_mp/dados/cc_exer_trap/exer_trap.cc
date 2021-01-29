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
  double h = (b-a)/n;

  double s = 0;
  #pragma omp parallel for reduction(+: s)
  for (int i=1; i<n; i++) {
    s += f(a + i*h);
  }
  s *= 2;
  s += f(a) + f(b);
  s *= h/2;

  printf("%f\n",s);
  
  return 0;
}

