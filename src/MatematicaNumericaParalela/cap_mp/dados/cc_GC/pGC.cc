#include <omp.h>
#include <stdio.h>
#include <time.h>
#include <math.h>

#include <gsl/gsl_matrix.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_rng.h>

int n = 999;
int tmax = 50;
double tol = 1e-8;

// inicializacao
void init(gsl_matrix *a,
	  gsl_vector *b);

// random +/- 1
double randsig(gsl_rng *rng);

// residuo
void residuo(const gsl_matrix *a,
	     const gsl_vector *x,
	     const gsl_vector *b,
	     gsl_vector *r);

// Metodo do Gradiente Conjugado
void pGC(const gsl_matrix *a,
	 const gsl_vector *b,
	 gsl_vector *x);

int main(int argc, char *argv[]) {

  // sistema
  gsl_matrix *a = gsl_matrix_alloc(n,n);
  gsl_vector *b = gsl_vector_alloc(n);

  // incognita
  gsl_vector *x = gsl_vector_alloc(n);

  // inicializacao
  init(a, b);

  // Método do Gradiente Conjugado
  pGC(a, b, x);
  
  gsl_matrix_free(a);
  gsl_vector_free(b);
  gsl_vector_free(x);
  
  return 0;
}

/******************************************
Inicializacao
******************************************/
void init(gsl_matrix *a,
	  gsl_vector *b)
{
  printf("Inicializacao ... \n");
  // gerador randômico
  gsl_rng *rng = gsl_rng_alloc(gsl_rng_default);
  gsl_rng_set(rng, time(NULL));

  // C - Matriz estritamente diagonal positiva
  double sig;
  gsl_matrix *c = gsl_matrix_alloc(n,n);
  #pragma omp parallel for
  for (int i=0; i<n; i++) {
    double aux;
    double s = 0;
    for (int j=0; j<n; j++) {
      aux = gsl_rng_uniform(rng);
      gsl_matrix_set(c, i, j,
		     randsig(rng) * aux);
      s += aux;
    }
    gsl_matrix_set(c, i, i,
		   randsig(rng) * s);
    gsl_vector_set(b, i,
		   randsig(rng) *
		   gsl_rng_uniform(rng));
  }
  // A = C'C: Simétrica positiva definida
  #pragma omp parallel for
  for (int i=0; i<n; i++)
    for (int j=0; j<n; j++) {
      double s;
      gsl_vector_const_view ci =
	gsl_matrix_const_column(c, i);
      gsl_vector_const_view cj =
	gsl_matrix_const_column(c, j);
      gsl_blas_ddot(&ci.vector, &cj.vector, &s);
      gsl_matrix_set(a, i, j, s);
    }

  gsl_rng_free(rng);
  gsl_matrix_free(c);

  printf("feito.\n");
}
/*****************************************/

/*****************************************
Sinal randomico
*****************************************/
double randsig(gsl_rng *rng)
{
  double signal = 1.0;
  if (gsl_rng_uniform(rng) >= 0.5)
	signal = -1.0;
  return signal;
}
/***************************************/

/***************************************
residuo
***************************************/
void residuo(const gsl_matrix *a,
	     const gsl_vector *x,
	     const gsl_vector *b,
	     gsl_vector *r)
{
  #pragma omp parallel for
  for (int i=0; i<n; i++) {
    double s = 0;
    for (int j=0; j<n; j++)
      s += gsl_matrix_get(a, i, j) *
	gsl_vector_get(x, j);
    gsl_vector_set(r, i,
		   s - gsl_vector_get(b, i));
  }  
}
/*************************************/

/***************************************
Metodo do Gradiente Conjugado
***************************************/
void pGC(const gsl_matrix *a,
	 const gsl_vector *b,
	 gsl_vector *x)
{
  gsl_vector *r = gsl_vector_alloc(n);
  gsl_vector *d = gsl_vector_alloc(n);
  gsl_vector *ad = gsl_vector_alloc(n);

  // x = 0
  gsl_vector_set_zero(x);

  // r = Ax - b
  residuo(a, x, b, r);

  // d = r
  gsl_vector_memcpy(d, r);

  for (int t=0; t<tmax; t++) {
    // r.d, Ad, dAd
    double rd = 0;
    double dAd = 0;
    #pragma omp parallel for reduction(+:rd,dAd)
    for (int i=0; i<n; i++) {
      rd += gsl_vector_get(r, i) *
	gsl_vector_get(d, i);
      double adi = 0;
      for (int j=0; j<n; j++)
	adi += gsl_matrix_get(a, i, j) *
	  gsl_vector_get(d, j);
      gsl_vector_set(ad, i, adi);
      dAd += gsl_vector_get(d, i) * adi;
    }
    
    // alpha
    double alpha = rd/dAd;

    // x = x - alpha*d
    #pragma omp parallel for
    for (int i=0; i<n; i++)
      gsl_vector_set(x, i,
		     gsl_vector_get(x, i) -
		     alpha *
		     gsl_vector_get(d, i));

    // residuo
    residuo(a, x, b, r);

    // rAd
    double rAd = 0;
    #pragma omp parallel for reduction(+:rAd)
    for (int i=0; i<n; i++)
      rAd += gsl_vector_get(r, i) *
	gsl_vector_get(ad, i);

    // beta
    double beta = rAd/dAd;

    // d
    #pragma omp parallel for
    for (int i=0; i<n; i++)
      gsl_vector_set(d, i,
		     beta *
		     gsl_vector_get(d, i) -
		     gsl_vector_get(r, i));

    // criterio de parada
    // ||r||_2 < tol
    double crt = 0;
    #pragma omp parallel for reduction(+: crt)
    for (int i=0; i<n; i++)
      crt += gsl_vector_get(r, i) *
	gsl_vector_get(r, i);
    crt = sqrt(crt);
    printf("Iter. %d: %1.1e\n", t, crt);
    if (crt < tol)
      break;
  }

  gsl_vector_free(r);
  gsl_vector_free(d);
  gsl_vector_free(ad);
  
}
/*************************************/
