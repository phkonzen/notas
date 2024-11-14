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

  // identificação (rank) do processo
  int pid;
  MPI_Comm_rank(MPI_COMM_WORLD, &pid);

  // limites globais de integração
  double a = 0;
  double b = 9999999;

  // limites locais de integração
  double a1 = a + pid*(b-a)/nproc;
  double b1 = a + (pid+1)*(b-a)/nproc;

  // subintervalos da quadratura local
  int n = 99999998;
  double h = (b1-a1)/n;

  // computa s0
  double s0 = 0;
  for (int j=1; j<n/2; j++)
    s0 += fun(a1+2*j*h);

  // computa s1
  double s1 = 0;
  for (int j=1; j<=n/2; j++)
    s1 += fun(a1+(2*j-1)*h);

  // solução na região local
  double s = h/3*(fun(a1)+2*s0+4*s1+fun(b1));

  // soma as soluções locais e aloca no pid=0
  double ss = 0;
  MPI_Reduce(&s, &ss, 1, MPI_DOUBLE, MPI_SUM, 0,
	     MPI_COMM_WORLD);

  // imprime a solução
  if (pid == 0)
    std::cout << "Simpson = " << ss << std::endl
	      << "Analítica = "
	      << b*sin(b)+cos(b)-a*sin(a)-cos(a) << std::endl;

  // Finaliza o MPI
  MPI_Finalize();

  return 0;
}
