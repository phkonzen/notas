#include <stdio.h>
#include <omp.h>

int main(int argc, char *argv[]) {

  int tid=10;
  int nt;

  // região paralela
#pragma omp parallel private(tid)
  {
    
    printf("Processo %d/%d\n", tid, nt);
  }
  printf("%d\n",tid);
  return 0;
}
