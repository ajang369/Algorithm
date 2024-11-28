#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#define FASTIO cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);

using namespace std;
int T, N;

int main() {
    FASTIO
    cin >> T;
    while(T--) {
        cin >> N;
        int root = static_cast<int>(sqrt(N));

        if ((N%2==1) && (root*root == N)) {
            cout << "OS\n";
        }
        else if (N%2 == 1) {
            cout << "O\n";
        }
        else if (root * root == N) {
            cout << "S\n";
        }
        else {
            cout << "EMPTY\n";
        }
    }
}