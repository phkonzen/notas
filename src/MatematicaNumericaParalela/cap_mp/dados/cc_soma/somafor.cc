#include <omp.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {

  int n = 99999999;
  
  int s = 0;
  #pragma omp parallel
  {
    int st = 0;
    
    #pragma omp for
    for (int i=0; i<n; i++)
      st += 1;

    #pragma omp critical
    s += st;
  }
  printf("%d\n",s);
  return 0;
}
