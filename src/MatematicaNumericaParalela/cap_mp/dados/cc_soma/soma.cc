#include <omp.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {

  int n = 99999999;
  int s = 0;
  
  #pragma omp parallel for reduction(+: s)
  for (int i=0; i<n; i++)
    s += 1;

  printf("%d\n",s);
  return 0;
}
