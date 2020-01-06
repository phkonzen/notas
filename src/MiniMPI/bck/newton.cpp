//#include <mpi.h>
#include <iostream>
#include <math.h>
#include <cstdlib>
#include <ctime>

#define TOL 1e-10

// função objetivo
double fun(double x)
{
  return (x+2)*(x+1)*(x-2);
}

// derivada da fun
double dfun(double x)
{
  return 3*x*x + 2*x - 4;
}
  

// código principal
int main()
{

  // variáveis
  double x0, x1;

  // aproximação inicial randômica
  std::srand(std::time(NULL));
  x0 = double(std::rand()-RAND_MAX/2)/RAND_MAX*100;
  std::cout << x0 << std::endl;

  // iteração de Newton
  for (int i=0; i<1000; i++) {
    double df = dfun(x0);
    if (fabs(df) > TOL)
      x1 = x0 - fun(x0)/df;
    else {
      std::cout << "dfun(x0) == 0!"
		<< std::endl;
      abort();
    }

    if (fabs(x0-x1) < TOL) {
      std::cout << "Zero encontrado: "
		<< x1
		<< std::endl;
      abort();
    }

    x0 = x1;
  }

  std::cout << "Falhou em encontrar um zero!"
	    << std::endl;
  
  return 0;
}
