#include <iostream>
#include <math.h>
#include <vector>

int main() {

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

  std::vector<double> u0(n);
  std::vector<double> u(n);

  // num. passos no tempo
  int m = int(tf/dt);

  // cond. inicial
  for (int i=0; i<n; i++)
    u0[i] = sin(M_PI*i*h);

  // c.c.
  u[0] = 0;
  u[n-1] = 0;

  // iteração temporal
  for (int k=0; k<m; k++) {

    for (int i=1; i<n-1; i++) {
      u[i] = u0[i] + dt/(h*h)*a2*(u0[i-1]-2*u0[i]+u0[i+1]);
    }

    u0 = u;

    if (((k % 10000) == 0) | (k == m-1)) {

      // calor médio
      double qa = 2/M_PI*exp(-a2*M_PI*M_PI*(k+1)*dt);
      double qn = 0;
      for (int j=0; j<n-1; j++)
	qn += h/2*(u[j]+u[j+1]);

      std::cout << std::endl
		<< "t = " << (k+1)*dt << std::endl
		<< " Analítica: " << qa << std::endl
		<< " Numérica : " << qn << std::endl;
    }
  }

  return 0;
  
}
  
