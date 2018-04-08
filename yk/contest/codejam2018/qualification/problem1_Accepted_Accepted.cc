#include <bits/stdc++.h>
using namespace std;

void Print(const vector<int64_t>& xs, int64_t x1) {
  for (int64_t i = 0; i < xs.size(); ++i) {
    cout << xs[i];
    if (i != xs.size() - 1) cout << ", ";
  }
  cout << ": " << x1 << endl;
}

void Solve(int64_t problem_n) {
  int64_t D;
  string P;
  cin >> D >> P;
  vector<int64_t> xs;
  int64_t n_charges = 0, n_shoots = 0, strength = 1, damage_total = 0;
  for (int64_t i = 0; i < P.size(); ++i) {
    char c = P[i];
    if (c == 'C') {
      ++n_charges;
      strength *= 2;
      xs.push_back(-1);
    } else if (c == 'S') {
      ++n_shoots;
      xs.push_back(strength);
      damage_total += strength;
    } else {
      throw exception();
    }
  }
  // Print(xs, damage_total);
  if (n_shoots > D) {
    cout << "Case #" << problem_n + 1 << ": " << "IMPOSSIBLE" << endl;
    return;
  }
  if (n_charges == 0 || n_shoots == 0) {
    cout << "Case #" << problem_n + 1 << ": " << 0 << endl;
    return;
  }
  int64_t s_last = -1;
  for (int64_t i = xs.size() - 1; i >= 0; --i) {
    if (xs[i] != -1) {
      s_last = i;
      break;
    }
  }
  int64_t c_to_move = -1;
  for (int64_t i = xs.size() - 1; i >= 0; --i) {
    if (xs[i] == -1 && i < s_last) {
      c_to_move = i;
      break;
    }
  }
  int64_t n_swaps = 0;
  while (damage_total > D) {
    if (c_to_move > s_last) {
      for (int64_t i = c_to_move - 1; i >= 0; --i) {
        if (xs[i] == -1 && i < s_last) {
          c_to_move = i;
          break;
        }
        if (i == 0) throw runtime_error("next c not exists.");
      }
    }
    swap(xs[c_to_move], xs[c_to_move + 1]);
    ++n_swaps;
    if (c_to_move + 1 == s_last) --s_last;
    ++c_to_move;
    if (xs[c_to_move - 1] != -1) {
      xs[c_to_move - 1] /= 2;
      damage_total -= xs[c_to_move - 1];
    }
    // Print(xs, damage_total);
  }
  cout << "Case #" << problem_n + 1 << ": " << n_swaps << endl;
}

int main() {
  int64_t T;
  cin >> T;
  for (int64_t i = 0; i < T; ++i) {
    Solve(i);
  }
}
