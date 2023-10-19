#include <stdio.h>

double f(double x)
{
  return 2.*x - 3.;
}

int main()
{
  double y = f(0.);
  printf("f(%lf) = %lf\n", 0., y);
  printf("f(%lf) = %lf\n", -1., f(-1.));
  double z = 2.;
  printf("f(%lf) = %lf\n", z, f(z));
  return 0;
}
