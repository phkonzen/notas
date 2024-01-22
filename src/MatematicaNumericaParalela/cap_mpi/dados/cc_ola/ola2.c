#include <stdio.h>

// API MPI
#include <mpi.h>

int main() {

  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // número total de processos
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // ID (rank) do processo
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  // Escreve mensagem
  printf("Olá! Eu sou o processo %d/%d.\n",
	        world_rank, world_size);

  // Finaliza o MPI
  MPI_Finalize();
}
