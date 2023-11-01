#include <stdio.h>

// GSL
#include <gsl/gsl_math.h>
#include <gsl/gsl_matrix.h>

int main()
{
  // alocação
  gsl_matrix *A = gsl_matrix_alloc(3, 4);

  // população
  gsl_matrix_set(A, 0, 0, 1.5);
  gsl_matrix_set(A, 0, 1, -1.);
  gsl_matrix_set(A, 0, 2, M_PI);
  gsl_matrix_set(A, 0, 3, 2.3);

  gsl_matrix_set(A, 1, 0, cbrt(25.));
  gsl_matrix_set(A, 1, 1, 2.1);
  gsl_matrix_set(A, 1, 2, -3.5);
  gsl_matrix_set(A, 1, 3, 3.);

  gsl_matrix_set(A, 2, 0, log10(15.));
  gsl_matrix_set(A, 2, 1, 0.);
  gsl_matrix_set(A, 2, 2, pow(2.5, 3.));
  gsl_matrix_set(A, 2, 3, -1.7);

  // imprime
  printf("A = \n");
  for (int i=0; i<A->size1; ++i) {
    for (int j=0; j<A->size2; ++j)
      printf("%g ", gsl_matrix_get(A, i, j));
    printf("\n");
  }

  gsl_matrix_free(A);
  return 0;
}
