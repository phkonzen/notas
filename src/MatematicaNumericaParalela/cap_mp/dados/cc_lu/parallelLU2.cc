#include <omp.h>
#include <stdio.h>
#include <ctime>
#include <algorithm>

#include <gsl/gsl_matrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_blas.h>

int main(int argc, char *argv[]) {

  int n = 5;

  gsl_matrix *a = gsl_matrix_alloc(n,n);

  // gerador randomico
  gsl_rng *rng = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(rng, time(NULL));

  // inicializacao
  printf('Inicializando ... \n'); 
  for (int i=0; i<n; i++) {
    for (int j=0; j<i; j++) {
      int sig = 1;
      if (gsl_rng_uniform(rng) >= 0.5)
	sig = -1;
      gsl_matrix_set(a, i, j,
		     sig*gsl_rng_uniform(rng));
      gsl_matrix_set(a, j, i,
		     gsl_matrix_get(a, i, j));
    }
    int sig = 1;
    if (gsl_rng_uniform(rng) >= 0.5)
      sig = -1;
    gsl_matrix_set(a, i, i,
  		     sig*gsl_rng_uniform_pos(rng));
  }
  printf('feito.\n');

  for (int k=0; k<n-1; k++) {
    #pragma omp parallel for
    for (int i=k+1; i<n; i++) {
      gsl_matrix_set(a, i, k,
  		     gsl_matrix_get(a, i, k)/
  		     gsl_matrix_get(a, k, k));
      for (int j=k+1; j<n; j++) {
  	gsl_matrix_set(a, i, j,
  		       gsl_matrix_get(a, i, j) -
  		       gsl_matrix_get(a, i, k) *
  		       gsl_matrix_get(a, k, j));
      }
    }
  }
  gsl_matrix_free(a);
  gsl_rng_free(rng);
  
  return 0;
}
