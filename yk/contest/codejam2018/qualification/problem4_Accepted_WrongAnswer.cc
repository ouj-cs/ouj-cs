#include <bits/stdc++.h>
using namespace std;

int main() {
  const double DEG045 = M_PI / 4;
  const double DEG090 = M_PI / 2;
  const double DEG180 = M_PI;
  const double DEG360 = 2 * M_PI;
  const double DEG055 = 0.9553166181245093;
  const double DEG035 = DEG090 - DEG055;
  int T;
  cin >> T;
  cout << setprecision(17);
  for (int i = 0; i < T; ++i) {
    double A;
    cin >> A;
    if (A <= sqrt(2)) {
      double theta_min = 0;
      double theta_max = DEG045;
      double prev2 = -2, prev1 = -1;
      while (prev2 != prev1) {
        double theta = (theta_min + theta_max) / 2;
        double area = sqrt(2) * cos(DEG045 - theta);
        if (area > A) {
          theta_max = theta;
        } else {
          theta_min = theta;
        }
        prev2 = prev1;
        prev1 = theta;
      }
      cout << "Case #" << i + 1 << ":" << endl;
      double x = 0.5 * cos(prev1);
      double y = 0.5 * sin(prev1);
      cout << x << " " << y << " 0" << endl;
      x = -0.5 * sin(prev1);
      y = 0.5 * cos(prev1);
      cout << x << " " << y << " 0" << endl;
      cout << "0 0 0.5" << endl;
    } else {
      double theta_min = 0;
      double theta_max = DEG055;
      double prev2 = -2, prev1 = -1;
      while (prev2 != prev1) {
        double theta = (theta_min + theta_max) / 2;
        double z0 = sqrt(3) * abs(sin(theta - DEG035));
        double z1 = sqrt(3) * sin(DEG035 + theta);
        double area = sqrt(2) * z0 + sqrt(2) * (z1 - z0) / 2;
        cout << setprecision(4);
//        cout << "A=" << A << ", theta=" << theta << ", area=" << area
//        << ", z0z1=" << z0 << "|" << z1 << ", (" << theta_min << ", " << theta_max << ")" << endl;
        cout << setprecision(17);
        if (area > A) {
          theta_max = theta;
        } else {
          theta_min = theta;
        }
        prev2 = prev1;
        prev1 = theta;
      }
      cout << "Case #" << i + 1 << ":" << endl;
      double x = 0.3535533905932738;
      double y = sqrt(2) / 4 * cos(prev1);
      double z = sqrt(2) / 4 * -sin(prev1);
      cout << x << " " << y << " " << z << endl;
      cout << -x << " " << y << " " << z << endl;
      x = 0;
      y = 0.5 * sin(prev1);
      z = 0.5 * cos(prev1);
      cout << x << " " << y << " " << z << endl;
    }
  }
}
