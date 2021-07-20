#include <bits/stdc++.h>
using namespace std;

int main() {
	
	cin.tie(NULL);
	ios::sync_with_stdio(0);
	
	long long n, m;
	cin >> n >> m;
	vector<long long> trees(n);
	for (long long i = 0; i < n; i++) {
		cin >> trees[i];
	}
	
	
	long long start = 0;
	long long end = *max_element(trees.begin(), trees.end()); // 가장 긴 길이를 h로 설정
	
	long long result = 0;
	long long sum;

	
	while (start<=end) {
		
		sum = 0;
		long long mid = (start + end) / 2;
		for (long i = 0; i < trees.size();i++) {
			long long len = trees[i] - mid;
			if (len > 0) {
				sum += len;
			}
		}
		if (sum == m) {
			result = mid;
			break;
		}
		else if (sum < m) {
			end = mid-1;
			
		}
		else if(sum > m){
			start = mid+1;
			result = mid;
			
		}
		
	}
	cout << result;
}