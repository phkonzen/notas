#include <stdio.h>

// GSL
#include <gsl/gsl_math.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_blas.h>

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

  // vetor solução ?
  gsl_vector *x = gsl_vector_alloc(3);

  gsl_vector_set(x, 0, -1.);
  gsl_vector_set(x, 1, 1.);
  gsl_vector_set(x, 2, -2.);

  // verificação
  // y = Ax
  gsl_vector *y = gsl_vector_alloc(3);
  gsl_blas_dgemv(CblasNoTrans, 1., A, x, 0., y);

  // y - b
  gsl_vector_sub(y, b);
  
  if (gsl_blas_dnrm2(y) < 1e-14)
    printf("x é solução do sistema.\n");
  else
    printf("x não é solução do sistema.\n");

  gsl_matrix_free(A);
  gsl_vector_free(b);
  gsl_vector_free(x);
  gsl_vector_free(y);
  
  return 0;
}
