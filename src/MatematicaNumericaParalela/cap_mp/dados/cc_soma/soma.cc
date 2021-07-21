#include <stdio.h>
#include <math.h>

#include <omp.h>

int main(int argc, char *argv[]) {

  int n = 999999991;

  int s = 0;

  #pragma omp parallel for reduction(+: s)
  for (int i=0; i<n+1; i++)
    s += 1;

  printf("%d\n",s);
  return 0;
}
