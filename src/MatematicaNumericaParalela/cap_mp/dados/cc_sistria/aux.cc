#include <omp.h>
#include <stdio.h>
#include <ctime>
#include <algorithm>

#include <gsl/gsl_spmatrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_rng.h>

int np, pid;
int ini, fim;
#pragma omp threadprivate(np,pid,ini,fim)

int main(int argc, char *argv[]) {

  static int x = 0;
  #pragma omp threadprivate(x)
  #pragma omp parallel
  x = 1;
  #pragma omp parallel
  printf("%d\n",x);
  
  return 0;
}
