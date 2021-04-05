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

  const size_t n = 10;
  gsl_vector *v = gsl_vector_alloc (0);

  if (world_rank == 0) {
    v = gsl_vector_alloc (n);

    for (size_t i=0; i<n; i++)
      gsl_vector_set (v, i, i+1);
  }

  size_t my_n = n/world_size;  
  gsl_vector *my_v = gsl_vector_alloc (my_n);

  MPI_Scatter (v->data, my_n, MPI_DOUBLE,
	       my_v->data, my_n, MPI_DOUBLE,
	       0, MPI_COMM_WORLD);

  double soma = 0.0;
  for (size_t i=0; i<my_n; i++) {
    soma += gsl_vector_get (my_v, i);
  }

  printf ("Processo %d soma = %f\n",
  	  world_rank, soma);  

  // Finaliza o MPI
  MPI_Finalize();

  return 0;
}
