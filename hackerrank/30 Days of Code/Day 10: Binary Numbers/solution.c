#include<stdio.h>

int main()
{
  int n, count = 0;
  scanf("%d", &n);

  while (n) {
    n &= n << 1;
    count += 1;
  }

  printf("%d", count);

  return 0;
}