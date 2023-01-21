#include <bits/stdc++.h>

using namespace std;

char board[25][25];
int visited[25][25];
int R,C; 

//위(0) 아래(1) 왼쪽(2) 오른쪽(3)
int dirX[] = {-1,1,0,0};
int dirY[] = {0,0,-1,1};

//각 가스관이 뚫려있는 위치   -      |      +     1      2      3      4   
string direction[] = {"1100","0011","1111","0101","1001","1010","0110"};
char pipes[] = {'|','-','+','1','2','3','4'};

struct{
    int x, y;
}typedef Point;

Point M, Z;


//파이프를 숫자형태로 변경
int pipe_to_int(char c){
    if(c=='|') return 0;
    else if(c=='-') return 1;
    else if(c=='+') return 2;
    else if(c=='1') return 3;
    else if(c=='2') return 4;
    else if(c=='3') return 5;
    else return 6; //c==4
}

int oppo_dir(int d){
    int retDir=0;
    Point hole_dir =  {-dirX[d], -dirY[d]};
    for(; retDir<4; retDir++) if(dirX[retDir]==hole_dir.x && dirY[retDir]==hole_dir.y) break;
    return retDir;
}

char check_hole(Point dot, Point nxt, int dir){
    //nxt 좌표의 형태 검사
    int nxt_pipe_idx = pipe_to_int(board[nxt.x][nxt.y]);
    string nxt_pipe_shape = direction[nxt_pipe_idx];
    
    //점에다가 파이프가 있는 쪽으로 구멍을 뚫어주어야 한다.
    //파이프 기준에서는 dir의 반대방향이다
    //ex. 파이프의 위치가 점 기준 위 -> 점이랑 이어지려면 아래쪽에 뚫려 잇어야 함.
    //so, next파이프의 구멍의 방향을 알려면 opposite

    //이어져 있다면, 1
    if(nxt_pipe_shape[oppo_dir(dir)]=='1') return '1';
    else return '0';
}



void fix_newpipe(Point Erased, string &str, Point p){
    //이미 M or Z에 연결된 파이프가 있는 지 check
    Point cmpr = {-1,-1};
    int dir = -1;
    for(int i=0; i<4; i++){
        int nx = p.x +dirX[i];
        int ny = p.y +dirY[i];
        if(nx<0||nx>R-1||ny<0||ny>C-1) continue;
        if(board[nx][ny]=='.') continue;
        if(direction[pipe_to_int(board[nx][ny])][oppo_dir(i)]=='1'){
            cmpr = {nx,ny};
            break;
        }
    }
    if(cmpr.x==-1 && cmpr.y==-1) return;

    //M or Z에 기존부터 연결되어 있던 파이프가 있으므로, newshape는 M or Z랑 이어진 구멍 지워주기
    for(int i=0; i<4; i++){
        int nx = Erased.x +dirX[i];
        int ny = Erased.y +dirY[i];
        if(str[i]=='0') continue;
        if(nx<0||nx>R-1||ny<0||ny>C-1) continue;
        if(board[nx][ny]!='M' && board[nx][ny]!='Z') continue;
        //newpipe에서 연결된 방향 지우기
        str.replace(i,1,"0");
        break;
    }
}

string make_shape(Point Erased){
    //4개의 방향을 검사해서 이 점이랑 이어진 파이프가 있는 지 확인!!
    //이어지는 파이프가 있다면, 이 점이 어떤 모양의 파이프가 되어야 하는 지 string으로 출력 
    string pipe_shape="";
    for(int i=0; i<4; i++){
        int nx = Erased.x + dirX[i];
        int ny = Erased.y + dirY[i];

        //막다른 벽이거나 점이면 pass -> 0으로 표시
        if(nx <0 || nx >R-1 || ny<0 || ny>C-1 || board[nx][ny]=='.'){
            pipe_shape+="0"; continue;
        }
        //시작점 or 종착지이면 이어져야하니 -> 1로 표시
        if(board[nx][ny]=='Z' || board[nx][ny]=='M'){
            pipe_shape+="1"; continue;
        }

        //파이프가 있다면, 모양 만들어주기.
        //파이프의 모양을 다음 위치의 파이프 모양이랑 비교해서 만들어주기.
        //각 방향에 존재하는 파이프의 모양을 알아야 함. -> check 함수로.. 
        pipe_shape+=check_hole({Erased.x, Erased.y},{nx,ny}, i);
    }


    //M & Z는 출입구가 한개여야 한다.
    //M or Z가 출입구가 한개 이상인지 check
    //만일 한 개 이상이면 newpipe에서 만들어진 것이므로, newpipe에서 삭제시키기
    fix_newpipe(Erased, pipe_shape, M);
    fix_newpipe(Erased, pipe_shape, Z);

    return pipe_shape;
}


