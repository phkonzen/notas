/* dados.cc
   Exemplo de alocação de variáveis.
*/
#include <stdio.h>

int main()
{
  // var inteira
  int i = 1;
  // var pto flutuante
  double x;

  x = 2.5;
  char s[6] = "i + x";
  double y = i + x;
  printf("%s = %f\n", s, y);
  return 0;
}
