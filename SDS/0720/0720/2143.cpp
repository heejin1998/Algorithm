#include<bits/stdc++.h>
using namespace std;
// 그렇게 큰 배열이 아니면 long으로 선언하는 습관도 ㄱㅊ음. 특히나 count 세는 경우

bool compare(long i, long j) { // 내림차순
	return j < i;
}

int main(void) {

	cin.tie(NULL);
	ios::sync_with_stdio(0);

	long t, n, m;
	

	cin >> t >> n;
	vector<long> a(n);
	
	for (int i = 0; i < n; i++)
		cin >> a[i];
	cin >> m;
	vector<long> b(m);
	for (int i = 0; i < m; i++)
		cin >> b[i];


	// 부배열 만들기
	vector<long> subA;
	vector<long> subB;

	long sum;
	
	for (int i = 0; i < n; i++) {
		sum = a[i];
		subA.push_back(sum);
		for (int j = i + 1; j < n; j++) {
			sum += a[j];
			subA.push_back(sum);
		}
	}

	for (int i = 0; i < m; i++) {
		sum = b[i];
		subB.push_back(sum);
		for (int j = i + 1; j < m; j++) {
			sum += b[j];
			subB.push_back(sum);
		}
	}
	
	// 부배열 정렬
	sort(subA.begin(), subA.end());				//오름차순
	sort(subB.begin(), subB.end(), compare); //내림차순

	

	// 슬라이딩 윈도우
	long ptA = 0;
	long ptB = 0;

	long result = 0;

	while (ptA < subA.size() && ptB < subB.size()) {

		long curA = subA[ptA];
		long target = t - curA;
		// a를 이용해 b를 찾아줄 것이다.
		if (subB[ptB] > target) {
			ptB++;
		}
		else if (subB[ptB] == target) {
			// 혹시나 같은 수가 있을 수 있기 때문에 같은 수가 몇개인지 센 다음에 경우의 수 구하기
			long countA = 0;
			long countB = 0;
			while (ptA < subA.size() && subA[ptA] == curA) {
				ptA++;
				countA++;
			}
			while (ptB < subB.size() && subB[ptB] == target) {
				ptB++;
				countB++;
			}
			result += countA * countB;
		}
		else {
			ptA++;
		}

	}
	cout << result;
	
}