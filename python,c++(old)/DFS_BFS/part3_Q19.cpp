// 백트래킹
#include <bits/stdc++.h>
using namespace std;
#define endl "\n"

int n;
int add, sub, mul, Div;
vector<int> nums;
int max_result = -1e9;
int min_result = 1e9;



void dfs(int cnt, int add, int sub, int mul, int Div, int result) {
	if (cnt == n) {
		max_result = max(result, max_result);
		min_result = min(result, min_result);
	}

	if (add > 0)
		dfs(cnt + 1, add-1, sub, mul, Div, result + nums[cnt]);
	if (sub > 0)
		dfs(cnt + 1, add, sub-1, mul, Div, result - nums[cnt]);
	if (mul > 0)
		dfs(cnt + 1, add, sub, mul-1, Div, result * nums[cnt]);
	if (Div > 0)
		dfs(cnt + 1, add, sub, mul, Div-1, result / nums[cnt]);
	
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);
	cout.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		nums.push_back(num);
	}

	cin >> add >> sub >> mul >> Div;

	dfs(1, add, sub, mul, Div, nums[0]);

	cout << max_result << endl;
	cout << min_result << endl;
}