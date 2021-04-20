#include <stdio.h>
#include <math.h>

// API MPI
#include <mpi.h>

int main (int argc, char** argv) {
  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // número total de processos
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // ID (rank) do processo
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  // parâmetros
  size_t M = 1000;
  size_t I = 10;

  // tamanho dos passos discretos
  double ht = 5e-4;
  double hx = 1.0/I;
  double cfl = ht/(hx*hx);
  
  // malha espacial local
  size_t ip = world_rank * int (I/world_size);
  size_t fp = (world_rank+1) * int (I/world_size);
  if (world_rank == world_size-1)
    fp = I;
  size_t my_I = fp - ip;
  
  double x[my_I+1];
  for (size_t j=0; j<=my_I; j++)
    x[j] = (ip+j) * hx;
  
  // solução local
  double u0[my_I+1], u[my_I+1];
  
  // condição inicial
  for (size_t j=0; j<=my_I; j++) {
    u0[j] = sin (M_PI * x[j]);
  }

  // condições de contorno de Dirichlet
  if (world_rank == 0) 
    u[0] = 0.0;
  if (world_rank == world_size-1)
    u[my_I] = 0.0;

  // auxiliares
  double u00, u0I;
  

  // iterações no tempo
  for (size_t m=0; m<M; m++) {

    if (world_rank == 0) {
      MPI_Send (&u0[my_I], 1, MPI_DOUBLE,
		1, 0, MPI_COMM_WORLD);
      MPI_Recv (&u0I, 1, MPI_DOUBLE,
		1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    } else if (world_rank < world_size-1) {
      MPI_Recv (&u00, 1, MPI_DOUBLE,
		world_rank-1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      MPI_Send (&u0[my_I], 1, MPI_DOUBLE,
		world_rank+1, 0, MPI_COMM_WORLD);
      
      MPI_Recv (&u0I, 1, MPI_DOUBLE,
		world_rank+1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      MPI_Send (&u0[1], 1, MPI_DOUBLE,
		world_rank-1, 0, MPI_COMM_WORLD);
    } else {
      MPI_Recv (&u00, 1, MPI_DOUBLE,
		world_size-2, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);    
      MPI_Send (&u0[1], 1, MPI_DOUBLE,
		world_size-2, 0, MPI_COMM_WORLD);
    }
    
    // atualização
    u[1] = u0[1]
      + cfl * u00
      - 2*cfl * u0[1]
      + cfl * u0[2];
    for (size_t j=2; j<my_I; j++)
      u[j] = u0[j]
	+ cfl * u0[j-1]
	- 2*cfl * u0[j]
	+ cfl * u0[j+1];
    if (world_rank < world_size-1)
      u[my_I] = u0[my_I]
	+ cfl * u0[my_I-1]
	- 2*cfl * u0[my_I]
	+ cfl * u0I;

    if (world_rank == 1)
      printf ("%f %f %e\n", (m+1)*ht, x[2], u[2]);

    // prepara nova iteração
    for (size_t j=0; j<=my_I; j++)
      u0[j] = u[j];

  }
  

  // Finaliza o MPI
  MPI_Finalize ();

  return 0;
}
