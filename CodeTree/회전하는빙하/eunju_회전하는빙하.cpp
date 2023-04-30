#include <bits/stdc++.h>

using namespace std;

int n, q;
int N;
int board[66][66];
int rotate_level[1002];

int dirX[] = {-1, 0, 1, 0};
int dirY[] = {0, -1, 0, 1};

int dirXY[][2] = {{1,0}, {1,1}, {0,1}};

void input(){
    cin >> n >> q;
    N = pow(2,n);

    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            cin >> board[i][j];
        }
    }

    //회전 레벨
    for(int i=0; i<q; i++)
        cin >> rotate_level[i];
}

// N/2/2
void clockwise(int x, int y, int size){
    // 그 범위의 시작위치를 옮겨준다고 생각하면 된다.
    // 시작 위치를 시계방향으로 옮겨준다.
    
    //1. 옮길 범위 복사
    //기준 size의 4/1인 왼쪽 위 배열만 잠시 복사해둘 곳
    int tmp[size/2][size/2];
    for(int i=x; i<x+size/2; i++)
        for(int j=y; j<y+size/2; j++)
            tmp[i-x][j-y] = board[i][j];

    //옮겨야하는 시작점의 좌표 4개 저장(왼쪽아래, 오른쪽 아래, 오른쪽 위, 왼쪽 위 순서로 저장)
    //10을 위로 옮기고 20을 왼쪽으로 옮기고 15를 아래로 옮기고 미리 저장해둔 32를 오른쪽으로 옮겨야 함.
    vector<pair<int,int>> point;
    for(int i=0; i<3; i++) //10, 20, 15 순으로 저장
        point.push_back({x+dirXY[i][0]*(size/2), y+dirXY[i][1]*(size/2)});

    for(int k=0; k<point.size(); k++){
        int xx = point[k].first, yy = point[k].second;

        for(int i=xx; i<xx+size/2; i++)
            for(int j=yy; j<yy+size/2; j++)
                board[i+dirX[k]*(size/2)][j+dirY[k]*(size/2)] = board[i][j];
            
    }

    //오른쪽으로 한 블럭 옮기기 
    for(int i=x; i<x+size/2; i++){
        for(int j=y; j<y+size/2; j++){
            board[i][j+size/2] = tmp[i-x][j-y];
        }
    }
}

// N/2
void rotateIceburg(int rotate_level){
    // cout <<"rotate level : " << rotate_level<<endl;
    int range = pow(2,rotate_level);

    for(int i=1; i<=N; i+=range)
        for(int j=1; j<=N; j+=range)
            //시계방향으로 돌려주기 // cout <<"(" <<i<<", "<<j << ") ";
            clockwise(i,j,range);
        
    
}

void meltIceburg(int rotate_level){
    vector<pair<int,int>> melt;

    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            int cnt = 0;
            for(int d=0; d<4; d++){
                int nx = i + dirX[d];
                int ny = j + dirY[d];

                if(nx < 1 || nx > N || ny < 1 || ny >N) continue;
                if(board[nx][ny]<=0) continue;
                cnt +=1;
            }
            if(cnt <3) melt.push_back({i,j});
        }
    }
    for(auto m : melt){
        board[m.first][m.second] -=1;
    }
}

bool visited[66][66];

int bfs(int x, int y){

    int area=1;
    queue<pair<int,int>> q;
    q.push({x, y});
    visited[x][y] = true;

    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i=0; i<4; i++){
            int nx = x + dirX[i];
            int ny = y + dirY[i];

            if(nx < 1 || nx > N || ny < 1 || ny >N) continue;
            if(visited[nx][ny]) continue;
            if(board[nx][ny] <=0) continue;

            visited[nx][ny]= true;
            area+=1;    
            q.push({nx,ny});
        }
    }

    return area;
}

int bigggestIceBurg(){

    int maxArea = 0;
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(board[i][j] > 0){
                maxArea = max(maxArea,bfs(i,j));
            }
        }
    }
    
    return maxArea;
}

int totalIceBurg(){
    int sum =0;
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(board[i][j] > 0){
                sum+=board[i][j];
            }
        }
    }
    return sum;
}

void solve(){
    for(int i=0; i<q; i++){
        //회전
        rotateIceburg(rotate_level[i]);
        //얼음 녹이기
        meltIceburg(rotate_level[i]);
    }

    // for(int i=1; i<=N; i++){
    //     for(int j=1; j<=N; j++){
    //         cout << board[i][j]<<"\t";
    //     }cout <<endl;
    // }

    //빙하의 총 양
    cout << totalIceBurg()<<endl;
    //가장 큰 얼음 군집
    cout << bigggestIceBurg()<<endl;
    

    
    
}

int main(){

    input();

    solve();

    return 0;
}