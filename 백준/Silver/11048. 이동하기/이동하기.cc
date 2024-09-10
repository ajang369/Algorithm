#include <iostream>
#include <algorithm>

using namespace std;

const int dx[] = { 1,0,1 };
const int dy[] = { 0,1,1 };
const int MAX_N = 1003;
int n, m, a[MAX_N][MAX_N],dp[MAX_N][MAX_N];

int go(int x, int y) {
	if (x == n && y == m) return a[x][y];
	int &ret = dp[x][y];
	if (ret != -1) return ret;
	ret = 0;
	int tmp = 0;
	for (int i = 0; i < 3; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx > n || ny > m || nx <= 0 || ny <= 0) continue;
		tmp = go(nx, ny) + a[x][y];
		ret = max(ret, tmp);
	}
	return ret;
}

// 방향이 정해져있음, 유향 비순환 그래프(사이클이 생길 수 없는 경로)
int main()
{
	cin >> n >> m;
	fill(&dp[0][0], &dp[0][0] + MAX_N * MAX_N, -1);
	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < m + 1; j++) {
			cin >> a[i][j];
		}
	}

	cout << go(1, 1) << '\n';

	return 0;
}