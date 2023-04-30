#include <bits/stdc++.h>

using namespace std;

struct cmp{
    bool operator() (pair<int,int> a, pair<int,int> b){
        return a.second > b.second; //a에 우선순위
    }
};

//현재 지점에서 모든 지점까지 최소비용을 구해야해서
void dijkstra(vector<int> &node_cost, vector<vector<int>> graph, int n, int start){

    //pair {노드, 비용} 
    priority_queue<pair<int,int>, vector<pair<int,int>>, cmp> pq;   //가장 적은 비용인 경우 pop되도록
    pq.push({start, 0});
    node_cost[start] = 0;

    while(!pq.empty()){
        int curr = pq.top().first;
        int cost = pq.top().second;
        pq.pop();

        // curr 정점으로부터 모든 정점까지 비용 계산
        for(int i=1; i<=n; i++){
            if(graph[curr][i]==0) continue; //이어져 있는 간선만

            // 현재까지 비용에 다음노드까지 가는 비용이 
            // 더 적으면 그 경로 비용으로 갱신
            if(node_cost[i] > cost + graph[curr][i]){
                node_cost[i] = cost + graph[curr][i];
                pq.push({i, graph[curr][i] + cost});    //현재 방문한 노드, 비용 push
            }
        }
    }
}

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = 0xffffff;

    //연결된 노드끼리 가중치 정보를 담을 그래프
    vector<vector<int> > graph(n+1, vector<int>(n+1, 0));

    for(auto fare : fares){
        int a = fare[0];
        int b = fare[1];
        int g = fare[2];
        graph[a][b] = g;
        graph[b][a] = g;
    }

    //시작으로부터 각 정점까지의 최소비용 담을 배열
    //S로부터 모든 정점까지의 최단경로
    vector<int> S(n+1, 0xffffff);  
    dijkstra(S, graph, n, s); 

    //A로부터 모든 정점까지의 최단경로  A -> i
    vector<int> A(n+1, 0xffffff);
    dijkstra(A, graph, n, a); 

    //B로부터 모든 정점까지의 최단경로  B -> i
    vector<int> B(n+1, 0xffffff);
    dijkstra(B, graph, n, b); 


    //(S->i) + (i->A) + (i->B)
    for(int i=1; i<=n; i++){
        int ans = S[i] + A[i] + B[i];
        answer = min(answer, ans);
    }

    return answer;
}

int main(){

    int n=6;
    int s=4;
    int a=6;
    int b=2;
    vector<vector<int>> fares = {
            {4, 1, 10},
            {3, 5, 24},
            {5, 6, 2},
            {3, 1, 41},
            {5, 1, 24},
            {4, 6, 50},
            {2, 4, 66},
            {2, 3, 22},
            {1, 6, 25}
    };

    cout << solution( n,  s,  a, b, fares);

    return 0;
}