#include <iostream>

// OpenMP API
#include <omp.h>

using namespace std;

int main(int argc, char *argv[]) {

  double a,b;
  printf("Digite o primeiro numero: ");
  scanf("%lf", &a);
  
  printf("Digite o segundo numero: ");
  scanf("%lf", &b);

  // regiao paralela
  #pragma omp parallel				
  {
    // id do processo
    int id = omp_get_thread_num();
    
    if (id == 0) {
      printf("Soma: %f\n", (a+b));
    }
    else if (id == 1) {
      printf("Produto: %f\n", (a*b));
    }
  }
  
  return 0;
}
