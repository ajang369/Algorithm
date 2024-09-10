#include <iostream>
#include <algorithm>

using namespace std;

int n,res,dp[1000004];

int go(int x) {
	if (x == 1) return 0;

}

int main()
{
	cin >> n;

	for (int i = 2; i < n + 1; i++) {
		dp[i] = dp[i - 1] + 1;
		if (i % 2 == 0) {
			dp[i] = min(dp[i], dp[i / 2] + 1);
		}
		if (i % 3 == 0) {
			dp[i] = min(dp[i], dp[i / 3] + 1);
		}
	}

	cout << dp[n] << '\n';
	return 0;
}