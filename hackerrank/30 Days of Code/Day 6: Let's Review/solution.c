#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int n;
  char s[10240], *out;

  scanf("%d", &n);

  while(n > 0) {
    int len, offset;

    scanf("%10238s", (char *) &s);
    len = strlen((char *) &s);
    offset = len / 2 + (!(len &1) ? 1 : 2);
    out = (char *) malloc((len + 2) * sizeof(char));
    out[offset - 1] = ' ';

    if (!out)
      return -1;

    for (int i = 0, j = 0; i < len; i++) {
      if (!(i & 1))
        out[j] = s[i];
      else {
        out[offset + j] = s[i];
        j++;
      }
    }

    out[len + 2] = '\n';
    n--;

    printf("%s\n", out);
  }

  return 0;
}
