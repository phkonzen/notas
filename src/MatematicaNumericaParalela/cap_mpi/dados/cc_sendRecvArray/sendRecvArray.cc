#include <stdio.h>

// API MPI
#include <mpi.h>

int main (int argc, char** argv) {
  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // numero total de processos
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // ID (rank) do processo
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  if (world_rank == 0) {

    int v[5];
    for (int i=0; i<5; i++)
      v[i] = i;
    
    MPI_Send (&v[1], 3, MPI_INT, 1,
	      0, MPI_COMM_WORLD);
  } else {
    int w[5];
    int i=0;
    for (int j=5; j --> 0; i++)
      w[j] = i;
    
    MPI_Recv (&w[0], 3, MPI_INT, 0,
	      0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    printf ("Processo 1: w=\n");
    for (int i=0; i<5; i++)
      printf ("%d ", w[i]);
    printf("\n");
  }

  // Finaliza o MPI
  MPI_Finalize ();

  return 0;
}
