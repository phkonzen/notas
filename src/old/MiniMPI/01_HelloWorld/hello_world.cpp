#include <mpi.h>
#include <iostream>

int main()
{
  // Inicializa o MPI
  MPI_Init(NULL, NULL);

  // Número de processos
  int nproc;
  MPI_Comm_size(MPI_COMM_WORLD, &nproc);

  // identificação (rank) do processo
  int pid;
  MPI_Comm_rank(MPI_COMM_WORLD, &pid);

  if (pid == 0)
    std::cout << "Num. de processos: "
	      << nproc
	      << std::endl;

  // Barreira de sincronização
  MPI_Barrier(MPI_COMM_WORLD);
  
  // imprime msg no terminal
  std::cout << "pid "
	    << pid
	    << " diz: Olá!"
	    << std::endl;

  // Finaliza o MPI
  MPI_Finalize();
  
  return 0;
}
