#include <omp.h>
#include <stdio.h>
#include <ctime>

#include <gsl/gsl_matrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_blas.h>

int main(int argc, char *argv[]) {

  int n = 9999;

  // vetores
  gsl_matrix *a = gsl_matrix_alloc(n,n);
  gsl_vector *x = gsl_vector_alloc(n);
  gsl_vector *y = gsl_vector_alloc(n);

  // gerador randômico
  gsl_rng *rng = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(rng, time(NULL));

  // inicialização
  #pragma omp parallel for
  for (int i=0; i<n; i++) {
    for (int j=0; j<n; j++) {
      gsl_matrix_set(a, i, j, gsl_rng_uniform(rng));
    }
    gsl_vector_set(x, i, gsl_rng_uniform(rng));
  }

  double dot;
  #pragma omp parallel for private(dot)
  for (int i=0; i<n; i++) {
    gsl_vector_const_view ai =
      gsl_matrix_row(a, i);
    gsl_blas_ddot(ai.vector,x,dot);
    gsl_vector_set(y,i,dot);
  }
  

  //gsl_blas_dgemv(CblasNoTrans, 1.0, a, x, 0.0, y);

  // y = A*x
  #pragma omp parallel sections
  {
    #pragma omp section
    {
      gsl_matrix_const_view as1
  	= gsl_matrix_const_submatrix(a,
				     0,0,
				     n/2,n);
      gsl_vector_view ys1
  	= gsl_vector_subvector(y,0,n/2);
      gsl_blas_dgemv(CblasNoTrans,
		     1.0, &as1.matrix, x,
		     0.0, &ys1.vector);
    }
    
    #pragma omp section
    {
      gsl_matrix_const_view as2
  	= gsl_matrix_const_submatrix(a,
				     n/2,0,
				     (n-n/2),n);
      gsl_vector_view ys2
  	= gsl_vector_subvector(y,n/2,(n-n/2));
      gsl_blas_dgemv(CblasNoTrans,
		     1.0, &as2.matrix, x,
		     0.0, &ys2.vector);
    }
  }

  //for (int i=0; i<n; i++)
  //printf("%f\n", gsl_vector_get(y,i));

  gsl_matrix_free(a);
  gsl_vector_free(x);
  gsl_vector_free(y);
  gsl_rng_free(rng);
  
  return 0;
}
