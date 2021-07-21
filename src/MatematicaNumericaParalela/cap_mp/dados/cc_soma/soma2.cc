#include <omp.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {

  int n = 999999991;
  
  int s = 0;
  #pragma omp parallel
  {
    int tid = omp_get_thread_num();
    int nt = omp_get_num_threads();

    int ini = (n+1)/nt*tid;
    int fin = (n+1)/nt*(tid+1);
    if (tid == nt-1)
      fin = n+1;

    int st = 0;
    for (int i=ini; i<fin; i++)
      st += 1;

    #pragma omp critical
    s += st;
  }
  
  printf("%d\n",s);
  
  return 0;
}
