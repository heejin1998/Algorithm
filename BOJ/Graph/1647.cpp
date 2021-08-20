// MST
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<pair<int, pair<int, int>>> edges;
int parent[100001];
vector<int> results;
int result = 0;

int Find(int a) {
	if (parent[a] == a)
		return a;
	return parent[a] = Find(parent[a]);
}

void Union(int a, int b) {
	int pa = Find(a);
	int pb = Find(b);
	/*
	if (pa < pb)
		parent[pb] = pa;
	*/
	parent[pa] = pb;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		edges.push_back({ c,{a,b} });
	}

	for (int i = 0; i <= n; i++)
		parent[i] = i;

	// ����ġ ������ ����
	sort(edges.begin(), edges.end());
	
	// ������ �ϳ��� Ȯ��
	for (int i = 0; i < edges.size(); i++) {
		int cost = edges[i].first;
		int a = edges[i].second.first;
		int b = edges[i].second.second;

		// ����Ŭ�� �߻����� ������ ���տ� ����
		if (Find(a) != Find(b)) {
			Union(a, b);
			result += cost;
			results.push_back(cost);
		}
	}
	
	cout << result - *max_element(results.begin(), results.end());


}