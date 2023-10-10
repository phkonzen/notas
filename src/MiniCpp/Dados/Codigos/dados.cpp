/* dados.cpp
   Exemplo de alocação de variáveis.
*/
#include <iostream>
#include <string>

int main() {
  // var inteira
  int i = 1;
  // var pto flutuante
  double x;
  // var string
  std::string s;

  x = 2.5;
  s = "i + x";
  double y = i + x;
  std::cout << s << " = " \
	    << y << std::endl;
  return 0;
}
