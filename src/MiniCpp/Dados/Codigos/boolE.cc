#include <stdio.h>

int main()
{
  bool T = true;
  bool F = false;
  printf("A   | B   | A && B\n");
  printf("%d   | %d   | %d\n", T, T, T&&T);
  printf("%d   | %d   | %d\n", T, F, T&&F);
  printf("%d   | %d   | %d\n", F, T, F&&T);
  printf("%d   | %d   | %d\n", F, F, F&&F);
}
