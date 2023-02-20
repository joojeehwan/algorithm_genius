#include <bits/stdc++.h>

using namespace std;

int n; //격자의 크기
int m; // 박멸이 진행되는 년 수
int K; // 제초제의 확산 범위
int c; //제초제가 남아있는 년 수
int board[21][21];
int herbicide[21][21];
int total_die = 0;

int dirX[] = {0, -1, -1,-1, 0, 1, 1, 1};
int dirY[] = {-1,-1, 0,  1, 1, 1, 0, -1};

struct{
    int cnt;
    int x; int y;
}typedef Tree;

void input(){
    cin >> n >> m >> K >> c;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> board[i][j];
        }
    }
}

void growth_tree(){
    int add_num[20][20];
    fill(&add_num[0][0], &add_num[19][20], 0);

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(board[i][j] <=0) continue;   //나무가 있으면
            
            //주변 나무 개수 check
            int cnt = 0;
            for(int k=0; k<8; k+=2){
                int nx = i+dirX[k];
                int ny = j+dirY[k];

                if(nx<0 || nx>n-1 || ny<0 || ny>n-1) continue;
                if(board[nx][ny]<=0) continue;

                cnt+=1;
            }
            add_num[i][j] = cnt;
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            board[i][j]+=add_num[i][j];
        }
    }
}

void spread_tree(){
    int add_num[20][20];
    fill(&add_num[0][0], &add_num[19][20], 0);

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(board[i][j] <=0) continue;   //나무가 있으면
            
            //주변 번식 가능한 칸 개수 check
            int cnt = 0;
            for(int k=0; k<8; k+=2){
                int nx = i+dirX[k];
                int ny = j+dirY[k];

                if(nx<0 || nx>n-1 || ny<0 || ny>n-1) continue;
                if(board[nx][ny]!=0) continue;
                if(herbicide[nx][ny]!=0) continue;

                cnt+=1;
            }

            //주변 나무에다 (curr칸 나무개수/빈칸) 나무심기
            for(int k=0; k<8; k+=2){
                int nx = i+dirX[k];
                int ny = j+dirY[k];

                if(nx<0 || nx>n-1 || ny<0 || ny>n-1) continue;
                if(board[nx][ny]!=0) continue;
                if(herbicide[nx][ny]!=0) continue;

                add_num[nx][ny] +=board[i][j]/cnt;
            }
        }
    }

    //번식
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            board[i][j]+=add_num[i][j];
        }
    }
}

bool cmp(Tree a, Tree b){
    if(a.cnt >b.cnt) return true;
    else if(a.cnt < b.cnt) return false;
    // 박멸하는 나무의 수가 같을 때
    else if(a.cnt == b.cnt){
        //행이 작은걸 먼저
        if(a.x < b.x) return true;
        else if(a.x > b.x) return false;
        else if(a.x == b.x){    //행까지 같으면, 열이 작은거
            if(a.y<b.y) return true;
            return false;
        }
    }
}

void delete_tree(){
    vector<Tree> die;
    
    //제초제를 뿌릴 나무 pick
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(board[i][j]<=0) continue;    //나무가 있는 공간만
            int tree_cnt = board[i][j];
            //대각선에
            for(int l=1; l<8; l+=2){
                //제초제의 확산 범위
                for(int k=1; k<=K; k++){
                    int nx = i + dirX[l]*k;
                    int ny = j + dirY[l]*k;
                    if(nx<0 || nx>n-1 || ny<0 || ny>n-1) break;
                    if(board[nx][ny]<=0) break; // 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다. 
                
                    tree_cnt+=board[nx][ny];
                }
            }
            if(tree_cnt > 0) die.push_back({tree_cnt, i, j});
        }
    }

    if(die.size()==0) return;
    sort(die.begin(), die.end(), cmp);
    //제초제를 뿌린 공간의 대각선 모두 박멸
    total_die += die[0].cnt;
    int x = die[0].x; int y = die[0].y;

    //나무가 있다면 
    if(board[x][y] > 0){
        board[x][y] = 0;
        herbicide[x][y] = c;    //제초제 뿌리기

        for(int l=1; l<8; l+=2){
            for(int k=1; k<=K; k++){
                int nx = x + dirX[l]*k;
                int ny = y + dirY[l]*k;

                //박멸 범위 중지
                if(nx < 0 || ny<0 || nx >n-1 || ny >n-1) break;
                if(board[nx][ny]<0) break; 

                herbicide[nx][ny] = c;

                if(board[nx][ny] == 0) break;
                else board[nx][ny] = 0; //나무 박멸
            }
        }
    }
    
}

//c년만큼 제초제 존재
void delete_herb(){
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(herbicide[i][j] == 0) continue;
            herbicide[i][j] -=1;
        }
    }
}

int main(){
    //1. 나무 성장 - 상하좌우 중 나무가 있는 칸 수만큼 성장
    //2. 번식 - 모든 나무에서
    //각 칸의 나무 수 / 총 번식이 가능한 칸 
    //3. 제초제
    // c년 만큼 제초제 유지

    input();

    for(int i=0; i<m; i++){
        growth_tree();  //나무 성장
        spread_tree();  //나무 번식
        delete_herb();  //매 턴마다 제초제 지우기
        delete_tree();  //나무 박멸하기
    }

    cout <<total_die<<"\n";

    return 0;
}