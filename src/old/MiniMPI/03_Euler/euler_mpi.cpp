#include <mpi.h>
#include <iostream>
#include <math.h>
#include <vector>
#include <assert.h>

int main() {

  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // Número de processos
  int nproc;
  MPI_Comm_size(MPI_COMM_WORLD, &nproc);

  // verifica nproc == 3
  assert(nproc == 3);

  // identificação (rank) do processo
  int pid;
  MPI_Comm_rank(MPI_COMM_WORLD, &pid);


  // declara sol. inicial global
  std::vector<double> u0 = {1,1,-1};

  // declara sol. corrente local
  double u;

  // passos no tempo
  int n = 100000000;
  double h = 1.0/n;

  // tempo inicial
  double t0=0;

  // iterações de Euler
  for (int i=0; i<n; i++) {

    if (pid == 0) {
      u = u0[0] + h*(u0[1]-u0[2]+t0);

      u0[0] = u;

      MPI_Recv(&u0[1], 1, MPI_DOUBLE, 1,
	       0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

      MPI_Recv(&u0[2], 1, MPI_DOUBLE, 2,
	       0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    }

    if (pid == 1) {
      u = u0[1] + h*3*t0*t0;

      u0[1] = u;

      MPI_Send(&u, 1, MPI_DOUBLE, 0,
	       0, MPI_COMM_WORLD);

      MPI_Send(&u, 1, MPI_DOUBLE, 2,
	       0, MPI_COMM_WORLD);
    }

    if (pid == 2) {
      u = u0[2] + h*(u0[1]+exp(-t0));

      u0[2] = u;
      
      MPI_Recv(&u0[1], 1, MPI_DOUBLE, 1,
	       0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

      MPI_Send(&u, 1, MPI_DOUBLE, 0,
	       0, MPI_COMM_WORLD);
    }

    t0 += h;
  }

  // imprime a sol.
  if (pid == 0)
    std::cout << "sol. t = "
	      << t0 << std::endl;

  std::cout << " u " << pid+1 << " = "
	    << u << std::endl;

  // Finaliza o MPI
  MPI_Finalize();
    
  return 0;
}
