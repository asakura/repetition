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
  double q1, q3, iqr;

  qsort((void*) x, n, sizeof(int), cmpfunc);

  if (n % 2 == 0) {
    q1 = median(middle, x);
    q3 = median(middle, (int *) x + middle);

  } else {
    q1 = median(middle, x);
    q3 = median(middle, (int *) x + middle + 1);
  }

  iqr = q3 - q1;

  printf("%.1lf\n", iqr);
}

int main() {
  int n, total = 0, *x, *f, *s;

  scanf("%d", &n);

  x = (int*) malloc(n * sizeof(int));

  if (!x)
    return -1;

  f = (int*) malloc(n * sizeof(int));

  if (!f)
    return -1;

  for (int i = 0; i < n; i++) {
    scanf("%d", &x[i]);
  }

  for (int i = 0; i < n; i++) {
    scanf("%d", &f[i]);
    total += f[i];
  }

  s = (int*) malloc(n * total * sizeof(int));

  if (!s)
    return -1;

  int offset = 0;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < f[i]; j++) {
      s[offset] = x[i];
      offset++;
    }
  }

  free(x);
  free(f);

  solution(total, s);

  free(s);

  return 0;
}
