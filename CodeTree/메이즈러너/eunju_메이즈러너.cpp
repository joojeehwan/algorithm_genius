#include <bits/stdc++.h>

using namespace std;


struct Point{
    int x, y;
};

int N, M, K;    //N : 미로의 크기. M : 참가자 수. K : 게임 시간
int board[11][11];
bool isExit[11];
Point attender[11];
Point out;
int attenderDist=0;   //  모든 참가자들의 이동 거리 합
int dirX[] = {-1, 1, 0, 0}; //상하좌우
int dirY[] = {0, 0, -1, 1};


Point rotateP;
int minRecSize;

int dist(Point a, Point b){
    return (a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y);
}

void moveAttender(){
    //모든 참가자는 1초마다 1칸씩만 움직인다.

    //각 참가자가 진행할 방향
    vector<int> dir(M+1,-1);
    for(int i=1; i<=M; i++){
        // 4방향 중에 출구까지의 최단거리 계산하기 
        vector<int> dirTemp;
        int exitFromHere = dist(attender[i], out);
        for(int d=0; d<4; d++){
            int nx = attender[i].x + dirX[d];
            int ny = attender[i].y + dirY[d];
            
            //0. 미로 벙위를 벗어나면 갈 수 없음
            if(nx < 1 || nx > N || ny <1 || ny > N) continue;
            // 1. 만일 벽이라면 갈 수 없음
            if(board[nx][ny]!=0) continue;
            // 2. dist(현재칸,출구) < dist(다음칸, 출구) 갈 수 없음
            if(exitFromHere < dist({nx,ny},out)) continue;
            dirTemp.push_back(d);
        }

        //참가자가 움직일 수 있는 상황이라면 움직이기(이 조건을 체크안해서 seg.fault 났음)
        if(dirTemp.size()==0) continue;
        //움직일 수 있는 칸이 2개 이상이라면 상하로 움직이는 것을 우선으로
        if(dirTemp.size() > 1) sort(dirTemp.begin(), dirTemp.end());
        dir[i] = dirTemp[0];
    }
    //참가자들이 선택한 진행할 방향으로 한칸씩 움직이기
    for(int i=1; i<=M ; i++){
        if(dir[i] <0) continue;
        if(isExit[i]) continue;
        int direction = dir[i];
        attender[i].x  = attender[i].x + dirX[direction];
        attender[i].y  = attender[i].y + dirY[direction];
        attenderDist+=1;
        if(attender[i].x == out.x && attender[i].y == out.y) isExit[i] = true;
    }
    
}


void makeRectangle(){
    //아래 세가지 조건 중 가장 작은 정사각형 만들기
    //1. 자신
    //2. 다른 참가자들 중에 최소 한명
    //3. 출구

    //각 참가자마다 최소 사각형 구하기
    //모든 사람중에 recSize가 가장 작은 사람이랑 사각형을 만들어본다.

    // 회전 변수 초기화
    rotateP = {N,N};
    minRecSize = N+1;

    for(int i=1; i<=M; i++){
        if(isExit[i]) continue;
        //아무나 한명을 붙잡고 사각형을 만들어본다. 그 중 젤 작은 사각형을 선택한다.
        
        // recSize가 같아도 가장 왼쪽위에 있는 정사각형을 만들어야 하니깐 
        // p1의 값이 더 적은 걸 선택해야한다.
        int recSize = max(abs(attender[i].x-out.x), abs(attender[i].y-out.y));
          if(recSize+1 < minRecSize){
            minRecSize = recSize+1;
            // 사람, 출구가 직선이면 
            // 두 좌표가 주어질 때 둘을 포함하는 가장 작은 정사각형
            // 일직선이면 고려할 case가 하나 더. -> 세로는 가로로, 가로는 세로로 
            // 세로직선이면 왼쪽으로 붙여보고
            // 가로직선이면 위로 붙여본다.
            
            Point tmpP4 = {max(attender[i].x, out.x), max(attender[i].y, out.y)};

            Point tmpP1 = {max(1,tmpP4.x-recSize), max(1,tmpP4.y-recSize)}; //3,1
 
      
            rotateP = tmpP1;
        }
    }   
}

//90도 회전시키기
//회전하기 전 1,1으로 좌표를 옮긴 후 돌려야 함
void rotate(){

    // 1. board 회전
    int tmp[11][11];

    for(int i = 0; i< minRecSize; i++){
        for(int j = 0; j<minRecSize; j++){
            tmp[i][j] = board[rotateP.x+i][rotateP.y+j];
        }
    }   

    // 그 자리에다가 옮겨주기
    for(int i=0; i<minRecSize; i++){
        for(int j=0; j<minRecSize; j++){
            board[j+rotateP.x][minRecSize-i-1+rotateP.y] = max(0,tmp[i][j]-1);   //내구도 1씩 깎을대 음수 방지
        }
    }

    // 2. 사람 회전
    for(int i=1; i<=M; i++){
        if(attender[i].x >=rotateP.x && attender[i].x <=rotateP.x+minRecSize -1
            && attender[i].y >=rotateP.y && attender[i].y<=rotateP.y+minRecSize-1 ){
                if(isExit[i]) continue;
                Point p = {attender[i].x - rotateP.x, attender[i].y - rotateP.y};

                //회전시키기
                attender[i].x = p.y + rotateP.x;
                attender[i].y = minRecSize - p.x -1 + rotateP.y; // 2,1 -> 2,2  / 3,2 -> 3,3
        }
    }

    // 3. exit 회전
    Point p = {out.x - rotateP.x, out.y - rotateP.y};
    out.x = p.y + rotateP.x;
    out.y = minRecSize-p.x -1 + rotateP.y; // 2 - 3
}


void solve(){

    //K초동안 반복
    for(int k=1; k<=K; k++){

        //모든 참가자 움직이기
        moveAttender();


        //사각형 만들기
        makeRectangle();
        
        // cout << "rotateP : " << rotateP.x <<" "<<rotateP.y<< " " << minRecSize<< endl;
        //미로 회전
        rotate();

        // cout <<"\nboard\n"<<endl;
        // for(int i=1; i<=N; i++){
        //     for(int j=1; j<=N; j++){
        //         cout<<board[i][j]<<" ";
        //     }cout <<endl;
        // }
        
        // cout <<"\attender\n"<<endl;
        // for(int i=1; i<=M; i++){
        //     cout << i << " : "<< attender[i].x << " "<<attender[i].y<<endl;
        // }

        // cout <<"attenderDist : "<<attenderDist<<endl;

        // //모든 참가자가 탈출에 성공한지 체크
        // check();
    }

}

int main(){

    cin >> N >> M >> K;

    // 미로의 정보
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            cin >> board[i][j];
        }
    }

    

    // 참가자 정보
    for(int i=1; i<=M; i++){
        cin >> attender[i].x >> attender[i].y;
    }

    // 충구 정보
    cin >> out.x >> out.y;
    
    solve();

    cout <<attenderDist<<endl;
    cout << out.x << " "<<out.y<<endl;

    return 0;
}