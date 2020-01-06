#include <mpi.h>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <gsl/gsl_rng.h>

// função objetivo
double fun(double x) {
  return 2/sqrt(M_PI)*exp(-x*x);
}

// código principal
int main() {

  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // Número de processos
  int nproc;
  MPI_Comm_size(MPI_COMM_WORLD, &nproc);

  // identificação (rank) do processo
  int pid;
  MPI_Comm_rank(MPI_COMM_WORLD, &pid);

  // inicializa o gerador randômico
  const gsl_rng_type * T;
  gsl_rng * r;
  gsl_rng_env_setup();
  T = gsl_rng_default;
  r = gsl_rng_alloc (T);
  gsl_rng_set(r, std::time(NULL)+pid);

  // num. de exemplos
  int ns = 99999999;

  // Soma de Monte Carlo
  double s = 0;
  for (int i=0; i<ns; i++) {
    double xs = gsl_rng_uniform (r);
    s += fun(xs);
  }
  s /= ns;

  gsl_rng_free (r);
  
  // Reduce para o pid 0
  double ss;
  MPI_Reduce(&s, &ss, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

  // imprime a solução
  if (pid == 0)
    std::cout << ss/nproc << std::endl;

  // Finaliza o MPI
  MPI_Finalize();
  
  return 0;
}
