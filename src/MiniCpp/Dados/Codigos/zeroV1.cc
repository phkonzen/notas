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
  } else if ((a == 0.) && (b == 0.)) {
    printf("Todo x real é zero da função.\n");
  }

  return 0;
}
