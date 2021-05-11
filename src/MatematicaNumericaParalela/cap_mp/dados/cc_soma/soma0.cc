#include <omp.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {

  int n = 99999999;
  
  int s = 0;
  #pragma omp parallel
  {
    int tid = omp_get_thread_num();
    int nt = omp_get_num_threads();

    int ini = n/nt*tid;
    int fin = n/nt*(tid+1);
    if (tid == nt-1)
      fin = n;
    for (int i=ini; i<fin; i++)
      s += 1;
  }
  printf('%d\n',s);
  return 0;
}
