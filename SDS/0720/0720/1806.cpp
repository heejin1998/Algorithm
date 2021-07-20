#include<bits/stdc++.h>
using namespace std;

int main(void) {

	cin.tie(NULL);
	ios::sync_with_stdio(0);
	int n, s;
	cin >> n >> s;
	vector<int> nums;
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		nums.push_back(num);
	}

	int left = 0;
	int right = 0;
	int sum = nums[0];
	int result = 100000000;

	while (right < n) {
		if (sum < s) {
			right++;
			if (right < n) {
				sum += nums[right];
			}
		}
		else if (sum >= s) {
			int new_result = right - left + 1;
			result = min(result, new_result);
			left++;
			sum -= nums[left - 1];
		}
		
	}
	if (result == 100000000)  cout << 0;
	else cout << result;
}