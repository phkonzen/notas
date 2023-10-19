#include <stdio.h>

int main()
{
  double a,b;
  printf("a = ");
  scanf("%lf", &a);
  printf("b = ");
  scanf("%lf", &b);

  if (a != 0.) {
    double x = -b/a;
    printf("x = %lf\n", x);
  }

  return 0;
}
