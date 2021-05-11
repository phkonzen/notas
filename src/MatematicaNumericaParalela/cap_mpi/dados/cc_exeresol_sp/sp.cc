#include <stdio.h>
#include <assert.h>

// API MPI
#include <mpi.h>

int main(int argc, char** argv) {
  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // numero total de processos
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // verifica o num. de processos
  if (world_size != 2) {
    printf('ERRO! Numero de processos '
	   'deve ser igual 2.\n');
    int errorcode=-1;
    MPI_Abort(MPI_COMM_WORLD, errorcode);
  }

  // ID (rank) do processo
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  int n = 2;
  int m = 3;

  if (world_rank == 0)
    printf('n+m = %d\n', n+m);
  else if (world_rank == 1)
    printf('n*m = %d\n', n*m);

  // Finaliza o MPI
  MPI_Finalize();

  return 0;
}
