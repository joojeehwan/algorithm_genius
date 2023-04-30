#include <bits/stdc++.h>

using namespace std;

bool cmp(pair<int,int> a, pair<int,int> b){
    return a.first < b.second;
}

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    vector<vector<int>> winner(n+1, vector<int>());

    //방향이 있는 그래프 만들기
    for(int i=0; i<results.size(); i++){
        int win = results[i][0];
        int lose = results[i][1];
        winner[win].push_back(lose);
    }

    vector<int> lose_cnt(n+1,0); //각 노드가 몇명에게 졌는 지 (자신의 앞에 몇명이 있는 지 체크)
    vector<int> rank_cnt(n+1,0); //순위가 몇개인지
    vector<pair<int,int>> rank;

    //각 플레이어마다 
    for(int player=1; player<=n; player++){
        
        //1-2
        //2-5
        //3-2 
        //4-3,2 이 경우 때문에 필요
        //2는 4한테 졌지만, 3이 4한테 진 이후에 3이 누구한테 이겼는 지 확인 할 때 2를 이겼으므로 이미 3한테 진경우가 cnt 된다.
        //그래서 같은 플레이어한테 진 동료에 의해, 이미 연쇄적으로 누구한테 졌는 지 확인 된 경우에는
        // 4번한테 진 경우를 한번 더 확인할 필요 없다.
        bool visited[n+1]; fill(visited, visited+n+1, false);

        //node를 담을 곳
        queue<int> q;
        q.push(player);
        visited[player] = true;

        while(!q.empty()){
            int tmp = q.front();
            q.pop();

            //내가 이긴사람 찾아가기
            for(int i=0; i<winner[tmp].size(); i++){
                int next_player = winner[tmp][i];
                if(visited[next_player]) continue;

                q.push(next_player);
                lose_cnt[next_player]+=1;   //이 next_player는 tmp 플레이어에게 졌다는 의미로 cnt+1
                visited[next_player] = true; 
            }
        }
    }

    for(int i=1; i<=n; i++) cout << i <<" "<< lose_cnt[i]<<endl;

    for(int node = 1; node<lose_cnt.size(); node++){
        rank_cnt[lose_cnt[node]] +=1;   // 진 횟수가 같은 경우가 몇번 같은 지 확인
        rank.push_back({lose_cnt[node], node});
    }

    sort(rank.begin(), rank.end(), cmp);
    //각 노드가 진 횟수가 적은 순으로 sort
    
    // 정렬 된 후 내 위치, 내가 진 횟수가 같고
    // 진 횟수가 같은 노드가 없다면
    // lose 횟수 :  0 0 1 3 4
    // 노드 no   :  1 4 3 2 5
    for(int i=0; i<rank.size(); i++)
        if(rank[i].first == i && rank_cnt[rank[i].first]==1) 
            answer+=1;
 
    


}

int main(){

    int n=5;
    vector<vector<int>> results={{4, 3}, {4, 2}, {3, 2}, {1, 2}, {2, 5}};
    cout << solution(n, results);
    
    return 0;
}