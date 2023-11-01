#include <stdio.h>

// GSL
#include <gsl/gsl_vector.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_linalg.h>

int main()
{
  // matriz dos coefs
  gsl_matrix *A = gsl_matrix_alloc(3, 3);
  
  gsl_matrix_set(A, 0, 0, 1.);
  gsl_matrix_set(A, 0, 1, -1.);
  gsl_matrix_set(A, 0, 2, 2.);

  gsl_matrix_set(A, 1, 0, 2.);
  gsl_matrix_set(A, 1, 1, 1.);
  gsl_matrix_set(A, 1, 2, -1.);

  gsl_matrix_set(A, 2, 0, -1.);
  gsl_matrix_set(A, 2, 1, 1.);
  gsl_matrix_set(A, 2, 2, 1.);

  // vetor dos termos consts
  gsl_vector *b = gsl_vector_alloc(3);

  gsl_vector_set(b, 0, -6.);
  gsl_vector_set(b, 1, 1.);
  gsl_vector_set(b, 2, 0.);

  // decomposição LU
  // PA = LU
  gsl_permutation *p = gsl_permutation_alloc(3);
  int signum;
  gsl_linalg_LU_decomp(A, p, &signum);

  // solução
  gsl_vector *x = gsl_vector_alloc(3);
  gsl_linalg_LU_solve(A, p, b, x);

  // imprime a solução
  for (int i=0; i<3; ++i)
    printf("x_%d = %g\n", i, gsl_vector_get(x, i));

  gsl_matrix_free(A);
  gsl_vector_free(b);
  gsl_permutation_free(p);
  gsl_vector_free(x);
  
  return 0;
}
