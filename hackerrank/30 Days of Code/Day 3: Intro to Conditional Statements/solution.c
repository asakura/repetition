#include <stdio.h>

int main() {
  int n;

  scanf("%d", &n);

  if ((n & 1) || (6 <= n && n <= 20))
    printf("Weird\n");
  else
    printf("Not Weird\n");

  return 0;
}
