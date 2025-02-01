#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void fastio() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);
}

int main() {
    fastio();
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        vector<string> result;

        string S;
        cin >> S;

        string revS = S;
        reverse(revS.begin(), revS.end());

        int l = S.length();

        for (int j = 0; j < l; j++) {
            string sub1 = S.substr(l - j - 1);
            string sub2 = revS.substr(0, j+1);
            // cout << sub1 << '\t' << sub2 << '\n';

            if (sub1 == sub2) {
                string tmp1 = S.substr(0, l-j-1);
                string tmp2 = revS.substr(j+1);

                string res = tmp1 + sub2 + tmp2;
                result.push_back(res);
                // cout << res << '\n';
            }
        }
        cout << result.back() << "\n";
    }

    return 0;
}