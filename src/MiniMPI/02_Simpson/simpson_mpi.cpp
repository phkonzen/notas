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

  assert(nproc == 2);
  
  // identificação (rank) do processo
  int pid;
  MPI_Comm_rank(MPI_COMM_WORLD, &pid);

  
  double a = 0;
  double b = 9999999;
  int n = 999999998;

  double h = (b-a)/n;

  double s1 = 0;
  if (pid == 0) {
    for (int j=1; j<n/2; j++)
      s1 += fun(a+2*j*h);

    MPI_Send(&s1, 1, MPI_DOUBLE, 1, 0, MPI_COMM_WORLD);
  }

  double s2 = 0;
  if (pid == 1) {
    for (int j=1; j<=n/2; j++)
      s2 += fun(a+(2*j-1)*h);

    MPI_Recv(&s1, 1, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

      std::cout << std::setprecision(10)
		<< h/3*(fun(a)+2*s1+4*s2+fun(b))
		<< std::endl
		<< b*sin(b)+cos(b)-(a*sin(a)+cos(a))
		<< std::endl;
  }

  MPI_Finalize();

  return 0;
}
