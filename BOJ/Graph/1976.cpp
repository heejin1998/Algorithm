// Union-Find
#include <bits/stdc++.h>
using namespace std;

int n, m;
int parent[201];

int Find(int a) {
	if (parent[a] == a)
		return a;
	return parent[a] = Find(parent[a]);
}

void Union(int a, int b) {
	int pa = Find(a);
	int pb = Find(b);
	if (pa < pb)
		parent[pb] = pa;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);

	cin >> n >> m;

	for (int i = 1; i <= n; i++)
		parent[i] = i;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			int num;
			cin >> num;
			if (num == 1) {
				Union(i, j);
			}
		}
	}
	vector<int> plans;
	for (int i = 0; i < m; i++) {
		int num;
		cin >> num;
		plans.push_back(num);
	}
	
	
	for (int i = 0; i < plans.size()-1; i++) {
		if (Find(plans[i]) != Find(plans[i + 1])) {
			cout << "NO\n";
			return 0;
		}
	}
	cout << "YES\n";
	return 0;
	
}