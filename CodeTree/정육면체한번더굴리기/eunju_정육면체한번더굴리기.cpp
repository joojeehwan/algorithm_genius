#include <bits/stdc++.h>

using namespace std;

int N, M;

int board[21][21];
int total_score=0;
bool visited[21][21];

/**
 * 1
 * 2
 * 6 3 1 4 
 * 5
 * 
 * 진행방향에 따라 주사위 위치, 바닥 면 업데이트 해 줄 예정
*/
pair<int,int> dicePos={1,1};
int BOTTOM = 6; // top : 1
int RIGHT = 3;  // left : 4
int FRONT = 2;  // back : 5


//0 (위) 1(오른쪽) 2(아래) 3(왼쪽)
int direction = 1;  //첨엔 오른쪽
int dirX[] = {-1, 0, 1, 0};
int dirY[] = {0, 1, 0, -1};

void input(){
    cin >> N >> M;
    for(int i=1; i<=N; i++)
        for(int j=1; j<=N; j++)
            cin >> board[i][j];
}

int getScore(){

    for(int i=0; i<N+1; i++)
    memset(visited[i],false,sizeof(bool)*N+1);

    queue<pair<int,int>> q;
    q.push(dicePos);
    visited[dicePos.first][dicePos.second]=true;
    // cout <<"dice "<<dicePos.first <<" "<<  dicePos.second<<endl;
    int cnt=1;

    while(!q.empty()){
        pair<int,int> p = q.front(); q.pop();
        
        for(int i=0; i<4; i++){
            int nx = p.first + dirX[i];
            int ny = p.second + dirY[i];
                // cout << nx<< ",, "<<ny<<" L ";
            if(nx < 1 || nx > N || ny<1 || ny >N){continue;}
            if(board[nx][ny] != board[dicePos.first][dicePos.second]) { continue;}
            if(visited[nx][ny]==true) {continue;}
            // cout <<"asdasdasd"<<endl;
            visited[nx][ny] = true;
            cnt +=1;
            q.push({nx,ny});
        }
        
    }
    // cout<< "scode "<< cnt <<"* "<< board[dicePos.first][dicePos.second]<<endl;
    return cnt * board[dicePos.first][dicePos.second];
}

//1. 주사위의 아랫면이 보드의 해당 칸에 있는 숫자보다 크면
//현재 진행방향에서 90' 시계방향으로 회전

//2. 주사위의 아랫면의 숫자가 더 작다면 
//현재 진행방향에서 90' 반시계방향으로 회전

//3. 만약 진행 도중 격자판을 벗어나게 된다면, 
//반사되어 방향이 반대로 바뀌게 된 뒤 한 칸 움직이게 됩니다. == 반사

pair<int, int> movePos(){
    int curX = dicePos.first;
    int curY = dicePos.second;

    int nx = curX + dirX[direction];
    int ny = curY + dirY[direction];

    if(nx < 1 || nx > N || ny<1 ||  ny> N){
        return {-1,-1};
    }
    return {nx,ny};

    
}


void rolling_dice(int turn){
    // 주사위를 계속 1칸씩 굴리게 됩니다
    // 1행 1열에 놓여져 있고, 처음에는 항상 오른쪽으로 움직입니다.

    //1. 방향 조절하기
    if(turn > 0){
        if(direction == 0){ //위
            tie(FRONT,RIGHT,BOTTOM) = make_tuple(BOTTOM,RIGHT, 7-FRONT);
        }
        else if(direction == 1){    //오른쪽
            tie(FRONT,RIGHT,BOTTOM) = make_tuple(FRONT,7-BOTTOM, RIGHT);
        }
        else if(direction == 2){    //아래
            tie(FRONT,RIGHT,BOTTOM) = make_tuple(7-BOTTOM,RIGHT, FRONT);
        }
        else if(direction == 3){    //왼쪽
            tie(FRONT,RIGHT,BOTTOM) = make_tuple(FRONT, BOTTOM, 7-RIGHT);
        }

        if(BOTTOM > board[dicePos.first][dicePos.second])
            direction = (direction+1)%4;

        else if(BOTTOM < board[dicePos.first][dicePos.second])
            direction = (direction-1+4)%4;
    }
    // cout <<"===turn ==="<<turn<<endl;
    // cout << "FRONT,RIGHT,BOTTOM "<<FRONT<<", "<<RIGHT<<", " <<BOTTOM <<"/"<< board[dicePos.first][dicePos.second]<<endl;
    // cout <<"direction : "<<direction<<endl;
    //2. 주사위 좌표 움직이기
    pair<int, int> next_pos= movePos();
    if(next_pos.first == -1 && next_pos.second == -1){
        direction ^= 2;
        next_pos = movePos();
        // cout <<"durwjs"<<endl;
    }
    
    dicePos = next_pos;


    //3. 점수 얻기
    total_score += getScore();

    // cout <<  total_score <<endl;
    // cout << dicePos.first<<", "<<dicePos.second <<endl;

}

void sovle(){
    for(int i=0; i<M; i++){
        //주사위 움직이기
        rolling_dice(i);
        
    }
}

int main(){

    input();
    sovle();

    cout << total_score<<endl;

    return 0;
}