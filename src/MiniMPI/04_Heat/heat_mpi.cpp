#include <mpi.h>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

int main() {

  // Inicializa o MPI
  MPI_Init(NULL, NULL);
  
  // Número de processos
  int nproc;
  MPI_Comm_size(MPI_COMM_WORLD, &nproc);

  // verifica nproc >= 2
  assert(nproc >= 2);

  // identificação (rank) do processo
  int pid;
  MPI_Comm_rank(MPI_COMM_WORLD, &pid);

  // parametros
  double alpha = 1e-1;
  double tf = 0.5;
  
  double a2 = alpha*alpha;

  // num. pts. disc. espaço
  int n = 10001;
  // dt
  double dt = 1e-7;

  // passo no espaço
  double h = 1.0/(n-1);
  std::cout << h << std::endl;

  int gii = pid*int((n-1)/nproc);
  int gfi = (pid+1)*int((n-1)/nproc);
  if (pid == nproc-1)
    gfi = n-1;
  int npid = gfi-gii+1;

  std::cout << std::endl
	    << "pid: " << pid << std::endl
	    << " gii: " << gii << std::endl
	    << " gfi: " << gfi << std::endl
	    << " npid: " << npid << std::endl;
    

  std::vector<double> u0(n);
  std::vector<double> u(npid);

  // num. passos no tempo
  int m = int(tf/dt);

  // cond. inicial
  for (int i=0; i<n; i++) {
    u0[i] = sin(M_PI*i*h);
  }

  // c.c.
  if (pid == 0) 
    u[0] = 0;
  if (pid == nproc-1)
    u[npid-1] = 0;

  // iteração temporal
  for (int k=0; k<m; k++) {

    for (int i=1; i<npid-1; i++) {
      int gi = gii + i;
      u[i] = u0[gi] + dt/(h*h)*a2*(u0[gi-1]-2*u0[gi]+u0[gi+1]);
    }

    if (pid != nproc-1) {
      u[npid-1] = u0[gfi] + dt/(h*h)*a2*(u0[gfi-1]-2*u0[gfi]+u0[gfi+1]);
    }


    MPI_Gather(&u[1],npid-1,MPI_DOUBLE,
    	       &u0[gii+1],npid-1,MPI_DOUBLE,
    	       0, MPI_COMM_WORLD);

    MPI_Bcast(&u0[0],n,MPI_DOUBLE,0,MPI_COMM_WORLD);

    // // npid igual para todos!
    // MPI_Allgather(&u[1],npid-1,MPI_DOUBLE,
    // 		  &u0[1],npid-1,MPI_DOUBLE,
    // 		  MPI_COMM_WORLD);

    
    if ((pid == 0) & (((k % 10000) == 0) | (k == m-1))) {
      
      // calor médio
      double qn = 0;
      for (int j=0; j<n-1; j++)
	qn += h/2*(u0[j]+u0[j+1]);

	double qa = 2/M_PI*exp(-a2*M_PI*M_PI*(k+1)*dt);

	std::cout << std::endl
		  << "t = " << (k+1)*dt << std::endl
		  << " Analítica: " << qa << std::endl
		  << " Numérica : " << qn << std::endl;
    }
    
  }

  // Finaliza o MPI
  MPI_Finalize();

  return 0;

}
  
