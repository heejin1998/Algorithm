// 백트래킹
#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
#define MAX 7
int n;
char graph[MAX][MAX];

vector<pair<int, int>> teachers;
vector<pair<int, int>> spaces;

int dx[] = { 0, 0, -1, 1 };
int dy[] = { -1, 1, 0, 0 };

// 감시 피할수 있으면 true, 없으면 false
bool chk(pair<int, int> t) {
		for (int i = 0; i < 4; i++) {

			int x = t.first;
			int y = t.second;

			while (x>=0 && x<n && y>=0 && y<n) {

				x += dx[i];
				y += dy[i];
				
				if (graph[x][y] == 'O')
					break;
				else if (graph[x][y] == 'S')
					return false;
			}
		}
	
	return true;
}
void dfs(int cnt, int idx) {
	if(cnt == 3) {
		for (auto t : teachers) {
			// 선생님들이 단 1명이라도 감시할 수 있다면 return
			if (!chk(t)) {
				return;
			}
		}
		cout << "YES\n";
		exit(0);
	
	}
	for (int i = idx; i < spaces.size(); i++) {
		int x = spaces[i].first;
		int y = spaces[i].second;
		graph[x][y] = 'O';
		dfs(cnt + 1, i + 1);
		graph[x][y] = 'X';
	}
	
}
int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> graph[i][j];
			if (graph[i][j] == 'T')
				teachers.push_back({ i,j });
			else if (graph[i][j] == 'X')
				spaces.push_back({ i,j });

		}
	}

	dfs(0, 0);
	cout<<"NO\n";
	
}