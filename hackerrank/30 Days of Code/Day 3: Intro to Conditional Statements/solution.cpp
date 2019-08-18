#include <bits/stdc++.h>

using namespace std;

int main()
{
  int n;
  cin >> n;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');

  if ((n & 1) || (6 <= n && n <= 20))
    cout << "Weird" << endl;
  else
    cout << "Not Weird" << endl;

  return 0;
}
