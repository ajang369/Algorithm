#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    char first = s[0];

    int cnt = 0;
    for (char c : s) {
        if (c == first) cnt++;
        else break;
    }

    cout << cnt << '\n';
    return 0;
}