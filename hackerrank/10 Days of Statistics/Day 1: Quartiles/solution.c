#include <stdio.h>
#include <stdlib.h>

int cmpfunc(const void *a, const void *b) {
  return *(int*) a - *(int*) b;
}

double median(const int n, const int *x) {
  if (n % 2 == 0)
    return (x[n / 2 - 1] + x[n / 2]) / (double) 2.0;

  return (double) x[n / 2];
}

void solution(const int n, const int *x) {
  int middle = n / 2;
  double q1, q2, q3;

  qsort((void*) x, n, sizeof(int), cmpfunc);

  q2 = median(n, x);

  if (n % 2 == 0) {
    q1 = median(middle, x);
    q3 = median(middle, (int *) x + middle);

  } else {
    q1 = median(middle, x);
    q3 = median(middle, (int *) x + middle + 1);
  }

  printf("%.6g\n%.6g\n%.6g\n", q1, q2, q3);
}

int main() {
  int n, *x;

  scanf("%d", &n);

  x = (int*) malloc(n * sizeof(int));

  if (!x)
    return -1;

  for (int i = 0; i < n; i++) {
    scanf("%d", &x[i]);
  }

  solution(n, x);

  free(x);

  return 0;
}
