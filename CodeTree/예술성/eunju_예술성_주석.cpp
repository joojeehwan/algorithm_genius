#include <bits/stdc++.h>

using namespace std;

int N;
int board[30][30];
int group[900][900]={0,};
int groupSize[900];
int groupMapping[900];  //groupMappint[1] = 4 : 1그룹의 숫자는 4이다.
int groupCnt;


bool visited[30][30];
int dirX[] = {-1,0,1,0};
int dirY[] = {0,1,0,-1};
struct Point{
    int x, y;
};

int edge[900][900] = {0,};  //edge[1][2] = 3 : 1그룹에 2와 맞닿은 변이 3개이다.

void input(){
    cin >> N;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin >> board[i][j];
        }
    }
}


//그룹나누기
void bfs(Point p, int Num, int g){
    queue<Point> q;
    q.push({p.x,p.y});
    visited[p.x][p.y] = true;
    group[p.x][p.y] = g;
    groupMapping[g] = Num;

    while(!q.empty()){
        Point p = q.front();
        q.pop();

        groupSize[group[p.x][p.y]]+=1;

        for(int i=0; i<4; i++){
            int nx = p.x + dirX[i];
            int ny = p.y + dirY[i];

            if(nx < 0 || nx > N-1 || ny <0 || ny > N-1) continue;
            if(visited[nx][ny]) continue;
            if(board[nx][ny]!=Num) continue;

            visited[nx][ny] = true;
            q.push({nx,ny});
            group[nx][ny] = g;
        }
    }
}

void edgeCount(){
    memset(edge, 0, sizeof(edge));
    //그룹 전체를 돌면서 curr 현재와 다른 변을 만나면 cnt++
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            
            //기준 그룹 코드
            int curr = group[i][j];
            // 오른쪽, 아래만 보면서 다른 
            for(int d=1; d<=2; d++){
                int nx = i + dirX[d];
                int ny = j + dirY[d];

                if(nx < 0 || nx > N-1 || ny <0 || ny > N-1) continue;
                if(group[nx][ny] == curr) continue; //현재 기준이 되는 그룹코드랑 같은 코드면 맞닿은 변이 아니다. 같은칸.

                edge[curr][group[nx][ny]] +=1;
            }
            
        }
    }
}

void rotate_square(int x, int y){
    int len = (N-1)/2;
    int tmp[30][30] = {0,};
    //1 2 
    //3 4

    //3 1 x좌표 
    //4 2
    for(int i=0;i<len;i++){
        for(int j=0;j<len;j++){
            tmp[j][len-1-i] = board[x+i][y+j];  //가로를 세로로 -> 밖에서부터 board값을 읽어와서 tmp에 저장
        }
    }
    
    //board에 복사
    for(int i=0;i<len;i++){
        for(int j=0;j<len;j++){
            board[x+i][y+j]=tmp[i][j];
        }
    }

}

void rotate(){
    //중심을 기준으로 가장자리까지 
    //N은 반드시 홀수이므로
    int len = (N-1)/2 + 1;
    rotate_square(0,0);
    rotate_square(0,(N-1)/2+1);
    rotate_square((N-1)/2+1,0);
    rotate_square((N-1)/2+1,(N-1)/2+1);


    //십자가 반시계 회전
    int tmp[30]={0,};
    len-=1;   //십자가 반개 길이

    //위 값 미리 저장 - 위쪽께 덮어씌워지게 구현
    for(int i=0;i<len;i++)  
        tmp[i] = board[i][len];
    //위 자리에 오른쪽 십자가 값 복사
    for(int i=0;i<len;i++)  
        board[i][len] = board[len][N-1-i];
    //오른쪽 자리에 아래쪽 십자가 값 복사
    for(int i=0;i<len;i++)  
        board[len][N-1-i]= board[N-1-i][len];
    //아래쪽 자리에 왼쪽 십자가 값 복사
    for(int i=0;i<len;i++)  
        board[N-1-i][len]=board[len][i];
    //왼쪽 자리에 미리 저장 해뒀던 위쪽값 복사
    for(int i=0;i<len;i++)  
        board[len][i]=tmp[i];
}

int calcScore(){
    
    // fill(&group[0][0], &group[N-1][N], 0);
    memset(group, 0, sizeof(group));
    memset(visited, false, sizeof(visited));

    //1. 그룹나누기
    groupCnt=1;
    // fill(&groupSize[0], &groupSize[30], 0);
    // fill(&groupMapping[0], &groupMapping[30], 0);
     memset(groupSize, 0, sizeof(groupSize));
      memset(groupMapping, 0, sizeof(groupMapping));
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(!visited[i][j])
                bfs({i,j}, board[i][j], groupCnt++);
        }
    }
    groupCnt-=1; 


    // for(int i=0; i<N; i++){
    //     for(int j=0; j<N; j++){
    //         cout << group[i][j] <<" ";
    //     }cout<<endl;
    // }
    

    //2. 각 그룹의 테두리와 맞닿은 그룹간의 공유 변 개수 세기
    edgeCount();

    //3. 전체 조화로움 계산
    int retVal = 0;
    for(int i=1; i<=groupCnt-1; i++){     
        for(int j=i+1; j<=groupCnt; j++){
            //(a칸수 + b칸 수) * a숫자 * b숫자 * a,b변갯수 
            retVal += (groupSize[i] + groupSize[j]) * groupMapping[i] *groupMapping[j] * (edge[i][j]+edge[j][i]);
            // cout<< i << "-"<<j<<" : " <<groupSize[i] <<" "<< groupSize[j] <<" "<< groupMapping[i] <<" "<< groupMapping[j] <<" "<< (edge[i][j])<<" "<<(edge[j][i]) 
            // <<" ->" << (groupSize[i] + groupSize[j]) * groupMapping[i] *groupMapping[j] * (edge[i][j]+edge[j][i])<<endl;
        }
    }
    // cout<<"retVal : "<<retVal<<endl;
    return retVal;
}

void solve(){
    int harmony=0;
    
    harmony += calcScore();   //초기예술점수
    // cout <<harmony<<endl;

    //4. 회전
    for(int i=0; i<3; i++){
        rotate();

        // for(int i=0; i<N; i++){
        //     for(int j=0; j<N; j++){
        //         cout << board[i][j] <<" ";
        //     }cout<<endl;
        // }
        // cout <<"--"<<endl;

        harmony += calcScore();   //초기예술점수

        

        // cout <<harmony<<endl;
        
    }

    

    cout <<harmony<<endl;
}


int main(){

    input();
    solve();

    return 0;
}