#include <bits/stdc++.h>

using namespace std;

int N, M, K;    //총 격자의 크기, 팀의 개수, 총 진행하는 라운드의 수
int board[21][21];
int score[6];
int dirX[] = {-1,0,1,0};
int dirY[] = {0,1,0,-1};
int total_score = 0;

struct Point{
    int x;
    int y;
};

struct Info{
    int length;
    int dir = 1; //1 : right, -1 : left
    vector<Point> line; //좌표를 dir 방향으로 한 칸씩 옮겨줌
};
Info team[6];

//1 - 머리사람, 2 - 나머지사람, 3 - 꼬리사람
//4 - 이동 선

//하나의 이동 선에는 하나의 팀만이 존재

void change_dir(int teamNo){
    //맞은 팀이 없을 경우 순서 바꿀필요 X
    if(teamNo == -1) return;

    //맞은 팀의 순서를 바꿔준다..
    //공을 획득한 팀의 경우에는 머리사람과 꼬리사람이 바뀝니다. 즉 방향을 바꾸게 됩니다.
    //1 2 3 4a 4b 4c 4d order
    //1 2 3 4  5  6  7 idx
    //3 2 1 4d 4c 4b 4a order

    reverse(team[teamNo].line.begin(), team[teamNo].line.begin() + team[teamNo].length);
    reverse(team[teamNo].line.begin() + team[teamNo].length, team[teamNo].line.end());

    //board update
    for(int i=0; i<team[teamNo].line.size(); i++){
        Point p = team[teamNo].line[i];

        //만약 4가 아니라면 좌표의 값 증가시켜주기
        if(i+1 > team[teamNo].length) board[p.x][p.y] = 4;
        else if(i+1 < team[teamNo].length && i+1 > 1)  board[p.x][p.y] = 2;
        else if(i+1 == team[teamNo].length)board[p.x][p.y] = 3;
        else if(i+1 == 1) board[p.x][p.y] = 1;
    }
}


int get_score(Point target){
    //이 사람의 좌표를 가진 팀이 point get

    for(int m=0; m<M; m++){
        for(int i=0; i<team[m].line.size(); i++){
            if(team[m].line[i].x == target.x && team[m].line[i].y== target.y){
                total_score+= pow(i+1,2);
                cout <<  "score : "<< pow(i+1,2)<<endl;
                // cout << "total_score : " << total_score<<endl;
                // cout << i<<endl;
                return m;
            }
        }
    }
    return -1;
}

Point shoot(int kround){
    // n : 7
    // 29번째 == 1
    // 13번째 == 13%(4*7) = 13/28
    // 30번째 == 
    // 오른쪽 - 1~N번 - 위~아래
    // 위쪽 - N+1 ~ 2N번 - 왼~오른
    // 왼쪽 - 2N+1 ~ 3N번 - 아래~위
    // 아래쪽 - 3N+1 ~ 4N번 - 오른~왼

    Point hit_point;
    bool hit = false;
    kround = (kround) % (4*N) -1;    //kround는 1qnxj

    if(kround <= N){
        //왼쪽->오른쪽 
        for(int i=0; i<N; i++){
            //만약에 사람이 있으면 
            if(1 <= board[kround][i] && board[kround][i] <=3){
                // cout << board[kround][i]<<endl;
               hit_point = {kround, i};
               hit = true;
               break; 
            }
        }
    }
    else if(kround<=2*N){
        //아래 -> 위
        //X위치가 N~0
        // N+1 ~ 2*N -> 1~N
        // kround
        kround-=N;
        for(int i=N-1; i>=0; i--){
            if(1 <= board[i][kround] && board[i][kround] <=3){
               hit_point = {i, kround};
               hit = true;
               break; 
            }
        }

    }
    else if(kround<=3*N){
        //오른쪽 -> 왼쪽, 밑에서 위로
        kround-=2*N;
        for(int i=N-1; i>=0; i--){
            if(1 <= board[N-kround][i] && board[N-kround][i] <=3){
               hit_point = {N-kround, i};
               hit = true;
               break; 
            }
        }
    }
    else if(kround<=4*N){   //4N이 넘어가면 4N+1
        kround-=3*N;
        for(int i=N-1; i>=0; i--){
            if(1 <= board[i][N-kround] && board[i][N-kround] <=3){
                hit_point = {i, N-kround};
                hit = true;
                break; 
            }
        }
    }
    if(hit) return hit_point;
    else return {-1,-1};
}

