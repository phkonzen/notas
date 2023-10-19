#include <stdio.h>

int main()
{
  int i{1}, n{1}, aux;
  printf("%d, %d\n", i, n);
  for (int m = 1; i<=10; ++i) {
    printf("%d, %d\n", i, m);
    int a = m;
    m += n;
    n = a;
  }
  return 0;
}
