#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <omp.h>

// GSL
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_rng.h>

using namespace std;

int main (int arc, char *argv[]) {
  const size_t n = 1000;
  const size_t m = 1000;
  gsl_matrix *a = gsl_matrix_alloc(n, n);
  gsl_matrix *b = gsl_matrix_alloc(n, n);

  // c parallel
  gsl_matrix *cp = gsl_matrix_alloc(n, n);

  // c serial
  gsl_matrix *cs = gsl_matrix_alloc(n, n);

  gsl_rng *r = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(r, time(NULL));

  for (int i=0; i<n; i++)
    for (int j=0; j<n; j++) {
      gsl_matrix_set(a, i, j, gsl_rng_uniform(r));
      gsl_matrix_set(b, i, j, gsl_rng_uniform(r));
    }

  time_t t = time(NULL);
  #pragma omp parallel
  {
    int id = omp_get_thread_num();
    int np = omp_get_num_threads();

    int nt = ceil(double(n)/np);

    double ya;
    for (int i=id*nt; i<(id+1)*nt & i<n; i++) {
      gsl_vector_const_view ai = gsl_matrix_const_row(a, i);
      for (int j=0; j<m; j++) {
	gsl_vector_const_view bj = gsl_matrix_const_column(b, j);
      gsl_blas_ddot(&ai.vector, &bj.vector, &ya);
      gsl_matrix_set(cp, i, j, ya);
      }
    }
  }
  time_t tp = (time(NULL) - t);
  printf("Parallel took: %ld s\n", tp);

  t = time(NULL);
  double ya;
  for (int i=0; i<n; i++) {
    gsl_vector_const_view ai = gsl_matrix_const_row(a, i);
    for (int j=0; j<m; j++) {
      gsl_vector_const_view bj = gsl_matrix_const_column(b, j);
      gsl_blas_ddot(&ai.vector, &bj.vector, &ya);
      gsl_matrix_set(cp, i, j, ya);
    }
  }
  time_t ts = time(NULL) - t;
  printf("Serial took: %ld s\n", ts);

  // printf("\n");
  // for (int i=0; i<n; i++) {
  //   for (int j=0; j< m; j++)
  //     printf("%lf ", gsl_matrix_get(cp, i, j));
  //   printf("\n");
  // }

  // printf("\n");
  // for (int i=0; i<n; i++) {
  //   for (int j=0; j< m; j++)
  //     printf("%lf ", gsl_matrix_get(cp, i, j));
  //   printf("\n");
  // }

  
  gsl_matrix_free(a);
  gsl_matrix_free(b);
  gsl_matrix_free(cp);
  gsl_matrix_free(cs);
  gsl_rng_free(r);

  return 0;
}
