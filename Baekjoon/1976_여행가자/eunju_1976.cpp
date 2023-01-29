#include <bits/stdc++.h>

using namespace std;

int N, M;                // 도시의 수, 여행계획에 속한 도시의 수
int plan[1001];          //여행계획
int parent[1001];        //parent
int rnk[1001];          //rank - 트리의 높이
int link[1001][1001];    //연결여부

int find(int u){
    if(parent[u] == u) return u;
    else return parent[u] = find(parent[u]);
}

void merge(int u, int v){
    u = find(u);
    v = find(v);

    //더 낮은 높이를 가진 트리를
    //더 높은 트리 밑으로 합치면, 
    //높이가 더 큰쪽으로 유지되어 find 연산을 빠르게 할 수 있음.
    if(rnk[u] > rnk[v]) swap(u,v);
    parent[u] = v;
    if(rnk[u] == rnk[v]) ++rnk[v];
}

int main(){
    cin >> N >> M;
    //연결정보
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            cin >> link[i][j];
        }
    }

    //여행 계획
    for(int i=1; i<=M; i++)
        cin >> plan[i];

    //각 도시의 parent 초기화
    for(int i=1; i<=N; i++)
        parent[i] = i;


    //1. 연결정보로 도시 union 실행
    // i가 j랑 연결되어 있다면 union
    for(int i=1; i<=N; i++)
        for(int j=1; j<=N; j++)
            if(link[i][j])
                merge(i, j);


    //2. 여행 계획 도시들이, 서로 연결되어 있는 지 find
    // find 수행 시  경로 업데이트 -> 수행시간 단축
    int index = find(plan[1]);
    //plan된 도시들의 parent가 모두 같으면 YES
    for(int i=2; i<=M; i++)
        if(index!=find(plan[i])){
            cout << "NO"<<"\n";
            return 0;
        }
    
    cout <<"YES"<<"\n";

    return 0;
}