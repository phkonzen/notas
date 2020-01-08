#include <mpi.h>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <assert.h>

// função objetivo
double fun(double x) {
  return x*cos(x);
}

// código principal
int main() {

  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // Número de processos
  int nproc;
  MPI_Comm_size(MPI_COMM_WORLD, &nproc);

  // aborta caso nproc != 2
  assert(nproc == 2);
  
  // identificação (rank) do processo
  int pid;
  MPI_Comm_rank(MPI_COMM_WORLD, &pid);

  // limites de integração
  double a = 0;
  double b = 9999999;

  // subintervalos na quadratura
  int n = 999999998;
  double h = (b-a)/n;

  // computa s0
  double s0 = 0;
  if (pid == 0) {
    
    for (int j=1; j<n/2; j++)
      s0 += fun(a+2*j*h);

    // envia s0 para pid=1
    MPI_Send(&s0, 1, MPI_DOUBLE, 1,
	     0, MPI_COMM_WORLD);
  }

  // computa s1
  double s1 = 0;
  if (pid == 1) {
    
    for (int j=1; j<=n/2; j++)
      s1 += fun(a+(2*j-1)*h);

    // recebe s0 do pid=1
    MPI_Recv(&s0, 1, MPI_DOUBLE, 0,
	     0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    // imprime a solução
    std::cout << "simpson = "
	      << h/3*(fun(a)+2*s0+4*s1+fun(b))
	      << std::endl
	      << "analítica = "
	      << b*sin(b)+cos(b)-(a*sin(a)+cos(a))
	      << std::endl;
  }

  // finaliza MPI
  MPI_Finalize();

  return 0;
}
