#include <stdio.h>

void f(double x)
{
  double y = 2.*x - 3.;
  printf("f(%lf) = %lf\n", x, y);
}

int main()
{
  f(0.);
  double x = -1.;
  f(x);
  double y = 2.;
  f(y);
  return 0;
}
