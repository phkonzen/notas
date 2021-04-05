#include <stdio.h>
#include <math.h>

// API MPI
#include <mpi.h>

// gsl
#include <gsl/gsl_vector.h>

int main(int argc, char** argv) {
  
  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // número total de processos
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // ID (rank) do processo
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  const size_t my_n = 5;
  gsl_vector *my_v = gsl_vector_alloc (my_n);
  for (size_t i=0; i<my_n; i++)
      gsl_vector_set (my_v, i, 5*world_rank+i+1);

  const size_t n = world_size*my_n;
  gsl_vector *v = gsl_vector_alloc (0);
  if (world_rank == 0) {
    v = gsl_vector_alloc (n);
  }

  MPI_Gather (my_v->data, my_n, MPI_DOUBLE,
	      v->data, my_n, MPI_DOUBLE,
	      0, MPI_COMM_WORLD);

  if (world_rank == 0) {
    printf ("v = ");
    for (size_t i=0; i<n; i++)
      printf ("%f ", gsl_vector_get (v, i));
    printf("\n");
  }

  // Finaliza o MPI
  MPI_Finalize();

  return 0;
}
