#include <stdio.h>

// GSL const e funs matemáticas
#include <gsl/gsl_math.h>
// GSL vetores
#include <gsl/gsl_vector.h>

int main() {
  // alocação de memória
  gsl_vector *v = gsl_vector_alloc(4);

  // atribuição
  gsl_vector_set(v, 0, sqrt(2.));
  gsl_vector_set(v, 1, 1.);
  gsl_vector_set(v, 2, 3.5);
  gsl_vector_set(v, 3, M_PI);

  // acesso e impressão
  for (int i=0; i<4; ++i) {
    printf("v_%d = %g\n", i, gsl_vector_get(v, i));
  }
  
  // liberação de memória
  gsl_vector_free(v);
}
