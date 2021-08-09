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

    if (tid == 1) {
      // delay 1s
      time_t t0 = time(NULL);
      while (time(NULL) - t0 < 1) {
      }
    }

    #pragma omp barrier
   
    printf("Processo %d/%d.\n", tid, nt);
  }  
  return 0;
}
