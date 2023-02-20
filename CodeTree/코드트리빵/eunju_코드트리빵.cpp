#include <bits/stdc++.h>

using namespace std;

int N, M;
int board[20][20];
// 0 : 빈칸
// 1: 베이스캠프
// -1 : 통행금지

int dist[20][20];
int dirX[] = {-1,0,0,1};
int dirY[] = {0,-1,1,0};

struct{ int x,y; } typedef Point;
struct{
    int x,y;
    int goalX, goalY;
}typedef Person;

Person ppl[31];

void bfs(Point p){
    //이 편의점에서 가장 가까운 베이스 캠프 찾기
    //최단거리 찾기 전 방문 여부 기록해두기
    //다른사람이 편의점에 도착하기 전에는 p도 지나갈 수 있음
    for(int i=1; i<=N; i++)
        for(int j=1; j<=N; j++)
            dist[i][j] = 0xffffff;

    dist[p.x][p.y] = 0;    
    queue<Point> q;
    q.push(p);
    
    while(!q.empty()){
        Point pp = q.front(); q.pop();
        
        for(int i=0;i<4;i++){
            int nx = pp.x + dirX[i];
            int ny = pp.y + dirY[i];
            if(nx <1 || nx>N || ny<1 || ny>N) continue;
            if(dist[nx][ny] !=0xffffff) continue;
            if(board[nx][ny]==-1) continue;
            dist[nx][ny] = dist[pp.x][pp.y]+1;
            q.push({nx,ny});
        }
    }
}

void move_person(Person &p){
    //편의점에 도착한 사람은 수행X
    if(p.x==p.goalX && p.y==p.goalY)
        return;
    
    //편의점으로부터 모든 격자의 최단거리 미리 계산하기
    bfs({p.goalX, p.goalY});

    //매 움직임 마다 자신과 인접한 네 곳을 보면서, 어디로 갈 지 정하기
    int mindist = 0xffffff, mindir = -1;
    for(int i=0; i<4; i++){
        int nx = p.x+dirX[i];
        int ny = p.y+dirY[i];
        if(nx <1 || nx>N || ny <1 || ny>N) continue;
        if(dist[nx][ny] < mindist){ //편의점부터 그 격자까지 거리가, 내가 알던 거리보다 가까우면 글로간다.
            mindist = dist[nx][ny];
            mindir = i;
        }
    }

    //그 방향으로 한 칸 이동
    p.x += dirX[mindir];
    p.y += dirY[mindir];
}

void checkArrived(Person &p){
    //사람 p가 store에 도착했으면 disabled 시키기
    if(p.x ==p.goalX && p.y==p.goalY)
        board[p.x][p.y] = -1;
}

//사람 p가 어디서 출발할 지 관리 (basecamp)
void find_basecamp(Person &p){
    //store에서 모든 base캠프까지의 최단거리 구하기
    bfs({p.goalX, p.goalY});

    //가장 가까운 베이스 캠프 찾기
    int mindist = 0XFFFFFF;
    Point tmp={0,0};
    //가장 작은쪽 행, 열부터 확인해서 조건 만족
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            //베이스캠프인 곳만 보기
            if(board[i][j]!=1) continue;
            if(dist[i][j] < mindist){
                mindist = dist[i][j];
                tmp = {i,j};
            }
        }
    }

    //선택한 basecamp 위치는 통행불가로 만들어주기
    //tmp.x, tmp.y에서 출발
    p.x = tmp.x, p.y = tmp.y;
    board[p.x][p.y] = -1;
}

bool isFinished(){
    //한사람이라도 도착하지 않은 사람이 있으면 false
    for(int i=1; i<=M; i++)
        if(ppl[i].x!=ppl[i].goalX || ppl[i].y!=ppl[i].goalY) 
            return false;
    return true;
}



void solve(){

    int T=0;
    while(!isFinished()){
        T++;
        //1. 모든 사람이 한 칸 움직인다.
        //T시간 이내 사람만
        for(int i=1; i<T && i<=M ;  i++)
            move_person(ppl[i]);

        //2. 도착한 사람 처리
        for(int i=1; i<T&&i<=M; i++)
            checkArrived(ppl[i]);

        //3. 새로 출발한 사람 관리
        if(T<=M)
            find_basecamp(ppl[T]);
    }
    cout << T;
}


int main() {
    // 여기에 코드를 작성해주세요.
    cin >> N >> M;
    for(int i=1; i<= N; i++){
        for(int j=1; j<=N; j++){
            cin >> board[i][j];
        }
    }

    for(int i=1; i<=M; i++){
        cin >> ppl[i].goalX >> ppl[i].goalY;
    }

    solve();

    return 0;
}
