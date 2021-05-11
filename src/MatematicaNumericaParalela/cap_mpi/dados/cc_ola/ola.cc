#include <stdio.h>

// API MPI
#include <mpi.h>

int main(int argc, char** argv) {
  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // numero total de processos
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // ID (rank) do processo
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  // Escreve mensagem
  printf('Ola! Eu sou o processo %d/%d.\n',
	 world_rank, world_size);

  // Finaliza o MPI
  MPI_Finalize();

  return 0;
}
