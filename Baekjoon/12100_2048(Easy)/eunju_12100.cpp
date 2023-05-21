#include <bits/stdc++.h>

using namespace std;

// 0은 빈 칸
int board[20][20];
int N;

//4방향으로 다 밀어보기
int move_block(int cnt){
    if(cnt == 5){
        int maxNum = 0;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                maxNum = max(board[i][j],maxNum);
            }
        }
        return maxNum;
    }

    int resultMax = 0;
    //0 : 위 1 : 오른쪽 2: 아래 3 : 왼쪽
    for(int direction=0; direction<4; direction++){

        int tmp[20][20];
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                tmp[i][j] = board[i][j];
            }
        }
        
        for(int i=0; i<N; i++){

            vector<int> notzero;
            //위 or 아래 
            if(direction == 0 || direction == 2){
                //세로 값들을 담아서
                for(int j=0; j<N; j++)
                    if(board[j][i] != 0)
                        notzero.push_back(board[j][i]);
                
            }
            //오른쪽, 왼쪽
            else{
                for(int j=0; j<N; j++)
                    if(board[i][j] != 0)
                        notzero.push_back(board[i][j]);
            }
            // 왼쪽
            // 2 0 2 4 4 4 0 2
            // 2 2 4 4 4 2 0 0 
            // 4 8 4 2 0 0 0 0 
            
            // 2 2 4 4 4 2

            // 2 4 4 4 2 2 
            // 2 4


            // 오른쪽
            // 2 0 2 4 4 4 0 2
            // 0 0 2 2 4 4 4 2 
            // 0 0 0 0 4 4 8 2
            if(direction == 1 || direction == 2){
                reverse(notzero.begin(), notzero.end());
            }

            // 다음숫자랑 같으면 합치고 그 다음 숫자를 다음 숫자랑 비교
            vector<int> calculated; // 2 8 4 2
            for(int k=0; k<notzero.size(); k++){
                if(notzero[k] == notzero[k+1] && k+1<notzero.size()){
                    calculated.push_back(notzero[k]*2);
                    k++;
                }
                else{
                    calculated.push_back(notzero[k]);
                }
            }

            //남은 부분은 0으로 채워주기
            for(int k=calculated.size(); k<N; k++){
                calculated.push_back(0);
            }


            if(direction == 1 || direction == 2)
                reverse(calculated.begin(), calculated.end());
            
        
            //갱신된 배열로 board의 세로 값을 갱신
            for(int j=0; j<calculated.size(); j++){
                if(direction == 0 || direction == 2){
                    board[j][i] = calculated[j];
                }
                else{
                    board[i][j] = calculated[j];
                }
            }
        }

       int returnMax =  move_block(cnt+1);
       if(returnMax > resultMax) resultMax = returnMax;


        //board원복시켜주기
        for(int k=0; k<N; k++){
            for(int l=0; l<N; l++){
                board[k][l] = tmp[k][l];
            }
        }
    }

    return resultMax;
}

//최대 5번 이동시켜서 가장 큰 값 만들기
void solve(){
    cout << move_block(0);
}

int main(){

    cin >> N;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin >> board[i][j];
        }
    }

    solve();

    return 0;
}