#include <stdio.h>
#include <ctime>
#include <omp.h>

int main(int argc, char *argv[]) {

  // master thread id
  int tid = 0;
  int nt;

  #pragma omp parallel private(tid)
  {
    tid = omp_get_thread_num();
    nt = omp_get_num_threads();

    #pragma omp sections nowait
    {
      // seção 1
      #pragma omp section
      {
	printf("%d/%d exec seção 1\n", \
	       tid, nt);
      }
      
      // seção 2
      #pragma omp section
      {
	// delay 1s
	time_t t0 = time(NULL);
	while (time(NULL) - t0 < 1) {
	}
	printf("%d/%d exec a seção 2\n", \
	       tid, nt);
      }
    }

    printf("%d/%d terminou\n", tid, nt);
  }

  return 0;
}
