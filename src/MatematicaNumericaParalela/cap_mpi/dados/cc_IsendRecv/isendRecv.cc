#include <stdio.h>

// API MPI
#include <mpi.h>

int main (int argc, char** argv) {
  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // numero total de processos
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  if (world_size < 2) {
    printf ("Num. de processos deve"\
	    "maior que 2.\n");
    int errorcode = -1;
    MPI_Abort (MPI_COMM_WORLD, errorcode);
  }
    
  // ID (rank) do processo
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  // MPI_Status & MPI_Request
  MPI_Status status;
  MPI_Request request;

  if (world_rank == 0) {
    double x = 3.1416;
    MPI_Isend (&x, 1, MPI_DOUBLE, 1,
	       0, MPI_COMM_WORLD, &request);
  } else {
    double y = 0.0;
    MPI_Irecv (&y, 1, MPI_DOUBLE, 0,
	      0, MPI_COMM_WORLD, &request);
    double x = y + 1.0;
    printf ("x = %f\n", x);
    int recvd = 0;
    while (!recvd)
      MPI_Test (&request, &recvd, &status);
    x = y + 1;
    printf ("x = %f\n", x);
  }
    
  // Finaliza o MPI
  MPI_Finalize ();

  return 0;
}
