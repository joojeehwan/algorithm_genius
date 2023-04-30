#include <bits/stdc++.h>

using namespace std;

int N, M;
int board[300][300];
bool visited[300][300];

struct Point{
    int x;
    int y;
};

vector<Point> ice;
int dirX[] = {-1,0,1,0};
int dirY[] = {0,1,0,-1};

void bfs(Point point){
    queue<Point> q;
    q.push(point);

    while(!q.empty()){
        Point p = q.front();
        q.pop();

        for(int i=0; i<4; i++){
            int nx = p.x + dirX[i];
            int ny = p.y + dirY[i];
            if(nx < 0 || nx > N-1 || ny <0 || ny > M-1) continue;
            if(visited[nx][ny]) continue;
            if(board[nx][ny] <=0) continue; //빙산이 아니면 스킵

            visited[nx][ny] = true;
            q.push({nx,ny});
        }
    }
}

int count_area(int year){
    fill(&visited[0][0], &visited[N-1][M], false);
    int cnt = 0;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(board[i][j] >0 && !visited[i][j]){
                cnt += 1;
                bfs({i,j});
            }
        }
    }
    return cnt;
}

/*바다 갯수 세기*/
int count_ocean(Point p){
    int cnt = 0;
    for(int i=0; i<4; i++){
        int nx = p.x + dirX[i];
        int ny = p.y + dirY[i];
        if(nx < 0 || nx > N-1 || ny < 0 || ny > M-1) continue;
        if(board[nx][ny]>0) continue;   // 바다가 있으면 카운트
        cnt+=1; 
    }
    return cnt;
}

void print(){
    cout<<endl;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cout << board[i][j]<<" ";
        }cout <<endl;
    }
    cout <<endl;
}

void remove_ice(){

    //삐용삐용
    //바로 깎으면 안됨
    // 깎아야하는 칸을 모아서 한번에 깎기
    // 바로 깎으니깐 아래처럼 같은 년도에서 먼저 깎인 빙산도 바다로 세서 본인 빙산 높이를 깎음
    // 같은 년도에 살아있는 빙산은 그 년도가 지나기 전에는 살아있는걸로 간주해야 함.
    // 0 0 0 0 0 0 0
    // 0 2 4 5 3 0 0
    // 0 3 0 2 5 2 0
    // 0 7 6 2 4 0 0
    // 0 0 0 0 0 0 0

    // 0 0 0 0 0 0 0 
    // 0 0 1 4 1 0 0 
    // 0 0 0 1 5 -1 0 
    // 0 4 4 1 2 0 0 
    // 0 0 0 0 0 0 0

    int tmp[300][300];
    fill(&tmp[0][0], &tmp[N-1][M], 0);

    //모든 칸을 확인라하면서
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            //빙산이 있으묜
            if(board[i][j] > 0){
                //주변에 바다가 몇면인지 세서
                int cnt = count_ocean({i,j});
                tmp[i][j] = cnt;
            }
        }
    }
    
    //깎아버리기
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            board[i][j] -=tmp[i][j];
        }
    }
    print();
}

void solve(){
    int year = 0;

    while(true){
        // 빙산이 몇등분인지 체크
        int cnt = count_area(year);
        //빙산이 최초로 2개 이상으로 분리되면 끛
        if(cnt >= 2){
            cout << year << "\n";
            break;
        }
        //만약에 빙산이 다 녹을 때까지 분리되지 않으면 출력하고 끝
        else if(cnt == 0) {
            cout << 0 << "\n";
            break;
        }

        // 매 년마다 얼음이 녹는다.
        // 각 칸의 주변에 바닷물이 접한 면이 몇개인지 체크해서
        // 그 갯수만큼 빙산 깎기
        remove_ice();
        
        //연도 증가시키기
        year += 1;
    }
}

int main (){
    cin >> N >> M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin >> board[i][j];
        }
    }

    solve();
    


}