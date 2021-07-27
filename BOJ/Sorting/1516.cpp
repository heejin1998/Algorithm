// ���� ���� (�������� + DP)

#include <bits/stdc++.h>
using namespace std;

const int MAX = 501;

int inDegree[MAX];
vector<int> graph[MAX];
int times[MAX];
int result[MAX];

int main() {

	cin.tie(0);
	ios::sync_with_stdio(0);
	cout.tie(0);

	int n;
	cin >> n;

	// 1. �������� input �ޱ�
	for (int i = 1; i <= n; i++) {
		int time;
		cin >> time;
		times[i] = time;

		while (true) {
			int node;
			cin >> node;
			if (node == -1)
				break;
			graph[node].push_back(i);
			inDegree[i]++;
		}
	}

	// 2. �������� 0�ΰ� queue�� ����
	queue<int> q;
	for (int i = 1; i <= n; i++) {
		if (inDegree[i] == 0)
			q.push(i);
	}

	// 3. �������� 0�ΰ� ���� ����� �� ����ġ��. �׷��� �������� 0�Ǹ� queue�� ����
	while (!q.empty()) {
		int now = q.front();
		q.pop();

		for (int i = 0; i < graph[now].size(); i++) {
			int next = graph[now][i];

			// (�ٽ�) �κ��ε� ���� �Ϻ� ���� X
			result[next] = max(result[now] + times[now], result[next]);
			inDegree[next]--;
			if (inDegree[next] == 0)
				q.push(next);
		}
	}

	for (int i = 1; i <= n; i++) {
		cout << result[i] + times[i] << "\n";
	}

}