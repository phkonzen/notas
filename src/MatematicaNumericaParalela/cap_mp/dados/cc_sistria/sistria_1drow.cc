#include <omp.h>
#include <stdio.h>
#include <ctime>
#include <algorithm>

#include <gsl/gsl_spmatrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_rng.h>

int main(int argc, char *argv[]) {

  int n = 9999;

  // vetores
  gsl_spmatrix *a = gsl_spmatrix_alloc(n,n);
  gsl_vector *b = gsl_vector_alloc(n);
  gsl_vector *x = gsl_vector_alloc(n);

  // // gerador randômico
  // gsl_rng *rng = gsl_rng_alloc(gsl_rng_default);
  // gsl_rng_set(rng, time(NULL));

  // inicialização
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

  // gsl_spmatrix_realloc(n*n/2+n, a);
  
  // FILE *fpa;
  // fpa = fopen('a.gsl','r');
  // gsl_spmatrix_fread(fpa, a);
  // fclose(fpa);

  // printf('%f\n',gsl_spmatrix_get(a,1,1));

  // FILE *fpb;
  // fpb = fopen('b.gsl','r');
  // gsl_vector_fread(fpb, b);
  // fclose(fpb);

  printf('feito.\n');

  printf('Executando em paralelo ... \n');

  time_t t = time(NULL);
  double s;
  #pragma omp parallel
  {
    int np = omp_get_num_threads();
    int pid = omp_get_thread_num();

    int ini = pid*n/np;
    int fim = (pid+1)*n/np;
    if (pid == np-1)
      fim = n;

    for (int j=0; j<n; j++) {

      if ((j>= ini) and (j<fim))
	gsl_vector_set(x, j,
		       gsl_vector_get(b, j) /
		       gsl_spmatrix_get(a, j, j));

      for (int i=std::max(j+1,ini); i<n and i<fim; i++)
	gsl_vector_set(b, i,
		       gsl_vector_get(b, i) -
		       gsl_spmatrix_get(a, i, j) *
		       gsl_vector_get(x, j));

    }
    
  }

  t = time(NULL)-t;

  s = 0;
  for (int i=0; i<n; i++)
    s += gsl_vector_get(x,i);
  
  printf('feito: %ld s %f\n', t, s);


  gsl_spmatrix_free(a);
  gsl_vector_free(b);
  gsl_vector_free(x);
  
  return 0;
}
