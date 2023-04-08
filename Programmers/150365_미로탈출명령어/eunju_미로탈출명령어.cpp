#include <bits/stdc++.h>

using namespace std;

bool finish = false;
string answer = "";
//          d l r u
int dx[] = {1,0,0,-1};  
int dy[] = {0,-1,1,0};

int left_dist(int x1, int y1, int x2, int y2){
    return abs(x1-x2)+abs(y1-y2);
}


void dfs(int left, int x, int y, int n, int m, int r, int c){
    if(left==0){
        finish = true;
    }

    for(int i=0; i<4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx <1 || nx >n || ny <1 || ny >m) continue;

        int diff = left_dist(nx,ny, r, c);
        //갈 수 있는 남은 dist
        //현재 지점 ~도착지점
        //현재지점 -> 도착지점까지 갈 수 있는 거리가 남아 있다면
        if(left >= diff){
            //사전순
            if(i==0) answer.push_back('d');
            else if(i==1) answer.push_back('l');
            else if(i==2) answer.push_back('r');
            else if(i==3) answer.push_back('u');

            dfs(left-1, nx, ny, n, m, r, c);
            if(finish) return;
        }
    }
}

string solution(int n, int m, int x, int y, int r, int c, int k) {
    
    //k : 미로까지 이동해야하는 거리
    //S에서 E까지 갈 수 있는 최단거리
    int dist = abs(r-x) + abs(c-y);
    
    //k-dist
    //남은 거리는 왔다갔다 더미 거리
    if(k-dist < 0 || (k-dist)%2!=0) {
        answer = "impossible";
    }
    else{
        dfs(k, x, y, n, m, r, c);
    }

    return answer;
}

int main (){
    int n, m, x, y, r, c, k;
    n=3;
    m=4;
    x=2;
    y=3;
    r=3;
    c=1;
    k=5;

    cout << solution( n, m, x, y, r, c, k);

}