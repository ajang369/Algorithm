#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int bX, bY;
    int dX, dY;
    int jX, jY;

    cin >> bX >> bY;
    cin >> dX >> dY;
    cin >> jX >> jY;

    int tmp1 = max(abs(bX - jX), abs(bY - jY));
    int tmp2 = abs(dX - jX) + abs(dY - jY);

    if (tmp1 < tmp2) {
        cout << "bessie" << '\n';
    } else if (tmp1 > tmp2) {
        cout << "daisy" << '\n';
    } else {
        cout << "tie" << '\n';
    }

    return 0;
}