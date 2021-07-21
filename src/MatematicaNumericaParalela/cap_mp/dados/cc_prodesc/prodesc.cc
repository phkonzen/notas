// io
#include <stdio.h>
// rand
#include <cstdlib>
// time
#include <ctime>
// openMP
#include <omp.h>

#define n 99999

int main(int argc, char *argv[]) {

  double a[n], b[n];

  // inicializa rand
  srand(time(NULL));

  // inicializa os vetores
  #pragma omp parallel for
  for (int i=0; i<n; i++) {
    a[i] = double(rand())/RAND_MAX;
    b[i] = double(rand())/RAND_MAX;
  }

  // produto escalar
  double dot = 0;
  #pragma omp parallel for reduction(+: dot)
  for (int i=0; i<n; i++)
    dot += a[i] * b[i];

  printf("%lf\n",dot);

  return 0;
}
