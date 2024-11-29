#include <iostream>
#define FASTIO cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);

using namespace std;

int main() {
    int p, t, n;
    cin >> n;
    while (n--) {
        cin >> p >> t;
        int a = t / 4;
        int b = t / 7;

        cout << (p + a - b) << '\n';
    }
    return 0;
}