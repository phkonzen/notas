#include <iostream>
#include <omp.h>

using namespace std;

int main(int argc, char *argv[]) {

#pragma omp parallel				
  {
    int id = omp_get_thread_num();
    cout << "Processo" << id << ": Olá, Mundo!\n";
  }
  
  return 0;
}
