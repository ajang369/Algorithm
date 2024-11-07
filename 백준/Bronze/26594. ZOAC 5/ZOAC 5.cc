#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;

    char first = s[0];

    int cnt = count(s.begin(), s.end(), first);

    cout << cnt << '\n';
    return 0;
}