#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

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

  // cronometro
  time_t init = time (NULL);

  // semente do gerador randomico
  srand (init + world_rank);
  
  // max. of 3 segundos
  size_t espera = rand() % 3000000;

  usleep (espera);
  
  printf ('%d chegou na barreira: %ld s.\n',
	  world_rank, (time (NULL) - init));
  
  MPI_Barrier (MPI_COMM_WORLD);
  
  printf ('%d saiu da  barreira: %ld s.\n',
	  world_rank, (time (NULL) - init));
  

  // Finaliza o MPI
  MPI_Finalize();

  return 0;
}
