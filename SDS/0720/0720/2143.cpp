#include<bits/stdc++.h>
using namespace std;
// �׷��� ū �迭�� �ƴϸ� long���� �����ϴ� ������ ������. Ư���� count ���� ���

bool compare(long i, long j) { // ��������
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


	// �ι迭 �����
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
	
	// �ι迭 ����
	sort(subA.begin(), subA.end());				//��������
	sort(subB.begin(), subB.end(), compare); //��������

	

	// �����̵� ������
	long ptA = 0;
	long ptB = 0;

	long result = 0;

	while (ptA < subA.size() && ptB < subB.size()) {

		long curA = subA[ptA];
		long target = t - curA;
		// a�� �̿��� b�� ã���� ���̴�.
		if (subB[ptB] > target) {
			ptB++;
		}
		else if (subB[ptB] == target) {
			// Ȥ�ó� ���� ���� ���� �� �ֱ� ������ ���� ���� ����� �� ������ ����� �� ���ϱ�
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