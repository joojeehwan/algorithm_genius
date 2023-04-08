#include <bits/stdc++.h>

using namespace std;

int M; //M만원 비용 지원
int N; //공항의 수
int K; //티켓 정보의 수
int T;



int main(){

    cin >> T;
    
    while(T--)
        cin >> N >> M >> K;
        vector<pair<int, int> > graph[100];
        for(int i=0; i<K; i++){
            int u,v; int c,d;
            cin >> u >> v >> c >> d;

            graph[u].push_back({v,c});
            graph[v].push_back(u);
        }
    return 0;
}