#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <omp.h>

// GSL
#include <gsl/gsl_vector.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_rng.h>

using namespace std;

int main (int arc, char *argv[]) {
  const size_t n = 10000;
  gsl_matrix *a = gsl_matrix_alloc(n,n);
  gsl_vector *x = gsl_vector_alloc(n);

  // y parallel
  gsl_vector *yp = gsl_vector_alloc(n);

  // y serial
  gsl_vector *ys = gsl_vector_alloc(n);

  gsl_rng *r = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(r, time(NULL));

  for (int i=0; i<n; i++)
    for (int j=0; j<n; j++)
      gsl_matrix_set(a, i, j, gsl_rng_uniform(r));

  for (int i=0; i<n; i++)
    gsl_vector_set(x, i, gsl_rng_uniform(r));

  time_t t = time(NULL);
  #pragma omp parallel
  {
    int id = omp_get_thread_num();
    int np = omp_get_num_threads();

    int nt = ceil(double(n)/np);

    double ya;
    for (int i=id*nt; i<(id+1)*nt & i<n; i++) {
      gsl_vector_const_view c = gsl_matrix_const_row(a, i);
      gsl_blas_ddot(&c.vector, x, &ya);
      gsl_vector_set(yp, i, ya);
    }
  }
  time_t tp = (time(NULL) - t);
  printf("Parallel took: %ld s\n", tp);

  t = time(NULL);
  double ya;
  for (int i=0; i<n; i++) {
    gsl_vector_const_view c = gsl_matrix_const_row(a, i);
    gsl_blas_ddot(&c.vector, x, &ya);
    gsl_vector_set(ys, i, ya);
  }
  time_t ts = time(NULL) - t;
  printf("Serial took: %ld s\n", ts);
    
  // for (int i=0; i<n; i++)
  //   printf("%lf %lf\n", gsl_vector_get(yp, i), gsl_vector_get(ys, i));
  
  
  
  gsl_matrix_free(a);
  gsl_vector_free(x);
  gsl_vector_free(yp);
  gsl_vector_free(ys);
  gsl_rng_free(r);

  return 0;
}
