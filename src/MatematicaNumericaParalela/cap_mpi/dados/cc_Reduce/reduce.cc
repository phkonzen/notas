#include <stdio.h>
#include <stdlib.h>

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

  double x = double (rand ()) / RAND_MAX;

  printf ("%d: %f\n",
	  world_rank, x);

  double y;
  MPI_Reduce (&x, &y, 1, MPI_DOUBLE,
	      MPI_MAX, 0, MPI_COMM_WORLD);

  if (world_rank == 0)
    printf ("Max. entre os numeros = %f\n",
	    y);
  // Finaliza o MPI
  MPI_Finalize();

  return 0;
}
