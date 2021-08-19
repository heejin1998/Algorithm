// 다익스트라 + BFS
#include<bits/stdc++.h>
using namespace std;
#define INF 1e9

int n, m;
int graph[101][101];
int d[101][101];

int dx[] = { 0, 0, -1, 1 };
int dy[] = { -1, 1, 0, 0 };

void BFS() {

	queue<pair<int, int>> q;
	q.push({ 0,0 });
	d[0][0] = 0;

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue; // 범위 벗어날 경우

			if (graph[nx][ny] == 1) {
				if (d[nx][ny] > d[x][y] + 1) {
					d[nx][ny] = d[x][y] + 1;
					q.push({ nx,ny });
				}
			}
			else if (graph[nx][ny] == 0) {
				if (d[nx][ny] > d[x][y]) {
					d[nx][ny] = d[x][y];
					q.push({ nx,ny });
				}
			}
		}
	}
}


int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);
	
	cin >> m >> n;
	for (int i = 0; i < n; i++) {
		string num_str;
		cin >> num_str;
		for (int j = 0; j < m; j++) {
			d[i][j] = INF;
			graph[i][j] = num_str[j]-'0';
		}
	}

	BFS();
	cout << d[n - 1][m - 1] << "\n";

}