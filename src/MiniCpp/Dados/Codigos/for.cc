#include <stdio.h>
#include <math.h>

int main()
{
  double s = 0;
  for (int i=0; i<10; ++i) {
    s += pow(2., double(-i));
  }
  printf("s = %lf\n", s);
  return 0;
}
