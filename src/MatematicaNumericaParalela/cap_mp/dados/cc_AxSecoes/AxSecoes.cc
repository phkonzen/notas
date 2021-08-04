#include <stdio.h>
#include <cstdlib>
#include <ctime>
#include <omp.h>

#define n 9999

int main(int argc, char *argv[]) {

  // matriz
  double a[n][n];
  // vetores
  double x[n], y[n];

  // inicializa rand
  srand(time(NULL));

  // inicializacao
  for (int i=0; i<n; i++) {
    for (int j=0; j<n; j++) {
      a[i][j] = double(rand())/RAND_MAX;
    }
    x[i] = double(rand())/RAND_MAX;
    
    y[i] = 0.;
  }

  // y = A*x
  #pragma omp parallel sections
  {
    #pragma omp section
    {
      for (int i=0; i<n/2; i++)
	for (int j=0; j<n; j++)
	  y[i] += a[i][j] * x[j];
    }
    
    #pragma omp section
    {
      for (int i=n/2; i<n; i++)
	for (int j=0; j<n; j++)
	  y[i] += a[i][j] * x[j];
    }
  }
  
  return 0;
}
