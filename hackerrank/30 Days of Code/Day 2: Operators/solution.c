#include <stdio.h>
#include <math.h>

// Complete the solve function below.
void solve(double meal_cost, int tip_percent, int tax_percent) {
  double tip = meal_cost * (tip_percent / 100.0);
  double tax = meal_cost * (tax_percent / 100.0);
  int total_cost = (int) round(meal_cost + tip + tax);

  printf("%d\n", total_cost);
}

int main() {
  double meal_cost;
  int tip_percent;
  int tax_percent;

  scanf("%lf", &meal_cost);
  scanf("%d", &tip_percent);
  scanf("%d", &tax_percent);

  solve(meal_cost, tip_percent, tax_percent);
}
