#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int m;
        char c;

        cin >> m >> c;

        if (c == 'C') {
            char arr[m+1];
            int res[m+1];
            for (int i = 0; i < m; i++) {
                cin >> arr[i];
                res[i] = int(arr[i]) - 64;
                cout << res[i] << " ";
            }
        } else {
            int arr[m+1];
            char res[m+1];
            for (int i = 0; i < m; i++) {
                cin >> arr[i];
                res[i] = char(arr[i]+64);
                cout << res[i] << " ";
            }
        }
        cout << '\n';
        
    }
    return 0;
}