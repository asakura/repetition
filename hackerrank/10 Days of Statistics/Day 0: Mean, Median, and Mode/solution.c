#include <stdio.h>
#include <stdlib.h>

int cmpfunc(const void *a, const void *b) {
  return *(int*) a - *(int*) b;
}

void solution(const int n, const int *x) {
  int mode,
    most = 0,
    total = 0;
  double mean, median;

  qsort((void*) x, n, sizeof(int), cmpfunc);

  // mean

  for (int i = 0; i < n; i++) {
    total += x[i];
  }

  mean = total / (double) n;

  // median

  if (n % 2 == 0) {
    median = (x[n / 2 - 1] + x[n / 2]) / 2.0;
  } else {
    median = x[n / 2];
  }

  // mode

  for (int i = 0; i < n; i++) {
    int count = 1;

    while (x[i] == x[i + 1]) {
      i++;
      count++;
    }

    if (count > most) {
      mode = x[i];
      most = count;
    }
  }

  printf("%.6g\n%.6g\n%d\n", mean, median, mode);
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
