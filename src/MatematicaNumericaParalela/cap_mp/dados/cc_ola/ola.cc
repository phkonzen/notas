#include <stdio.h>

// OpenMP API
#include <omp.h>

int main(int argc, char *argv[]) {

  // regiao paralela
  #pragma omp parallel				
  {
    // id da instancia de processamento
    int id = omp_get_thread_num();
    
    printf("Processo %d, ola!\n", id);
  }
  
  return 0;
}
