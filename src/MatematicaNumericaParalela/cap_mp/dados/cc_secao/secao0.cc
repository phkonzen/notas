#include <stdio.h>
#include <ctime>
#include <omp.h>

int main(int argc, char *argv[]) {

  // master thread id
  int tid = 0;
  int nt;

  // regiao paralela
  #pragma omp parallel private(tid)
  {
    tid = omp_get_thread_num();
    nt = omp_get_num_threads();

    #pragma omp sections
    {
      // secao 1
      #pragma omp section
      {
	printf("%d/%d exec secao 1\n", \
	       tid, nt);
      }
      
      // secao 2
      #pragma omp section
      {
	// delay 1s
	time_t t0 = time(NULL);
	while (time(NULL) - t0 < 1) {
	}
	printf("%d/%d exec a secao 2\n", \
	       tid, nt);
      }
    }

    printf("%d/%d terminou\n", tid, nt);
  }

  return 0;
}
