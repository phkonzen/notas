#include <stdio.h>
#include <stdlib.h>

#include <omp.h>

#include <math.h>
#include <gsl/gsl_vector.h>

// fonte
double f(double t, double x) {
  return (M_PI*M_PI-1.) * 
         exp(-t) * sin(M_PI * x);
}

int main()
{
  // parâmetros no tempo
  double tf = 1.;
  int nt = 1000;
  double ht = tf / nt;

  // parâmetros no espaço
  int nx = 10;
  double hx = 1./nx;

  // malha
  gsl_vector *x = gsl_vector_alloc(nx+1);
  #pragma omp parallel for
  for (int i = 0; i <= nx; i++) {
    gsl_vector_set(x, i, i*hx);
  }

  gsl_vector *u0 = gsl_vector_alloc(nx+1);
  gsl_vector *u = gsl_vector_calloc(nx+1);

  // inicialização
  double t = 0.;
  #pragma omp parallel for
  for (int i = 0; i <= nx; i++) {
    gsl_vector_set(u0, i, 
                    sin(M_PI *
                    gsl_vector_get(x, i)));
  }

  // armazena malha
  FILE *fx = fopen("results/x.dat", "wb");
  gsl_vector_fwrite(fx, x);
  fclose(fx);

  // armazena solução
  char str[21];
  sprintf(str, "results/u_%06d.dat", 0);
  printf("t = %g, [%s]\n", t, str);

  FILE *fu = fopen(str, "wb");
  gsl_vector_fwrite(fu, u0);
  fclose(fu);

  #pragma omp parallel
  {
    // iteração no tempo
    for (int k=0; k < nt; k++) {
      #pragma omp single
      t += ht;

      #pragma omp for
      for (int i=1; i < nx; i++) {
        gsl_vector_set(u, i,
                        gsl_vector_get(u0, i) +
                        ht/(hx*hx) * (gsl_vector_get(u0, i+1) - 2*gsl_vector_get(u0, i) + gsl_vector_get(u0, i-1)) + ht * 
                        f(t-ht, gsl_vector_get(x, i)));
      }

      #pragma omp single
      {
        sprintf(str, "results/u_%06d.dat", k+1);
        printf("t = %g, [%s]\n", t, str);
        fu = fopen(str, "wb");
        gsl_vector_fwrite(fu, u0);
        fclose(fu);
        
        // u0 = u
        gsl_vector_memcpy(u0, u);
      }

    }
  }
  
  gsl_vector_free(x);
  gsl_vector_free(u);
  gsl_vector_free(u0);
  return 0;
}
