#include <stdio.h>
#include <omp.h>

int main(int argc, char *argv[]) {

  int tid, nt;

  // regiao paralela
  #pragma omp parallel
  {
    tid = omp_get_thread_num();
    nt = omp_get_num_threads();
    
    printf("Processo %d/%d\n", tid, nt);
  }
  printf("%d\n",nt);
  return 0;
}
