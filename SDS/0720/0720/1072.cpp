#include <bits/stdc++.h>
using namespace std;

int main(void) {

	cin.tie(0);
	ios::sync_with_stdio(0);

	long x, y;
	cin >> x >> y;
	
	long percent = 100 * y / x;
	cout << "percent: " << percent<<endl;
	
	if (percent>=99) { // �Ұ����� ���
		cout << -1;
		return 0;
	}

	long start = 0;
	long end = x;
	
	while (start < end) {
		long mid = (start + end) / 2;
		long new_percent = (100 * (y + mid) / (x + mid));
		if (new_percent == percent) {	// �·� �� �ٲ� ���
			start = mid + 1; // ���� mid�� �ʿ����. �׷��Ƿ� start = mid + 1 �ϱ�
		}
		else { // �·��� �ٲ���� ��
			end = mid; // mid�� ���� �� �� ������ ����� �Ѵ�. end = mid - 1 ��������

		}
			
		
	}
	
	cout << end;
}