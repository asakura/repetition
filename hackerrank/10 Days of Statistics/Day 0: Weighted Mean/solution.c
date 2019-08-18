#include <stdio.h>
#include <stdlib.h>

void solution(const int n, const int *x, const int *w) {
  int numerator = 0, denominator = 0;
  double weighted_mean;

  for (int i = 0; i < n; i++) {
    numerator += x[i] * w[i];
    denominator += w[i];
  }

  weighted_mean = (double) numerator / (double) denominator;

  printf("%.1f\n", weighted_mean);
}

int main() {
  int n, *x, *w;

  scanf("%d", &n);

  x = (int *) malloc(n * sizeof(int));
  w = (int *) malloc(n * sizeof(int));

  for (int i = 0; i < n; i++) {
    scanf("%d", &x[i]);
  }

  for (int i = 0; i < n; i++) {
    scanf("%d", &w[i]);
  }

  solution(n, x, w);

  free(x);
  free(w);

  return 0;
}
