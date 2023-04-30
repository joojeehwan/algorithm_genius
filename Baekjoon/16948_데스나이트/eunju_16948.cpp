#include <bits/stdc++.h>

using namespace std;

struct Point{
    int x, y;
};


int N; 
int dirX[] = {-2,-2,0,0,2,2};
int dirY[] = {-1,1,-2,2,-1,1};
bool visited[200][200];
int dist[200][200];

void bfs(Point p1){

    queue<Point> q;
    q.push(p1);

    dist[p1.x][p1.y] = 0;
    visited[p1.x][p1.y] = true;

    while(!q.empty()){
        Point p = q.front();
        q.pop();
         
        for(int i=0; i<6; i++){
            int nx = p.x + dirX[i];
            int ny = p.y + dirY[i];

            if(nx < 0 || nx > N-1 || ny < 0 || ny > N-1) continue;
            if(visited[nx][ny]) continue;

            visited[nx][ny] = true;
            dist[nx][ny] = dist[p.x][p.y] + 1;
            q.push({nx,ny});
        }

    }
}


// (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1) 
int main(){

    Point p1, p2;

    cin >> N;
    cin >> p1.x >> p1.y >> p2.x >> p2.y;
    
    bfs(p1);

    if(dist[p2.x][p2.y] == 0) cout << -1<<"\n";
    else cout << dist[p2.x][p2.y] << "\n";

    return 0;
}