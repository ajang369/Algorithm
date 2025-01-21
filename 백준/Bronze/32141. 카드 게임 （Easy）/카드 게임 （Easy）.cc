#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n, h;
    int cards[1000000];
    int count = 0;

    cin >> n >> h;
    
    for (int i = 0; i < n; i++) {
        cin >> cards[i];
        
        h -= cards[i];
        count++;
        if (h <= 0) break;
    }
    if (h > 0) count = -1;
    
    cout << count;

    return 0;
}