//1 - 머리사람, 2 - 나머지사람, 3 - 꼬리사람
//4 - 이동 선
void move(){
    // //머리 사람이 이동 선을 따라 1칸 이동
    // for(int i=0; i<N; i++){
    //     for(int j=0; j<N; j++){
    //         if(arr[][])
    //     }   
    // }

    //모든 팀이 앞으로 1칸 이동
    for(int m=0; m<M; m++){
        Point tmp = team[m].line[team[m].line.size()-1];
        for(int i=team[m].line.size()-1; i>0; i--){
            team[m].line[i] = team[m].line[i-1];
        }
        team[m].line[0] = tmp;
    }
    


    //board update
    for(int m=0; m<M; m++){
        for(int i=0; i<team[m].line.size(); i++){
            Point p = {team[m].line[i].x, team[m].line[i].y};

            //만약 4가 아니라면 좌표의 값 증가시켜주기
            if(i+1 > team[m].length) board[p.x][p.y] = 4;
            else if(i+1 < team[m].length && i+1 > 1)  board[p.x][p.y] = 2;
            else if(i+1 == team[m].length)board[p.x][p.y] = 3;
            else if(i+1 == 1) board[p.x][p.y] = 1;
        }
    }
}

bool visited[21][21];

void dfs(int x, int y, int idx, int len){

    if(board[x][y] == 1 && team[idx].line.size()!=0){
        return;
    } 
    if(board[x][y] == 3) team[idx].length=len;

    team[idx].line.push_back({x,y});
    visited[x][y] = true;

    
    for(int i=0; i<4; i++){
        int nx = x + dirX[i];
        int ny = y + dirY[i];

        if(nx <0 || nx >N-1 | ny<0 || ny>N-1) continue;
        if(board[nx][ny]==0) continue;
        if(visited[nx][ny]) continue;
        if(board[x][y]==1 && board[nx][ny]==4) continue;
        
        dfs(nx, ny, idx, len+1);
    }

}


void sep_team(){

    int cnt = 0;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(board[i][j]==1){          
                dfs(i,j, cnt++, 1);
            }
        }
    }

}

void solve(){

    //구역 나누기
    sep_team();

    for(int i=0; i<M; i++){
        cout << "ppl "<<i<<"\n";
        for(auto pl : team[i].line)                                                                                                                                                                                                                                                                 
            cout <<pl.x <<", "<<pl.y<<"\n";

    //     // cout << "street\n";
    //     // for(auto st : info[i].street)
    //     //     cout <<st.x <<", "<<st.y<<"\n";
        cout <<"size : "<<team[i].length<<endl;
    }


    //K라운드
    int kround=1;
    while(K--){ 
        //1. 머리사람을 따라 모든 팀 1칸 이동
        move();
        cout<<endl;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                cout << board[i][j]<<" ";          
                
            }cout <<endl;
        }
        //2. 공 발사
        Point hit_point = shoot(kround++); 
        // cout << hit_point.x << " "<<hit_point.y<<endl;
        //3. 가장 먼저 맞는 사람 점수 획득
        int hit_team = get_score(hit_point);

        //4. 점수 획득한 팀 방향 바꾸기 - 팀 정보 필요
        change_dir(hit_team);
    }

}

int main(){
    
    cin >> N >> M >> K;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin >> board[i][j];
        }
    }

    solve();

    cout << total_score;

    return 0;
}