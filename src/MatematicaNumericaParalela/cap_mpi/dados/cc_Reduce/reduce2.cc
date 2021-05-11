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

  double x[2] = {double (rand ()) / RAND_MAX,
		 double (rand ()) / RAND_MAX};

  printf ('%d: %f %f\n',
	  world_rank, x[0], x[1]);

  double y[2];
  MPI_Reduce (&x, &y, 2, MPI_DOUBLE,
	      MPI_SUM, 0, MPI_COMM_WORLD);

  if (world_rank == 0)
    printf ('Vetor soma = %f %f\n',
	    y[0], y[1]);
  // Finaliza o MPI
  MPI_Finalize();

  return 0;
}
