#include <iostream>
#include <math.h>
#include <vector>

int main() {

  // declara sol. inicial
  std::vector<double> u0 = {1,1,-1};

  // declara sol. corrente
  std::vector<double> u(3);

  // passos no tempo
  int n = 100000000;
  double h = 1.0/n;

  // tempo inicial
  double t0=0;

  // iterações de Euler
  for (int i=0; i<n; i++) {

    u[0] = u0[0] + h*(u0[1]-u0[2]+t0);
    u[1] = u0[1] + h*3*t0*t0;
    u[2] = u0[2] + h*(u0[1]+exp(-t0));

    t0 += h;
    u0 = u;
  }

  // imprime a sol.
  std::cout << "sol. t = "
	    << t0 << std::endl
	    << " u1 = "
	    << u[0] << " / " << 3.2-exp(-1) << std::endl
	    << " u2 = "
	    << u[1] << " / " << 2 << std::endl
	    << " u3 = "
	    << u[2] << " / " << 1.25 - exp(-1) << std::endl;
    
  return 0;
}
