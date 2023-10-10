#include <iostream>

int main() {

  double x = 5.2e-2;
  
  std::cout << "Padrão: "
	    << x << std::endl;

  std::cout << "Fixada: " << std::fixed
	    << x << std::endl;;

  std::cout << "Científica: " << std::scientific
	    << x << std::endl;;
  return 0;
}
