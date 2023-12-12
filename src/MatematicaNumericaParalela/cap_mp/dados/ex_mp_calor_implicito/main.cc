#include <stdio.h>
#include <stdlib.h>

#include <omp.h>

#include <math.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_blas.h>

// fonte
double f(double t, double x) {
  return (M_PI*M_PI-1.) * 
         exp(-t) * sin(M_PI * x);
}

int main()
{
  // parâmetros no tempo
  double tf = 1.;
  int nt = 100;
  double ht = tf / nt;

  // parâmetros no espaço
  int nx = 10;
  double hx = 1./nx;

  // parâmetros Jacobi
  int maxit = 1000;
  double tol = 1.49e-8;

  // auxiliar
  double r = ht/(hx*hx);

  // malha
  gsl_vector *x = gsl_vector_alloc(nx+1);
  #pragma omp parallel for
  for (int i = 0; i <= nx; i++) {
    gsl_vector_set(x, i, i*hx);
  }

  gsl_vector *u0 = gsl_vector_alloc(nx+1);
  gsl_vector *u = gsl_vector_calloc(nx+1);

  // auxiliares
  double norm;
  gsl_vector *u00 = gsl_vector_alloc(nx+1);
  gsl_vector *diff = gsl_vector_calloc(nx+1);

  // inicialização
  double t = 0.;
  #pragma omp parallel for
  for (int i = 0; i <= nx; i++) {
    gsl_vector_set(u0, i, 
                    sin(M_PI *
                    gsl_vector_get(x, i)));
  }
  
  // u00 = u0
  gsl_vector_memcpy(u00, u0);

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
      {
        t += ht;
        printf("%d: t = %g\n", k+1, t);
      }

      // iteração de Jacobi
      for (int it=0; it < maxit; it++) {

        #pragma omp for
        for (int i=1; i < nx; i++) {
          gsl_vector_set(u, i, 1./(2.*r + 1.) *
                             (r * (gsl_vector_get(u00, i-1) + 
                                   gsl_vector_get(u00, i+1)) +
                             gsl_vector_get(u0, i) +
                             + ht * f(t, gsl_vector_get(x, i))));
                          
          gsl_vector_set(diff, i, gsl_vector_get(u, i) -
                                  gsl_vector_get(u00, i));
        }

        #pragma omp single
        {
          norm = gsl_blas_dnrm2(diff);
          printf("\t%d: norm=%.2e\n", it, norm);

          gsl_vector_memcpy(u00, u);
        }

        if (norm < tol) {
            break;
        }

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
  gsl_vector_free(u00);
  gsl_vector_free(diff);

  return 0;
}
