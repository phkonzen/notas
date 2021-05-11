#include <omp.h>
#include <stdio.h>
#include <ctime>
#include <algorithm>

#include <gsl/gsl_spmatrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_rng.h>

int np, pid;
int ini, fim;
#pragma omp threadprivate(np,pid,ini,fim)

int main(int argc, char *argv[]) {

  int n = 9999;

  // vetores
  gsl_spmatrix *a = gsl_spmatrix_alloc(n,n);
  gsl_vector *b = gsl_vector_alloc(n);
  gsl_vector *x = gsl_vector_alloc(n);

  // inicializacao
  printf('Inicializando ... \n');

  for (int i=0; i<n; i++) {
    for (int j=0; j<i; j++) {
      gsl_spmatrix_set(a, i, j,
		       pow(-1.0,i+j)*(i+j)/(i*j+1));
    }
    gsl_spmatrix_set(a, i, i,
  		     (pow(i-n/2,2)+1)*2/n);
    gsl_vector_set(b, i,
  		   pow(-1.0,i)/(i+1));
  }

  printf('feito.\n');

  printf('Executando em paralelo ... \n');

  time_t t = time(NULL);
  #pragma omp parallel
  {
    np = omp_get_num_threads();
    pid = omp_get_thread_num();

    ini = pid*n/np;
    fim = (pid+1)*n/np;
    if (pid == np-1)
      fim = n;
  }

  for (int i=0; i<n; i++) {
    double s = 0;
    #pragma omp parallel reduction(+: s)
    {
      for (int j=std::max(0,ini); j<i and j<fim; j++)
	s += gsl_spmatrix_get(a,i,j) *
	     gsl_vector_get(x,j);
    }
    gsl_vector_set(x, i,
		   (gsl_vector_get(b,i) - s) /
		   gsl_spmatrix_get(a,i,i));
  }

  t = time(NULL)-t;

  printf('feito. %ld s\n', t);


  gsl_spmatrix_free(a);
  gsl_vector_free(b);
  gsl_vector_free(x);
  
  return 0;
}
