#include <omp.h>
#include <stdio.h>
#include <time.h>

#include <gsl/gsl_matrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_rng.h>

// random +/- 1
double randsig(gsl_rng *rng);

int main(int argc, char *argv[]) {

  int n = 999;
  int tmax = 50;
  double tol = 1e-8;

  gsl_matrix *a = gsl_matrix_alloc(n,n);
  gsl_vector *b = gsl_vector_alloc(n);
  
  gsl_vector *x = gsl_vector_alloc(n);
  gsl_vector *x0 = gsl_vector_alloc(n);

  // gerador randômico
  gsl_rng *rng = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(rng, time(NULL));

  // Inicializacao
  // Matriz estritamente diagonal dominante
  printf('Inicializacao ... \n');
  double sig;
  for (int i=0; i<n; i++) {
    double s = 0;
    for (int j=0; j<n; j++) {
      double aux = gsl_rng_uniform(rng);
      gsl_matrix_set(a, i, j,
		     randsig(rng)*aux);
      s += aux;
    }
    gsl_matrix_set(a, i, i,
		   randsig(rng) * s);
    gsl_vector_set(b, i,
		   randsig(rng) *
		   gsl_rng_uniform(rng));
    gsl_vector_set(x, i,
		   randsig(rng) *
		   gsl_rng_uniform(rng));
  }
  printf('feito.\n');

  // Random Gauss-Seidel
  for (int t=0; t<tmax; t++) {
    gsl_vector_memcpy(x0, x);
    #pragma omp parallel for
    for (int i=0; i<n; i++) {
      double s = 0;
      for (int j=0; j<i; j++)
	s += gsl_matrix_get(a, i, j) *
	  gsl_vector_get(x, j);
      for (int j=i+1; j<n; j++)
	s += gsl_matrix_get(a, i, j) *
	  gsl_vector_get(x, j);
      gsl_vector_set(x, i,
		     (gsl_vector_get(b, i) - s) /
		     gsl_matrix_get(a, i, i)); 
    }
    // criterio de parada
    // ||x-x0||_2 < tol
    gsl_blas_daxpy(-1.0, x, x0);
    double e = gsl_blas_dnrm2(x0);
    printf('Iter. %d: %1.0e\n', t, e);
    if (e < tol)
      break;
  }

  gsl_matrix_free(a);
  gsl_vector_free(b);
  gsl_vector_free(x);
  gsl_vector_free(x0);
  gsl_rng_free(rng);
  
  return 0;
}

double randsig(gsl_rng *rng)
{
  double signal = 1.0;
  if (gsl_rng_uniform(rng) >= 0.5)
	signal = -1.0;
  return signal;
}
