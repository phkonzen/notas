#include <stdio.h>
#include <math.h>

int main()
{
  // P = (2, 3)
  int P[2] = {2, 3};
  printf("P = (%d, %d)\n", P[0], P[1]);
  
  double v[3];
  v[0] = 2.5;
  v[1] = M_PI;
  v[2] = -1.;
  printf("v = (%lf, %lf, %lf)\n", v[0], v[1], v[2]);
  
  return 0;
}
