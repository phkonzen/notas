#include <stdio.h>
#include <math.h>

// API MPI
#include <mpi.h>

int main(int argc, char** argv) {
  
  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // número total de processos
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // ID (rank) do processo
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  double x;

  if (world_rank == 0)
    x = M_PI;

  MPI_Bcast (&x, 1, MPI_DOUBLE,
	     0, MPI_COMM_WORLD);

  printf ("Processo %d x = %f\n",
	  world_rank, x);  

  // Finaliza o MPI
  MPI_Finalize();

  return 0;
}
