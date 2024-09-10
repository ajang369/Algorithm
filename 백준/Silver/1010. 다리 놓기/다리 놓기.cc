#include <iostream>
#include <algorithm>

using namespace std;

int tc,n,m;
long long dp[32][32];
long long go(int x, int y) {
	if (y == 0 || x == y) return 1;
	long long &ret = dp[x][y];
	if (ret != -1) return ret;
	ret = go(x - 1, y - 1) + go(x - 1, y);
	return ret;
}

int main()
{
	cin >> tc;
	while (tc--) {
		cin >> n >> m;
		fill(&dp[0][0], &dp[0][0] + 32 * 32, -1);
		cout << go(m, n) << '\n';
	}
	return 0;
}