#include <omp.h>
#include <stdio.h>
#include <ctime>
#include <algorithm>

#include <gsl/gsl_matrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_blas.h>

int main(int argc, char *argv[]) {

  int n = 2000;

  gsl_matrix *a = gsl_matrix_alloc(n,n);
  gsl_matrix *u = gsl_matrix_alloc(n,n);
  gsl_matrix *l = gsl_matrix_alloc(n,n);

  // gerador randômico
  gsl_rng *rng = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(rng, time(NULL));

  // inicialização
  printf('Inicializando ... \n'); 
  for (int i=0; i<n; i++) {
    for (int j=0; j<i; j++) {
      int sig = 1;
      if (gsl_rng_uniform(rng) >= 0.5)
	sig = -1;
      gsl_matrix_set(a, i, j,
		     sig*gsl_rng_uniform(rng));
      gsl_matrix_set(a, j, i,
		     gsl_matrix_get(a, i, j));
    }
    int sig = 1;
    if (gsl_rng_uniform(rng) >= 0.5)
      sig = -1;
    gsl_matrix_set(a, i, i,
  		     sig*gsl_rng_uniform_pos(rng));
  }
  printf('feito.\n');

  // U = A
  gsl_matrix_memcpy(u,a);
  // L = I
  gsl_matrix_set_identity(l);

  printf('LU serial ... \n');
  time_t t = time(NULL);
  for (int k=0; k<n-1; k++) {
    for (int i=k+1; i<n; i++) {
	gsl_matrix_set(l, i, k,
		     gsl_matrix_get(u, i, k)/
		     gsl_matrix_get(u, k, k));
      for (int j=k; j<n; j++) {
	gsl_matrix_set(u, i, j,
		       gsl_matrix_get(u, i, j) -
		       gsl_matrix_get(l, i, k) *
		       gsl_matrix_get(u, k, j));
      }
    }
  }
  t = time(NULL)-t;
  printf('feito. %ld s\n\n', t);


  gsl_matrix_memcpy(u,a);
  printf('LU parallel ... \n');
  t = time(NULL);
  for (int k=0; k<n-1; k++) {
    #pragma omp parallel for
    for (int i=k+1; i<n; i++) {
      gsl_matrix_set(l, i, k,
  		     gsl_matrix_get(u, i, k)/
  		     gsl_matrix_get(u, k, k));
      for (int j=k; j<n; j++) {
  	gsl_matrix_set(u, i, j,
  		       gsl_matrix_get(u, i, j) -
  		       gsl_matrix_get(l, i, k) *
  		       gsl_matrix_get(u, k, j));
      }
    }
  }
  t = time(NULL)-t;
  printf('feito. %ld s\n\n', t);

  
  // for (int i=0; i<n; i++) {
  //   for (int j=0; j<n; j++)
  //     printf('%1.1f ', gsl_matrix_get(a,i,j));
  //   printf('\n');
  // }
  // printf('\n');
  // printf('l=\n');
  // for (int i=0; i<n; i++) {
  //   for (int j=0; j<n; j++)
  //     printf('%1.1f ', gsl_matrix_get(l,i,j));
  //   printf('\n');
  // }
  // printf('\n');
  // printf('u=\n');
  // for (int i=0; i<n; i++) {
  //   for (int j=0; j<n; j++)
  //     printf('%1.1f ', gsl_matrix_get(u,i,j));
  //   printf('\n');
  // }
  // printf('\n');
  // printf('a=\n');
  // gsl_matrix *aa = gsl_matrix_alloc(n,n);
  // gsl_blas_dgemm(CblasNoTrans,CblasNoTrans,
  // 		 1.0,l,u,0.0,aa);
  // for (int i=0; i<n; i++) {
  //   for (int j=0; j<n; j++)
  //     printf('%1.1f ', gsl_matrix_get(aa,i,j));
  //   printf('\n');
  // }
  // gsl_matrix_free(aa);
  

  gsl_matrix_free(a);
  gsl_matrix_free(u);
  gsl_matrix_free(l);
  gsl_rng_free(rng);
  
  return 0;
}
