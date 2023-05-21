#include <bits/stdc++.h>

using namespace std;

int N, M;   // n ≤ 25

//0(오른쪽) 1(아래) 2(왼쪽) 3(위)
int direction = 0;  //첨엔 오른쪽
int dirX[] = {0, 1, 0, -1};
int dirY[] = {1, 0, -1, 0};

int board[25][25];


void round(){

}

void input(){
    cin >> N >> M;
    for(int i=0; i<N; i++)
        for(int j=0; j<N; j++){
        cin >> board[i][j];
    }   

    for(int i=0; i<M; i++){
        int d, p; cin >> d >> p;
        //round(d, p);
    }
}

int main(){

    input();

    return 0;
}