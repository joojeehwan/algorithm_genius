#include <bits/stdc++.h>

using namespace std;

bool visited[100][100];
int dirX[] = {-1,0 ,1, 0};
int dirY[] = {0, 1, 0, -1};
int N, M;
vector<int> answer;
vector<string> maps;

void bfs(int x, int y ){
    
    queue<pair<int, int> > q;
    q.push({x, y});
    int sum = maps[x][y]-'0';

    visited[x][y] = true;
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i=0; i<4; i++){
            int nx = x + dirX[i];
            int ny = y + dirY[i];

            if(nx < 0 || nx >N-1 || ny<0 || ny >M-1 ) continue;
            if(maps[nx][ny] == 'X') continue;
            if(visited[nx][ny]) continue;
            
            q.push({nx,ny});
            visited[nx][ny] = true;
            sum+=maps[nx][ny] - '0';
        }
    }
    answer.push_back(sum);
}


vector<int> solution(vector<string> maps) {
    
    N = maps.size(); M = maps[0].size();

    fill(&visited[0][0], &visited[N-1][M], false);

    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(!visited[i][j] && maps[i][j]!='X'){
                bfs(i, j);
            }
        }
    }

    sort(answer.begin(), answer.end());

    if(answer.size()!=0)
        for(auto ans : answer)cout <<ans << " ";
    else
        cout << -1;
    
    return answer;
}

int main(){

    vector<string> maps = {"X591X","X1X5X","X231X", "1XXX1"};
    solution(maps) ;

    return 0;
}