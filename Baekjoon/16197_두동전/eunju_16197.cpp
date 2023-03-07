#include <bits/stdc++.h>

using namespace std;

int N, M;
int ans=0xffffff;

//o : 동전, . : 빈칸, # : 벽
char board[20][20];

// 버튼 : 왼쪽 오른쭉 위 아래
int dirX[] = {0,0,-1,1};
int dirY[] = {-1,1,0,0};

//동전 위치
struct{
    int x;
    int y;
}typedef Point;
vector<Point> coin;

void dfs(Point coin1, Point coin2, int dir, int cnt){
    //check
    if(cnt > 10){   
        ans = min(ans,cnt);
        return;
    }
    // 기존 횟수보다, 더 버튼을 많이 눌러야 한다면 더이상 할 이유가 없음
    if(ans < cnt) return;

    int coin1_x = coin1.x + dirX[dir];
    int coin1_y = coin1.y + dirY[dir];
    int coin2_x = coin2.x + dirX[dir];
    int coin2_y = coin2.y + dirY[dir];

    //case1. 두 동전이 board 밖으로 모두 떨어지는 경우
    //더이상 진행할 이유가 없음.
    if((coin1_x <0 || coin1_x >N-1 || coin1_y <0 || coin1_y >M-1) && (coin2_x <0 || coin2_x >N-1 || coin2_y <0 || coin2_y >M-1)){
        return;
    }
    //case2. 두 동전 중 한 동전만 떨어지는 경우
    //1번동전 떨어짐, 2번동전 보드 안
    else if((coin1_x <0 || coin1_x >N-1 || coin1_y <0 || coin1_y >M-1) && (coin2_x>=0 && coin2_x<=N-1 && coin2_y >=0 && coin2_y<=M-1)){
        ans = min(ans, cnt);
        return;
    }
    //1번동전 보드 안, 2번동전 떨어짐
    else if( (coin1_x>=0 && coin1_x<=N-1 && coin1_y >=0 && coin1_y<=M-1) && (coin2_x <0 || coin2_x >N-1 || coin2_y <0 || coin2_y >M-1)){
        ans = min(ans, cnt);
        return;
    }

    //이동하려는 칸이 벽이면 이동하지 않는다
    if(board[coin1_x][coin1_y] =='#'){
        coin1_x = coin1.x;
        coin1_y = coin1.y;
    }
    if(board[coin2_x][coin2_y] =='#'){
        coin2_x = coin2.x;
        coin2_y = coin2.y;
    }

    //4방향으로 이동시키기
    for(int i=0; i<4; i++){
        dfs({coin1_x,coin1_y},{coin2_x,coin2_y},i,cnt+1);
    }
            
}

void solve(){
    //버튼을 4방향으로 눌러보면서
    //두 동전 중 하나만 떨어졌는 지 확인
    for(int i=0; i<4; i++)
        dfs(coin[0], coin[1], i, 1);    //coin1, coin2, dir, cnt

    //ans
    if(ans > 10)cout << -1<<"\n";
    else cout << ans <<"\n";
}

int main(){

    //최소의 버튼을 누르기 위한 경우
    cin >> N >> M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin >> board[i][j];
            if(board[i][j]=='o') coin.push_back({i,j}); 
        }
    }
    
    solve();
    

    return 0;
}
