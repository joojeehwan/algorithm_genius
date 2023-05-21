#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<pair<int,int>> graph[10001];
bool visited[10001];

int main(){

    // 최소 간선을 선택하고
    // 그 선이랑 연결된 선들 중에 가장 최소비용인 간선을 계속해서 선택해 나가다가
    // 더이상 선택할 선이 없으면 break

    cin >> N >> M;

    
    // [a, b, c]
    int minA, minB, minC=10001;

    for(int i=0; i<M; i++){
        int a, b, c; cin >> a >> b >> c;
        graph[a].push_back({b,c});
        graph[b].push_back({a,c});
    }
    
    //solve - prim
    // 최소비용 누적할 변수
    int ans = 0;
    //가중치가 가장 낮은 점을 뽑으려고 {비용, 컴퓨터}
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > pq;
    pq.push({0,1});
    //모든 정점을 확인하면서 그 점이랑 이어질 점을 확인
    for(int i=1; i<=N; i++){

        //이미 한번 방문한 점은 pass
        while(!pq.empty() && visited[pq.top().second]) pq.pop();
        
        //1번이랑 점이랑 이어진 점 중에서 방문하지 않은 점, edge[1][next]가중치가 가장 낮은 점
        int next = pq.top().second;
        int cost = pq.top().first;
        visited[next] = true; 

        ans += cost;

        cout << "next : "<< next <<endl;
        cout <<"cost : "<<cost <<endl<<endl;
        
        
        for(auto e : graph[next])
            pq.push({e.second, e.first});   //비용, 간선

    }

    cout << ans;

    return 0;
}