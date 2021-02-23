#include <omp.h>
#include <stdio.h>
#include <ctime>
#include <algorithm>

#include <gsl/gsl_matrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_blas.h>

int main(int argc, char *argv[]) {

  int n = 5000;
  //int n = 5;

  // matrizes a=u, l
  gsl_matrix *u = gsl_matrix_alloc(n,n);
  gsl_matrix *l = gsl_matrix_alloc(n,n);

  // gerador randômico
  gsl_rng *rng = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(rng, time(NULL));

  // inicialização
  printf("Inicializando ... \n");
#pragma omp parallel for
  for (int i=0; i<n; i++) {
    for (int j=0; j<i; j++) {
      int sig = 1;
      if (gsl_rng_uniform(rng) >= 0.5)
	sig = -1;
      gsl_matrix_set(u, i, j,
		     sig*gsl_rng_uniform(rng));
      gsl_matrix_set(u, j, i,
		     gsl_matrix_get(u, i, j));
    }
    int sig = 1;
    if (gsl_rng_uniform(rng) >= 0.5)
      sig = -1;
    gsl_matrix_set(u, i, i,
		   sig*gsl_rng_uniform_pos(rng));
  }
  printf("feito.\n");

  // for (int i=0; i<n; i++) {
  //   for (int j=0; j<n; j++)
  //     printf("%1.1f ", gsl_matrix_get(u,i,j));
  //   printf("\n");
  // }
  // printf("\n");


  printf("LU parallel ... \n");
  time_t t = time(NULL);
  #pragma omp parallel
  for (int i=0; i<n; i++) {
    
    #pragma omp single nowait
    gsl_matrix_set(l, i, i, 1.0);
    
    for (int j=i+1; j<n; j++) {
      
      #pragma omp single nowait
      gsl_matrix_set(l, j, i,
		     gsl_matrix_get(u, j, i)/
		     gsl_matrix_get(u, i, i));

      #pragma omp for schedule(static, 16)
      for (int k=i; k<n; k++)
	gsl_matrix_set(u, j, k,
		       gsl_matrix_get(u, j, k) -
		       gsl_matrix_get(l, j, i) *
		       gsl_matrix_get(u, i, k));
    }
  }
  t = time(NULL)-t;
  printf("feito. %ld s\n", t);

  // for (int i=0; i<n; i++) {
  //   for (int j=0; j<n; j++)
  //     printf("%1.1f ", gsl_matrix_get(l,i,j));
  //   printf("\n");
  // }
  // printf("\n");
  // for (int i=0; i<n; i++) {
  //   for (int j=0; j<n; j++)
  //     printf("%1.1f ", gsl_matrix_get(u,i,j));
  //   printf("\n");
  // }
  //   printf("\n");
  // gsl_matrix *a = gsl_matrix_alloc(n,n);
  // gsl_blas_dgemm(CblasNoTrans,CblasNoTrans,
  // 		 1.0,l,u,0.0,a);
  // for (int i=0; i<n; i++) {
  //   for (int j=0; j<n; j++)
  //     printf("%1.1f ", gsl_matrix_get(a,i,j));
  //   printf("\n");
  // }
  

  gsl_matrix_free(u);
  gsl_matrix_free(l);
  gsl_rng_free(rng);
  
  return 0;
}
