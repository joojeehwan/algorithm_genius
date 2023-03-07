#include <bits/stdc++.h>

using namespace std;

int N, M, H, K;
int board[100][100];

//위 오른쪽 아래 왼쪽 - 시계방향
int dirX[] = {-1,0,1,0};
int dirY[] = {0,1,0,-1};

//1,1,2,2,3,3,4,4
//masterCurrCnt로 지나온 칸을 count 하면서 
//masterTargetLen 1번 만족 시키면 masterArrowCnt 1증가
//masterArrowCnt가 2가 되면 masterTargetLen 1증가하게
int masterTargetLen = 1;
int mCurrCnt = 0;

//선분
int masterArrowCnt= 0;

//큰 나선을 그리는 선 
bool masterClockWise = true;  

//좌우 - 우, 상하 - 하
struct Point{
    int x;
    int y;
};

struct Info{
    Point p;
    int curDir;
};

Info master;   //술래
vector<Info> runner;  //M
bool tree[100][100];    //H


bool dist_check(Point x, Point target){
    int dist = abs(x.x -  target.x) + abs(x.y - target.y);
    // cout <<x.x<< ", "<<x.y <<" : "<<dist <<"<3\n";
    if(dist <=3) return true;
    return false;
}

bool master_exist(Point x, Point target){
    if(x.x == target.x && x.y ==target.y) return true;
    return false;
}

void RunnerMove(){
    for(int i=0; i<M; i++){
        //술래와의 거리가 3이하인 도망자만 move

        if(dist_check(runner[i].p, master.p)==false) continue;
        
        int x = runner[i].p.x;
        int y = runner[i].p.y;
        // cout<< "술래와 거리가 3이하인 도망자 pos : "<< x <<", "<<y<<"\n";
        
        int nx = x + dirX[runner[i].curDir];
        int ny = y + dirY[runner[i].curDir];

        //현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나는 경우
        if(nx <0 || nx>N-1 || ny <0 || ny>N-1){
            // 방향을 반대로 틀어주기
            runner[i].curDir^=2;
            // 술래가 없다면 1칸 움직이기
            nx = x + dirX[runner[i].curDir];
            ny = y + dirY[runner[i].curDir];

            if(master_exist({nx, ny},master.p)) continue;
            runner[i].p = {nx,ny};
            
        }
        //현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나지 않는 경우
        else{
            //술래가 있다면 not move
            if(master_exist({nx, ny},master.p)) continue;
            //술래가 없다면 이동
            runner[i].p = {nx,ny};
        }
    }

    // cout <<"\n도망자 update\n";
    // for(int i=0; i<M; i++){
    //     cout <<runner[i].p.x <<" "<<runner[i].p.y<<"), d : "<<runner[i].curDir<<"\n";
    // }
}

void MasterMove(){
    int x = master.p.x;
    int y = master.p.y;
    int d = master.curDir;

    int nx = x + dirX[d];
    int ny = y + dirY[d];
    
    // 매 턴마다 1칸씩 움직임
    mCurrCnt+=1;

    //목표 칸 개수에 도달하면 칸 개수 늘리기
    if(mCurrCnt == masterTargetLen){
 
        mCurrCnt = 0;   //지나온 거리를 0으로
        masterArrowCnt+=1;  //화살표 하나 완료햇으니 증가

        //달팽이방향이 정방향 이면
        if(masterClockWise){
            //위, 오른쪽, 아래 왼쪽 시계방향으로 무한 움직이기
            if(d == 3) d = 0;
            else d +=1;
        }
        //역방향이면
        else{
            //반시계로 돌리기
            if(d == 0) d=3;
            else d-=1;
        }

        //1 2 2 3 3 4 4 2번씩 반복할려고
        //2개까지 했으면 다시 2개카운트 할려고
        if(masterArrowCnt == 2){
            masterArrowCnt = 0;

            //반시계방향이면 
            if(!masterClockWise)    
                masterTargetLen--;  // 목표 칸 개수 1씩 줄이가
            //시계방향
            else    
                masterTargetLen++;  // 목표 칸 개수 1씩 늘리기
        }
    }

    //이동후의 위치가 방향을 틀어줘야하는 지점
    //case 1. (1,1)
    if(nx == 0 && ny == 0){
        masterClockWise = false;    //달팽이 방향 - 역방향으로
        masterTargetLen = N-1;  //지나가야하는 정해진 길이
        d = 2;      //다시 아래 방향으로 진행하도록 초기화
        masterArrowCnt = -1;
        mCurrCnt = 0;  //지나온 거리 세는걸 0부터 다시 세기
    }
    //case 2. 가운데 (N/2,N/2) 지점
    if(nx == N/2 && ny ==N/2){
        masterClockWise = true;   //달팽이 방향 - 정방향으로
        masterTargetLen = 1;       //지나가야하는 정해진 길이 초기화
        d = 0;  //다시 위 방향 부터
        masterArrowCnt = 0; //선분개수 0개부터 세기
        mCurrCnt = 0;  //지나온 거리 세는걸 0부터 다시 세기
    }

    
    //술래의 위치 업데이트
    master = {nx, ny, d};  
}

