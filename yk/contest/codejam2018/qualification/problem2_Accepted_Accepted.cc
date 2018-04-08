#include <bits/stdc++.h>
using namespace std;

void Print(const vector<int>& xs) {
  for (int i = 0; i < xs.size(); ++i) {
    cout << xs[i] << ", ";
  }
  cout << endl;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int N;
    cin >> N;
    vector<int> V(N);
    for (auto& x : V) cin >> x;
    vector<int> V_even, V_odd;
    for (int i = 0; i < V.size(); ++i) {
      if (i % 2 == 0)
        V_even.push_back(V[i]);
      else
        V_odd.push_back(V[i]);
    }
    sort(V_even.begin(), V_even.end());
    sort(V_odd.begin(), V_odd.end());
    vector<int> V_sorted(N, -1);
    for (int i = 0; i < V_even.size(); ++i) {
      V_sorted[2 * i] = V_even[i];
    }
    for (int i = 0; i < V_odd.size(); ++i) {
      V_sorted[2 * i + 1] = V_odd[i];
    }
    int error = -1;
    for (int i = 1; i < V_sorted.size(); ++i) {
      if (V_sorted[i - 1] > V_sorted[i]) {
        error = i - 1;
        break;
      }
    }
    if (error == -1) {
      cout << "Case #" << i + 1 << ": " << "OK" << endl;
    } else {
      cout << "Case #" << i + 1 << ": " << error << endl;
    }
  }
}

