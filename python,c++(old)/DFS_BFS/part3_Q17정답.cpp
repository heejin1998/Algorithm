#include <bits/stdc++.h>

using namespace std;

class Virus{
    public:
    int index;
    int second;
    int x;
    int y;

    Virus(int index, int second, int x, int y){
        this->index = index;
        this-> second = second;
        this -> x = x;
        this -> y = y;
    }
    // 정렬 기준은 번호가 낮은 순서
    bool operator < (Virus &other){
        return this->index < other.index;
    }
};

int n, k;
// 전체 보드 정보를 담는 배열
int graph[200][200];
// 바이러스에 대한 정보를 담는 리스트
vector<Virus> viruses;

// 바이러스가 퍼져나갈 수 있는 4가지 위치
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0. -1};

int main(void){
    cin >> n >> k;

    // 보드 정보 한 줄 단위로 입력
    for(int i=0; i<n;i++){
        for(int j =0;j<n;j++){
            cin >> graph[i][j]
            // 해당 위치에 바이러스 존재할 경우
            if(graph[i][j] != 0){
                viruses.push_back(Virus(graph[i][j],0,i,j));
            }
        }
    }

    // 정렬 이훼 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
    sort(viruses.begin(), viruses.end());
    queue<Virus> q;
    for(int i= 0;)
}
