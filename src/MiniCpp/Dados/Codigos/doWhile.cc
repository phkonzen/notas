#include <stdio.h>
#include <math.h>

int main()
{
  int i = 0;
  double s;
  do {
    s += pow(0.5, double(i));
    i += 1;
  } while (i < 10);
  printf("s = %lf\n", s);
  return 0;
}
