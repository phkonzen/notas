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

  // gerador randômico
  gsl_rng *rng = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(rng, time(NULL));

  // inicialização
  printf("Inicializando ... \n");

  int sig;
  for (int i=0; i<n; i++) {
    for (int j=0; j<i; j++) {
      if (gsl_rng_uniform(rng) >= 0.5)
	sig = 1;
      else
	sig = -1;
      gsl_spmatrix_set(a, i, j,
	sig*gsl_rng_uniform_pos(rng));
    }
    gsl_spmatrix_set(a, i, i,
		     n + sig*gsl_rng_uniform_pos(rng));
    if (gsl_rng_uniform(rng) >= 0.5)
      sig = 1;
    else
      sig = -1;
    gsl_vector_set(b, i,
		   sig*gsl_rng_uniform(rng));
  }
  printf("feito.\n");

  printf("Salvando o sistema ...\n");
  FILE *fpa;
  fpa = fopen("a.bck","w");
  gsl_spmatrix_fwrite(fpa, a);
  fclose(fpa);

  FILE *fpb;
  fpb = fopen("b.bck","w");
  gsl_vector_fwrite(fpb, b);
  fclose(fpb);
  printf("feito.\n");


  gsl_spmatrix_free(a);
  gsl_vector_free(b);
  gsl_rng_free(rng);
  
  return 0;
}
