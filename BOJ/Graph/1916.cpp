// 다익스트라
#include <bits/stdc++.h>
#define INF 1e9

using namespace std;

vector <pair<int, int>> graph[1001];
int d[1001];

void dijkstra(int start) {
	priority_queue<pair<int, int>> pq;
	// 시작 노드로 가기 위한 최단 경로는 0으로 설정
	pq.push({ 0,start });
	d[start] = 0;

	while (!pq.empty()) {
		// 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
		int dist = -pq.top().first; // 현재 노드까지의 비용
		int now = pq.top().second;
		pq.pop();

		// 현재 노드가 이미 처리 된 적이 있는 노드라면 무시
		if (d[now] < dist) continue;
		// 현재 노드와 연결된 다른 인접 노드들 확인
		for (int i = 0; i < graph[now].size(); i++) {
			int cost = dist + graph[now][i].second;
			if (cost < d[graph[now][i].first]) {
				d[graph[now][i].first] = cost;
				pq.push({ -cost, graph[now][i].first });
			}
		}
	}
}

int main() {

	cin.tie(0);
	ios::sync_with_stdio(0);

	int n, m;
	int start, end;
	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		graph[a].push_back({ b,c });

	}
	cin >> start >> end;
	// 최단 거리 테이블 무한으로 초기화
	fill(d, d + 1001, INF);

	dijkstra(start);
	cout << d[end];
	

}