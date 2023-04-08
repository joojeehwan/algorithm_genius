#include <bits/stdc++.h>

using namespace std;

int N;
int player[51][10];
int order[10];
bool selected[10];  //자리가 이미 찼는 지
int maxScore = -1;

void input(){
    cin >> N;
    for(int i=1; i<=N; i++){
        for(int j=1; j<=9; j++){
            cin >> player[i][j];
        }
    }
}

void forward(bool lu[], int score, int &totalScore){
    //기존 루에 있는 선수 처리
    for(int i=3; i>=1; i--){
        //각 루에 선수가 있을때만 score칸 씩 움직이기
        if(lu[i]==false) continue;

        //3루에 있는 선수가 움직이면 점수 획득
        if(i + score >3)
            totalScore+=1;
        else lu[i+score] = true;

        lu[i] = false;  //빠져나오고
    }

    //타자 처리
    if(score == 4) totalScore+=1;
    else lu[score] = true;
}



//게임을 진행해서 점수 계산
void play(){

    int start_number = 1; //이닝이 변경되더라도, 플레이어 넘버는 변하지 않는다.
    int totalScore = 0;
    bool lu[4];  //각 루에 몇번 선수가 있는 지
    
    //N이닝동안 진행
    for(int n=1; n<=N; n++){

        bool isfinished = false;
        int out = 0; 
        fill(lu, lu+4, false);

        //한 타순이 끝날때까지 계속 play
        while(1){
               //아웃이 3번이면 이닝이 바뀜
            for(int i=start_number; i<=9; i++){
                //선수 출격
                int p = order[i];
                int score = player[n][p];
                
                if(score == 0) out++; // 아웃
                else if(score == 1 || score == 2 || score == 3  || score == 4){    //1루타
                    forward(lu, score, totalScore);
                }

                if(out == 3){
                    start_number = (i+1)%9;
                    isfinished = true;
                    break;
                }
            }
            if(isfinished) break;   //중간에 아웃에의해 턴이 바뀌는 경우라면 start_number가 마지막 선수로 교체
            start_number=1;    //그게아니라, 마지막 선수까지 타자를 다 쳐서 끝난 경우라면 start_number=1
        }
    }
    // maxScore = max(maxScore, totalScore);
    // 점수 계산이 잘못됐다.
    if(maxScore <totalScore){
        maxScore = totalScore;

        // cout <<"*********** ";
        // for(int i=1; i<=9; i++){
        //     cout << order[i]<<" ";
        // }cout <<totalScore<< "***********\n";
    }

}


// void play(){
//     int total_score=0;
//     int batter = 1; //1번 타자부터
//     int out = 0;    //out 횟수

//     for(int n=1; n<=N; n++){
//         out = 0;
//         bool lu[4]; fill(lu, lu+4, false);

//         while(out < 3){
//             int p = order[batter];
//             int score = player[n][p];
//             if(score ==0) out++;
//             else{
//                 for(int i=3; i>=1; i--){
//                     if(!lu[i]) continue;
//                     if(i + score > 3) total_score+=1;
//                     else lu[i+score] = true;
//                     lu[i] = false;
//                 }

//                 if(score == 4) total_score+=1;
//                 else lu[score] = true;
//             }
//             batter = (batter+1)%9;
//         }
//     }
//     maxScore = max(maxScore, total_score);
// }

void dfs(int cnt){
    
    if(cnt > 9){
        //2. 게임 진행해서 점수 확인
        play();
        // for(int i=1; i<=9; i++){
        //     cout << order[i]<<" ";
        // }cout <<"\n";
        return;
    }

    //dfs로 각 선수를 모든 자리에 위치 시키기
    for(int i=1; i<=9; i++){
        if(selected[i]==true) continue;

        selected[i] = true;
        order[i] = cnt;
        dfs(cnt+1);
        selected[i] = false;
    }
}


void solve(){
    //이닝 - 공격, 수비
    //N이닝 진행
    //경기 시작 전 타순 정하기
    //3out -> 공격,수비 change
    // 9번타자까지 치고 3out이 안생기면 다시 1번타자로 돌아온다.
    // 이닝이 변해도 타순은 유지.
    // 공격 : 투수가 던진 공을 타석에 있는 타자가 치는 것 
    //       공격이 1루, 2루, 3루를 거쳐서 홈에 도착하면 1점
    //       

    //1번타자를 4번째로
    //한 이닝이 끝나는 것을 체크ㄴ
    
    //각 이닝마다 모든 겨우의 수 체크
    //순서를 만들 때 1번타자의 위치는 4번 위치로 지정
    //4번타자는 1번 선수이다.
    order[4] = 1;
    selected[4] = true;
    //1. 타순 만들기
    //2번 선수부터 위치 시키기
    dfs(2);

    cout<<maxScore<<"\n";
    
}

int main(){

    input();
    solve();
    
    return 0;
}