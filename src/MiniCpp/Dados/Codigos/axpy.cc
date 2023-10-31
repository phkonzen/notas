#include <stdio.h>

// GSL vetores
#include <gsl/gsl_vector.h>
// GSL BLAS
#include <gsl/gsl_blas.h>

int main() {

  // alpha
  double alpha = 2.;
  
  // u
  gsl_vector *u = gsl_vector_alloc(3);
  gsl_vector_set(u, 0, 1.);
  gsl_vector_set(u, 1, -2.);
  gsl_vector_set(u, 2, 0.5);

  // v
  gsl_vector *v = gsl_vector_alloc(3);
  gsl_vector_set(v, 0, 2.);
  gsl_vector_set(v, 1, 1.);
  gsl_vector_set(v, 2, -1.5);

  // w = alpha*u + v
  // alloc w
  gsl_vector *w = gsl_vector_alloc(3);
  // copy w = v
  gsl_vector_memcpy(w, v);
  // w = alpha*u + w
  gsl_blas_daxpy(alpha, u, w);
  
  // imprime
  for (int i=0; i<3; ++i) {
    printf("w_%d = %g\n", i, gsl_vector_get(w, i));
  }
  
  // liberação de memória
  gsl_vector_free(v);
}