int catchRunner(){
    int x = master.p.x;
    int y = master.p.y;
    int d = master.curDir;
    // cout<< "master pos : "<< x <<", "<<y<<"\n";
    
    //잡은 도망자 수
    int cnt =0;

    //격자 크기에 상관없이 술래의 시야는 항상 3칸
    //3칸이내의 러너 잡기
    for(int i=0;i<3;i++){
        int nx = x+dirX[d]*i;
        int ny = y+dirY[d]*i;

        //나무가 있으면 러너 안잡는다.
        if(tree[nx][ny])   continue;
        if(nx <0 || ny <0 || nx > N-1 || ny > N-1)   continue;

        // cout<<"pass : "<< nx <<" , "<<ny<<" dir : " <<d<<endl;
        //검사하려는 칸에 러너가 있으면 잡기, 비워주기
        // vector<Info> tmp_runner;
        // for(int i=0; i<runner.size(); i++)
        //     tmp_runner.push_back(runner[i]);

        vector<int> remove_index;
        for(int i=0; i<M; i++){
            if(runner[i].p.x == nx && runner[i].p.y==ny){
                cnt+=1;
                // cout <<"remove runner : (" << runner[i].p.x <<" "<<runner[i].p.y<<"), d : "<<runner[i].curDir<<"\n\n";
                // runner.erase(runner.begin() + i);   //그 러너 없애기
                // M-=1;   //도망자 수 하나 줄이기
                //그 러너 없애기
                remove_index.push_back(i);
            }
        }
        //remove_runner
        for(int  i=remove_index.size()-1; i>=0; i--){
            int idx = remove_index[i];
            runner.erase(runner.begin() + idx);
        }
        M-=remove_index.size();
        // runner.clear();
        // for(int i=0; i<tmp_runner.size(); i++)
        //     runner.push_back(tmp_runner[i]);

    }
    return cnt;
}

void solve(){
    int score = 0;
    for(int i=1;i<=K;i++){
        //도망자 move
        RunnerMove();
        //술래 move
        MasterMove();
        //점수
        score += i*catchRunner();

        // cout <<"\n도망자\n";
        // for(int i=0; i<M; i++){
        //     cout <<runner[i].p.x <<" "<<runner[i].p.y<<"), d : "<<runner[i].curDir<<"\n";
        // }
    }
    cout<<score<<"\n";
}


int main(){
    
    //board[N*N], 도망자 M명, H개 나무, K번 반복
    cin >> N >> M >> H >> K;
    // cout<<"\n";
    for(int i=0; i<M; i++){
        int x, y, d; cin >> x >> y >> d;
        runner.push_back({{x-1, y-1},d});
        // cout <<"[runner input]\n";
        // cout <<runner[i].p.x <<" "<<runner[i].p.y<<"), d : "<<runner[i].curDir<<"\n";
        //d => 1: 좌우(우), 2: 상하(하)
    }
    // cout<<"\n";

    for(int i=0; i<H; i++){
        int x, y; cin >> x >> y;
        tree[x-1][y-1] = true;
        // cout <<"[tree input["<< i<<"]]\n";
        // cout <<"("<<x-1<<", "<<y-1<<"), bool : "<<tree[x-1][y-1]<<"";
    }
    // cout<<"\n";
    // cout<<"\n";

    //d : 위부터 시작
    master = {{(N-1)/2,(N-1)/2},0};

    solve();
    
    return 0;
}