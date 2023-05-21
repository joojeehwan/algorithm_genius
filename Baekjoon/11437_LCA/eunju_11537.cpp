#include <bits/stdc++.h>

using namespace std;

vector<int> graph[50001];
bool visited[50001];
int parent[50001];
int level[50001];

int LCA(int a, int b){

    //level[a] < level[b] 탐색을 최소로 만들기위해
    if(level[a] > level[b]) swap(a, b);
    
    //같은 레벨로 만들기
    while(level[a] != level[b]){
        b = parent[b];
    }

    //공통 부모 찾기
    while(1){
        if(a == b) break;
        a = parent[a];
        b = parent[b];
    }

    return a;
}

int main(){

    int N; cin >> N;
    for(int i=0; i<N-1; i++){
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        int a, b; cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }  

    queue<int> q; q.push(1);
    visited[1] = true;

    //level, parent 기록
    while(!q.empty()){
        int cur = q.front();
        q.pop();

        for(int i=0; i<graph[cur].size(); i++){
            int next = graph[cur][i];
            
            if(visited[next]) continue;
            visited[next] = true;
            level[next] = level[cur]+1;
            parent[next] = cur;
            q.push(next);
        }   
    }

    int M; cin >> M;
    for(int i=0; i<M; i++){
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        int a, b; cin >> a >> b;
        cout << LCA(a, b) << "\n";
    }

    return 0;
}