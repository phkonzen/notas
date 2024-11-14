#include <mpi.h>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>

// função objetivo
double fun(double x, double y) {
  return exp(-(x*x+y*y));
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
  std::srand(std::time(NULL)+pid);
  
  // num. de exemplos
  int ns = 99999999;

  // Soma de Monte Carlo
  double s = 0;
  for (int i=0; i<ns; i++) {
    double xs = double(std::rand())/RAND_MAX;
    double ys = double(std::rand())/RAND_MAX;
    s += fun(xs,ys);
  }
  s /= ns;
  
  // Reduce para o pid 0
  double ss;
  MPI_Reduce(&s, &ss, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

  // imprime a solução
  if (pid == 0) {
    std::cout << RAND_MAX << std::endl; 
    std::cout << ss/nproc << std::endl;
  }

  // Finaliza o MPI
  MPI_Finalize();
  
  return 0;
}
