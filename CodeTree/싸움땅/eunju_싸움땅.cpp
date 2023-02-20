#include <bits/stdc++.h>

using namespace std;

int N, M, K; //격자 크기, 플레이어 수, 라운드 수
priority_queue<int> board[21][21]; // 총의 정보가 있는 격자

struct{
    int x,y;
    int d; //위 오른쪽 아래 왼쪽 - 시계방향 
    int s; //초기 능력치
    int gun; //매번 줍는 가장 공격력이 큰 총
    int point; // 포인트
}typedef Player;
Player player[31];

int dirXY[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};

void move(int i){
    int d = player[i].d;
    int nx = player[i].x + dirXY[d][0];
    int ny = player[i].y + dirXY[d][1];
    if(nx<0 || nx>N-1 || ny<0 || ny>N-1){
        d ^= 2; 
        player[i].d ^= 2; 
        nx = player[i].x + dirXY[d][0];
        ny = player[i].y + dirXY[d][1];
    }
    player[i].x = nx;
    player[i].y = ny;
}

void select_gun(int i){
    int x = player[i].x;
    int y = player[i].y;

    if(board[x][y].empty()){
        player[i].gun = 0;
        return;
    }

    player[i].gun = board[x][y].top();
    board[x][y].pop();
}

void put_gun(int i){
    int x = player[i].x;
    int y = player[i].y;
    board[x][y].push(player[i].gun);
    player[i].gun = 0;
}


int check_player_in_board(int x, int y, int p){
    for(int i=0; i<M; i++){
        if(i==p) continue;
        if(x == player[i].x && y == player[i].y){
            return i;
        }   
    }
    return -1;
}

void lose(int p){
    put_gun(p);
    //한 칸 이동
    int d = player[p].d;
    int nx = player[p].x + dirXY[d][0];
    int ny = player[p].y + dirXY[d][1];
    //90도씩 시계방향으로 돌면서 
    //격자 범위 밖 || 다른 플에이어 존재 한다면
    //방향, 위치 바꿔주기
    while(nx<0 || nx>N-1 || ny<0 || ny >N-1 || check_player_in_board(nx,ny,p)!=-1){
        d = (d+1)%4;
        nx = player[p].x + dirXY[d][0];
        ny = player[p].y + dirXY[d][1];
    }
    player[p].x = nx;
    player[p].y = ny;
    player[p].d = d;

    select_gun(p);
}

void win(int p){
    put_gun(p);
    select_gun(p);
}

bool cmpr(int i, int ni){
    int p1 = player[i].s + player[i].gun;
    int p2 = player[ni].s + player[ni].gun;
    if (p1 != p2) 
        return p1 > p2;
    return player[i].s > player[ni].s;
}

void fight(int i, int ni){
    int p1 = player[i].gun + player[i].s;
    int p2 = player[ni].gun + player[ni].s;
    int diff = p1-p2;
    if(cmpr(i,ni)){   //i가 이긴경우
        player[i].point += diff;
        lose(ni);
        win(i); 
    }
    else{   //i가 진 경우
        player[ni].point += -diff;
        lose(i);
        win(ni); 
    }
}

void solve(){
    //1. 플레이어 순차 이동
    for(int k=0; k<K; k++){
        for(int i=0; i<M; i++){
            move(i);
            //플레이어 존재
            int n_player = check_player_in_board(player[i].x,player[i].y,i);
            if(n_player!=-1){ //플레이어가 있는 경우
                fight(i, n_player);
            }
            else{   //플레이어가 없는 경우
                put_gun(i);
                select_gun(i);
            }
        }
    }

    for(int i=0; i<M; i++)
        cout << player[i].point<<" ";
}


int main() {
    //input
    cin >> N >> M >> K;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            int a; cin >> a;
            board[i][j].push(a);
        }
    }
    for(int i=0; i<M; i++){
        int x,y,d,s; cin >> x >> y >> d >> s;
        player[i] = {x-1,y-1,d,s,0,0};
    }

    solve();
    
    return 0;
}