#include <stdio.h>

// OpenMP API
#include <omp.h>

using namespace std;

int main(int argc, char *argv[]) {

  // região paralela
  #pragma omp parallel				
  {
    // id da instância de processamento
    int id = omp_get_thread_num();
    
    printf("Processo %d, olá!\n", id);
  }
  
  return 0;
}
