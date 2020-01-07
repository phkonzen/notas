#include <mpi.h>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <assert.h>

// função objetivo
double fun(double x) {
  return x*exp(-x*x);
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

  // limites globais de integração
  double a = 0;
  double b = 1;

  // limites locais de integração
  double a1 = a + pid*(b-a)/nproc;
  double b1 = a + (pid+1)*(b-a)/nproc;
  int n = 2000;

  double h = (b1-a1)/n;

  double s1 = 0;
  for (int j=1; j<n/2; j++)
    s1 += fun(a1+2*j*h);

  double s2 = 0;
  for (int j=1; j<=n/2; j++)
    s2 += fun(a1+(2*j-1)*h);

  double s = h/3*(fun(a1)+2*s1+4*s2+fun(b1));

  double ss = 0;
  MPI_Reduce(&s, &ss, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

  if (pid == 0)
    std::cout << std::setprecision(25)
	      << ss
	      << std::endl
	      << -exp(-b*b)/2 + exp(-a*a)/2
	      << std::endl;

  MPI_Finalize();

  return 0;
}
