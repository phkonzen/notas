#include <omp.h>
#include <stdio.h>
#include <ctime>

// GSL vector suport
#include <gsl/gsl_vector.h>
#include <gsl/gsl_rng.h>

int main(int argc, char *argv[]) {

  int n = 99999999;

  // vetores
  gsl_vector *a = gsl_vector_alloc(n);
  gsl_vector *b = gsl_vector_alloc(n);

  // gerador randômico
  gsl_rng *rng = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(rng, time(NULL));

  // inicializa os vetores
  #pragma omp parallel for
  for (int i=0; i<n; i++) {
    gsl_vector_set(a, i, gsl_rng_uniform(rng));
    gsl_vector_set(b, i, gsl_rng_uniform(rng));
  }

  // produto escalar
  double dot = 0;
  #pragma omp parallel for reduction(+: dot)
  for (int i=0; i<n; i++)
    dot += gsl_vector_get(a, i) * \
      gsl_vector_get(b, i);

  printf("%f\n",dot);

  gsl_vector_free(a);
  gsl_vector_free(b);
  gsl_rng_free(rng);
  
  return 0;
}
