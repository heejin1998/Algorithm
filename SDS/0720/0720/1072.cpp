#include <bits/stdc++.h>
using namespace std;

int main(void) {

	cin.tie(0);
	ios::sync_with_stdio(0);

	long x, y;
	cin >> x >> y;
	
	long percent = 100 * y / x;
	cout << "percent: " << percent<<endl;
	
	if (percent>=99) { // 불가능한 경우
		cout << -1;
		return 0;
	}

	long start = 0;
	long end = x;
	
	while (start < end) {
		long mid = (start + end) / 2;
		long new_percent = (100 * (y + mid) / (x + mid));
		if (new_percent == percent) {	// 승률 안 바뀐 경우
			start = mid + 1; // 여기 mid는 필요없다. 그러므로 start = mid + 1 하기
		}
		else { // 승률이 바뀌었을 때
			end = mid; // mid가 답이 될 수 있으니 살려야 한다. end = mid - 1 하지말기

		}
			
		
	}
	
	cout << end;
}