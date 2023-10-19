#include <stdio.h>
#include <math.h>

int main()
{
  int i = 0;
  double s = 0.;
  while (i < 10) {
    s = s + pow(0.5, double(i));
    i += 1;
  }
  printf("s = %lf\n", s);
  return 0;
}
