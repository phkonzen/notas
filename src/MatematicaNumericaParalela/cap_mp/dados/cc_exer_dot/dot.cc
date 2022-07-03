#include <stdio.h>

// OpenMP API
#include <omp.h>

// Armadillo
#include <armadillo>

int main(int argc, char *argv[]) {

  // n
  int n = 10;

  // inicializa o gerador randômico
  arma::arma_rng::set_seed_random();

  // aloca os vetores
  arma::vec u(n, arma::fill::randu);
  arma::vec v(n, arma::fill::randu);

  arma::cout << u << std::endl;
  arma::cout << v << std::endl;

  // num de threads
  int nth = 2;
  omp_set_num_threads(nth);
    
  // produtos parciais
  arma::vec s(nth);

  // regiao paralela
  #pragma omp parallel				
  {
    // thread id
    int tid = omp_get_thread_num();

    // partição dos vetores
    int ini = n/nth*tid;
    int fim = (tid != nth-1) ? n/nth*(tid+1)-1 : n-1;

    // produto escalar parcial
    s(tid) = arma::dot(u.subvec(ini,fim),
		       v.subvec(ini,fim));
    arma::cout << tid << ": " << s(tid);
  }
  
  return 0;
}
