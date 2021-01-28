#include <omp.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {

  int n = 1000;
  
  int s = 0;
  #pragma omp parallel
  {
    int tid = omp_get_thread_num();
    int nt = omp_get_num_threads();

    int np = ceil(double(n)/nt);
    for (int i=tid*np; i<(tid+1)*np & i<n; i++)
      s += i;
  }
  printf("%d\n",s);
  return 0;
}
