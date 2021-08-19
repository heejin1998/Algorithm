// ���ͽ�Ʈ��
#include <bits/stdc++.h>
#define INF 1e9

using namespace std;

vector <pair<int, int>> graph[1001];
int d[1001];

void dijkstra(int start) {
	priority_queue<pair<int, int>> pq;
	// ���� ���� ���� ���� �ִ� ��δ� 0���� ����
	pq.push({ 0,start });
	d[start] = 0;

	while (!pq.empty()) {
		// ���� �ִ� �Ÿ��� ª�� ��忡 ���� ���� ������
		int dist = -pq.top().first; // ���� �������� ���
		int now = pq.top().second;
		pq.pop();

		// ���� ��尡 �̹� ó�� �� ���� �ִ� ����� ����
		if (d[now] < dist) continue;
		// ���� ���� ����� �ٸ� ���� ���� Ȯ��
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
	// �ִ� �Ÿ� ���̺� �������� �ʱ�ȭ
	fill(d, d + 1001, INF);

	dijkstra(start);
	cout << d[end];
	

}