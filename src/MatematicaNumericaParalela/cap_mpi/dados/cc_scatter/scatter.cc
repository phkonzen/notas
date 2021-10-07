#include <stdio.h>
#include <stdlib.h>
#include <math.h>

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

  const size_t n = 10;
  double *v = NULL; 

  if (world_rank == 0) {
    v = (double*) malloc (n * sizeof(double));

    for (size_t i=0; i<n; i++)
      v[i] = i+1;
  }

  size_t my_n = n/world_size;  
  double *my_v = (double*) malloc (my_n * sizeof(double));

  MPI_Scatter (v, my_n, MPI_DOUBLE,
	       my_v, my_n, MPI_DOUBLE,
	       0, MPI_COMM_WORLD);

  double soma = 0.0;
  for (size_t i=0; i<my_n; i++) {
    soma += my_v[i];
  }

  printf ("Processo %d soma = %f\n",
  	  world_rank, soma);

  free (v);
  free (my_v);

  // Finaliza o MPI
  MPI_Finalize();

  return 0;
}
