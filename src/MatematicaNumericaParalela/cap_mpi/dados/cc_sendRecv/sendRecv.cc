#include <stdio.h>

// API MPI
#include <mpi.h>

int main (int argc, char** argv) {
  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // numero total de processos
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // ID (rank) do processo
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  if (world_rank == 0) {
    double x = 3.1416;
    MPI_Send (&x, 1, MPI_DOUBLE, 1,
	      0, MPI_COMM_WORLD);
  } else {
    double y;
    MPI_Recv (&y, 1, MPI_DOUBLE, 0,
	      0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    printf ('Processo 1 recebeu o '\
	    'numero %f do processo 0.\n', y);
  }
    

  // Finaliza o MPI
  MPI_Finalize ();

  return 0;
}