Point find_first_pipe(){
    Point retVal = {-1,-1};

    //M에서 시작하는 첫번째 파이프 찾기
    for(int i=0; i<4; i++){
        int nx = M.x+dirX[i];
        int ny = M.y+dirY[i];
        if(nx<0 || nx>R-1 || ny <0 || ny>C-1) continue;
        if(board[nx][ny]=='.') continue; 
        //파이프를 만나면 종료
        retVal = {nx,ny};
        break;
    }

    //시작점에 파이프가 없으면 Z에 있는 끝점부터
    if(retVal.x == -1 && retVal.y ==-1){
       for(int i=0; i<4; i++){
            int nx = Z.x+dirX[i];
            int ny = Z.y+dirY[i];
            if(nx<0 || nx>R-1 || ny <0 || ny>C-1) continue;
            if(board[nx][ny]=='.') continue; 
            //파이프를 만나면 종료
            retVal = {nx,ny};
            break;
        } 
    }
    return retVal;
}


Point bfs(){
    /*  1. 첫번째 파이프부터 이어진 파이프를 따라 진행 -> 가스가 흐를 수 있는 방향이 정해져 있으므로, 길히 한 방향임.
        2. 그러다, 이 파이프 통로랑 이어진 좌표에 점이 있자면 stop!
        3. 그 점을 기준으로 주변에 진행 가능한 방향으로 구멍이 나있는 파이프가 있는 지 check
        4. 그런 파이프가 존재한다면, 이어져야하는데 이어지지 않은 파이프이다.
    */
    
    Point retVal;
    Point first_pipe = find_first_pipe(); //start from M end Z
    queue<Point> q;

    q.push({first_pipe.x, first_pipe.y});
    visited[first_pipe.x][first_pipe.y]=true;
    
    while(!q.empty()){
        Point p = q.front(); q.pop();
        visited[p.x][p.y] = true;

        //이 curr 파이프의 구멍이 나 있는 지점 check
        int pipe_idx = pipe_to_int(board[p.x][p.y]);
        //파이프의 가스관이 뚫린 방향 저장
        string pos = direction[pipe_idx];
    
        for(int i=0; i<4; i++){
            //뚫려있는 방향만 큐에 넣기위해 검사
            if(pos[i]=='0') continue;   

            int nx = p.x + dirX[i];
            int ny = p.y + dirY[i];

            if(nx<0 || nx>R-1 || ny <0 || ny>C-1) continue;
            if(visited[nx][ny]) continue;
            if(board[nx][ny]=='Z' || board[nx][ny]=='M') continue; 

            //파이프 일때만 큐에 push
            if(board[nx][ny]!='.') q.push({nx,ny});
            //만약 점이라면 이 점 주변에 가스관 통로가 있는 지 검사
            else if(board[nx][ny]=='.'){
                retVal = {nx,ny};
                break;  //가스의 흐름이 유일하므로 찾으면 바로 break;
            }
        }
    }
    return retVal;
}

void solve(){

    //1. 지워진 파이프의 위치 좌표 찾기
    Point Erased = bfs(); 
    
    //2. 지워진 파이프의 모양 만들기
    string pipe_shape = make_shape(Erased);

    //3. 지워진 파이프의 좌표, 모양 출력하기
    cout << (Erased.x+1)<< " " << (Erased.y+1)<<" "; //좌표
    for(int i=0; i<7; i++) //모양
        if(direction[i]==pipe_shape){
            cout << pipes[i]<<"\n";
            break;
        }
}


int main(){
    //입력
    cin >> R >> C;
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++){
            cin >> board[i][j];
            if(board[i][j] =='M') M={i,j};
            else if(board[i][j]=='Z') Z={i,j};
        }

    //solve
    solve();
    return 0;
}
