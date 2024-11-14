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
    

  std::vector<double> u0(npid);
  std::vector<double> u(npid);
  double uaux = 0;

  // num. passos no tempo
  int m = int(tf/dt);

  // cond. inicial
  for (int li=0; li<npid; li++) {
    int gi = gii + li;
    u0[li] = sin(M_PI*gi*h);
  }
  uaux = sin(M_PI*(gfi+1)*h);

  // c.c.
  if (pid == 0) 
    u[0] = 0;
  if (pid == nproc-1)
    u[npid-1] = 0;

  // iteração temporal
  for (int k=0; k<m; k++) {

    for (int i=1; i<npid-1; i++) {
      u[i] = u0[i] + dt/(h*h)*a2*(u0[i-1]-2*u0[i]+u0[i+1]);
    }

    if (pid != nproc-1) {
      u[npid-1] = u0[npid-1] + dt/(h*h)*a2*(u0[npid-2]-2*u0[npid-1]+uaux);
    }

    if (pid != 0) {
      MPI_Send(&u[1], 1 , MPI_DOUBLE, pid-1,
	       0, MPI_COMM_WORLD);

      MPI_Recv(&u[0], 1 , MPI_DOUBLE, pid-1,
	       0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    }
    if (pid != nproc-1) {
      MPI_Recv(&uaux, 1, MPI_DOUBLE, pid+1,
	       0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

      MPI_Send(&u[npid-1], 1 , MPI_DOUBLE, pid+1,
	       0, MPI_COMM_WORLD);
    }

    u0 = u;

    if (((k % 10000) == 0) | (k == m-1)) {
      
      // calor médio
      double aux = 0;
      for (int j=0; j<npid-1; j++)
	aux += h/2*(u[j]+u[j+1]);

      double qn=0;
      MPI_Reduce(&aux, &qn, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

      if (pid == 0) {
	double qa = 2/M_PI*exp(-a2*M_PI*M_PI*(k+1)*dt);

	std::cout << std::endl
		  << "t = " << (k+1)*dt << std::endl
		  << " Analítica: " << qa << std::endl
		  << " Numérica : " << qn << std::endl;
      }
    }
    
  }

  // Finaliza o MPI
  MPI_Finalize();

  return 0;

}
  
