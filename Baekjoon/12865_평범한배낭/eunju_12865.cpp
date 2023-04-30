#include <bits/stdc++.h>

using namespace std;

int dp[101][100001];
//dp[i][j] : 처음부터 i번째까지 물건을 넣어보고, 배낭의 용량이 j일 때 배낭에 들어간 물건의 가치 합(최대값)
//dp[N][K] : 정답

int main(){
    int N, K; cin >> N >> K;    //N개의 물건, 최대 K만큼의 무게 배낭

    vector<pair<int,int>> v;
    v.push_back({0,0});

    for(int i=1; i<=N; i++){
        int W,V; cin >> W >> V; // 무게, 가치
        v.push_back({W,V});
    }


    //napsack
    for(int i=1; i<=N; i++){
        int W = v[i].first; //  현재 물건의 무게
        int V = v[i].second;//  현재 물건의 가치

        for(int j=0; j<K+1; j++){
            // 현재 배낭 용량이 현재 물건을 넣을 수 없는 무게이면 넣지 않고
            // 현재 용량에 이전 물건을 넣었을 때 최대 가치를 넣어준다.
            if(j<W) dp[i][j] = dp[i-1][j];
            // 현재 용량에 이전 물건까지 넣었을 때의 가치 최댓값
            // 용량이 j인 배낭에 i번째 물건을 넣었을 때까지의 가치 최댓값(i-1번째 물건까지 넣었고 j용량에 W무게가 들어가기 전) 
            else dp[i][j] = max(dp[i-1][j-W]+V, dp[i-1][j]);
        }
    }

    cout << dp[N][K]<<endl;
}