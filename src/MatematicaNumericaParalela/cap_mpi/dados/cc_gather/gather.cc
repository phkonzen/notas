#include <stdio.h>
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

  const size_t my_n = 5;
  double *my_v = (double*) malloc (my_n * sizeof(double));
  for (size_t i=0; i<my_n; i++)
    my_v[i] = 5*world_rank+i+1;

  const size_t n = world_size*my_n;
  double *v = NULL;
  if (world_rank == 0) {
    v = (double*) malloc (n * sizeof(double));
  }

  MPI_Gather (my_v, my_n, MPI_DOUBLE,
	      v, my_n, MPI_DOUBLE,
	      0, MPI_COMM_WORLD);

  if (world_rank == 0) {
    printf ("v = ");
    for (size_t i=0; i<n; i++)
      printf ("%f ", v[i]);
    printf("\n");
  }

  // Finaliza o MPI
  MPI_Finalize();

  return 0;
}
