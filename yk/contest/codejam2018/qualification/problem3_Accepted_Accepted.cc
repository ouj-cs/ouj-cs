#include <bits/stdc++.h>
using namespace std;

bool m[1001][1001];

void Print(int col_max) {
  for (int i = 1; i <= 3; ++i) {
    for (int j = 1; j <= col_max + 1; ++j) {
      cerr << (m[i][j] ? '#' : '-');
    }
    cerr << endl;
  }
  cerr << endl;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    for (int i = 0; i < 1001; ++i) {
      for (int j = 0; j < 1001; ++j) {
        m[i][j] = false;
      }
    }
    int A;
    cin >> A;
    int row = 2, col = 2, col_max;
    if (A == 20)
      col_max = 6;
    else
      col_max = 66;
    int n_try = 0;
    while (true) {
      // Print(col_max);
      if (m[1][col - 1] && m[2][col - 1] && m[3][col - 1])
        col = min(col_max, col + 1);
      cout << row << " " << col << endl;
      ++n_try;
      int x, y;
      cin >> x >> y;
      if (x == -1 && y == -1)
        break;
      if (x == 0 && y == 0) {
        cerr << "n_try: " << n_try << endl;
        break;
      }
      m[x][y] = true;
    }
  }
}

