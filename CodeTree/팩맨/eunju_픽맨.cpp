#include <bits/stdc++.h>

using namespace std;
            //반시계
            //상 오른쪽위 오른쪽 오른쪽아래 아래 왼쪽아래 완쪽 왼쪽위
int dirX[] = {-1, -1,  0,  1, 1, 1, 0, 1};
int dirY[] = {0 , -1, -1, -1, 0, 1, 1, 1};

struct Point{
    int x, y;
};

struct Monster{
    Point p;
    int d;
};


Point pickman;
vector<Monster> board[5][5];    //각 위치에 픽맨이 몇마리 있는 지 담을 배열
vector<Monster> tmp_board[5][5];    //다음 턴에 위치할 몬스터들을 따로 담아둘려고
vector<Monster> tmp[5][5];
int dead[5][5][3];  //각 칸에 지속시간이 {0,1,2}인 시체의 개수

int M, T;

void copyMonster(){
    for(int i=1; i<=4; i++)
        for(int j=1; j<=4; j++)
            tmp[i][j].clear();

    
    for(int i=1; i<=4; i++){
        for(int j=1; j<=4; j++){
            //각 칸에있는 몬스터의 수만큼 복제
            for(int m=0; m<board[i][j].size(); m++){
                tmp[i][j].push_back(board[i][j][m]);
            }
        }
    }
}

void endCopyMonster(){
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            //각 칸에있는 몬스터의 수만큼 복제
            for(int m=0; m<tmp[i][j].size(); m++){
                board[i][j].push_back(tmp[i][j][m]);
            }
        }
    }
}

bool check(int nx, int ny){
    if(nx<1 || nx > 4 || ny <1 || ny >4) return false;
    if(nx == pickman.x && ny == pickman.y) return false;

    // 죽은 유령이 남아있는 지 체크
    for(int k=0; k<3; k++){
        if(dead[nx][ny][k]!=0) return false;
    }

    return true;
}

void moveMonster(){
    for(int i=1; i<=4; i++){
        for(int j=1; j<=4; j++){
            // 각 칸의 몬스터로
            for(auto m : board[i][j]){
                for(int d=0; d<8; d++){

                    int nx = i + dirX[d];
                    int ny = j + dirY[d];
                    
                    //몬스터가 갈 수 있는 곳인지 체크
                    if(check(nx,ny)){
                        tmp_board[nx][ny].push_back(m);
                        break;
                    }

                    // 몬스터가 원하는 칸으로 진행할 수 없을 때마다 
                    // 45도 꺾어주기.
                    d = (d+1)%8;
                }
            }
        }
    }

    for(int i=1; i<=4; i++){
        for(int j=1; j<=4; j++){
            board[i][j] = tmp_board[i][j];
            tmp_board[i][j].clear();
        }
    }


    
}

void removeMonster(){
    for(int i=1; i<=4; i++){
        for(int j=1; j<=4; j++){
            // 죽으면 dead[i][j][2]=1;
            //앞으로 한칸씩 옮겨주고
            // 마지막칸은 0으로
            for(int k=1; k>=0; k--){
                dead[i][j][k] = dead[i][j][k+1];
            }
            dead[i][j][2]=0;
        }
    }
}

int max_eaten;
bool visited[5][5];
vector<Point> max_route;

void calc_eaten(int turn, int eaten_cnt, vector<Point> route){
    if(turn == 4){
        if(max_eaten > eaten_cnt){
            max_eaten = eaten_cnt;
            max_route.clear();
            max_route = route;
        }
        return;
    }

    for(int d=0; d<8; d+=2){
        int nx = pickman.x + dirX[d];
        int ny = pickman.y + dirY[d];

        if(nx < 1 || nx > 4 || ny < 1 || ny >4) continue;
        if(visited[nx][ny]) continue;

        //몬스터 먹기
        visited[nx][ny] = true;
        eaten_cnt +=board[nx][ny].size();   //몬스터 먹고
        route.push_back({nx,ny});

        calc_eaten(turn+1, eaten_cnt, route);

        visited[nx][ny] = false;
        eaten_cnt -= board[nx][ny].size();
        route.pop_back();
    }
}


//3. 팩맨 이동시키기
//가장 많이 먹을 수 있는 방향으로 움이기
void movePickman(){

    //어떤 길로 갔을 때 최대로 몬스터를 먹는 지 계산해서 저장해야한다.
    visited[pickman.x][pickman.y] = true;
    calc_eaten(0,0,{});

    // 구하고 나면 몬스터 먹어버리기
    // board에 먹힌 몬스터 없애기
    // 유령 몬스터 살아있는 기간 표시
    for(int i=0; i<3; i++){
        int x = max_route[i].x;
        int y = max_route[i].y;
        
        dead[x][y][2] += board[x][y].size();
        board[x][y].clear();
    }
}

void solve(){
    while(T--){
        //1. 몬스터 복제시도
        copyMonster();
        //2. 몬스터 이동
        moveMonster();
        // //3. 픽맨 이동
        movePickman();
        // //4. 몬스터 시체 소멸
        // removeMonster();
        // //5. 몬스터 복제 완성
        // endCopyMonster();
    }

    int ans = 0;
    for(int i=1; i<=4; i++){
        for(int j=1; j<=4; j++){
            ans += board[i][j].size();
        }
    }
    cout << ans << endl;
}

int main(){
    cin >> M >> T;
    cin >> pickman.x >> pickman.y;

    for(int i=0; i<M; i++){
        int r,c,d; cin >> r >> c >> d;
        board[r][c].push_back({{r,c},d});
    }

    solve();

}