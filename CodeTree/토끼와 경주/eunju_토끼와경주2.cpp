#include <bits/stdc++.h>

using namespace std;

struct Rabbit{
    int pidi;    // 토끼 고유번호
    int count=0;  // 현재까지 총 점프 횟수
    int x=0, y=0;   //토끼의 최초 시작 점 0,0
};

map<int,int> rabbitIndex; // 토끼 고유번호 -> index
int distL[2000]; // 이동해야하는 거리
long long score[2000];
Rabbit rabbit[2000];
bool checkRabbit[2000]; //각 토끼가 이번 턴에서 선택 됐었는 지 여부

int dirX[] = {-1, 0, 1, 0};
int dirY[] = {0, 1, 0, -1};

int N, M;   // N*M의 격자
int P;  // P마리의 토끼
int K, S;   //K 번의 턴동안 멀리 보내주기, 가장 우선순위 높은 토끼에게 S더해주기
int pid_T, L;   //pid_T인 토끼 이동거리 L배 해주기


/**
 * 우선순위가 높은 토끼를 뽑아 멀리보내주는 작업 K번 반복
 * 1. 현재까지의 총 점프 횟수가 적은 토끼
 * 2. 현재 서있는 행 번호 + 열 번호가 작은 토끼
 * 3. 행 번호가 작은 토끼
 * 4. 열 번호가 작은 토끼
 * 5. 고유번호가 작은 토끼
*/
struct compare1{
    bool operator()(const Rabbit& r1, const Rabbit& r2){
        //pq는 반대이다. true이면 위치를 바꿔준다.
        if(r1.count == r2.count){
            if(r1.x+r1.y == r2.x+r2.y){
                if(r1.x == r2.x){
                    if(r1.y == r2.y){
                        return r1.pidi > r2.pidi;
                    }
                    return r1.y > r2.y;
                }
                return r1.x > r2.x; 
            }
            return r1.x+r1.y > r2.x+r2.y;
        }
        return r1.count > r2.count;
    }
};

/*
 * 1. 행 번호 + 열 번호가 큰 칸
 * 2. 행 번호가 큰 칸
 * 3. 열 번호가 큰 칸
*/
struct compare2{
    bool operator()(const pair<int,int>& p1, const pair<int,int>& p2){
        if(p1.first+p1.second == p2.first+p2.second){
            if(p1.first == p2.first){
                return p1.second < p2.second;
            }
            return p1.first < p2.first;
        }
        return p1.first+p1.second < p2.first+p2.second;
    }
};

/*
 * 1. 현재 서있는 행 번호 + 열 번호가 큰 토끼
 * 2. 행 번호가 큰 토끼
 * 3. 열 번호가 큰 토끼
 * 4. 고유번호가 큰 토끼
*/
struct compare3{
    bool operator()(const Rabbit& r1, const Rabbit& r2){
        if(r1.x+r1.y == r2.x+r2.y){
            if(r1.x == r2.x){
                if(r1.y == r2.y){
                    return r1.pidi < r2.pidi;
                }
                return r1.y < r2.y;
            }
            return r1.x <r2.x;
        }
        return r1.x+r1.y < r2.x+r2.y;
    }
};

priority_queue<Rabbit, vector<Rabbit>, compare1> pq;
priority_queue<pair<int,int>, vector<pair<int,int>>, compare2> pos;
priority_queue<Rabbit, vector<Rabbit>, compare3> afterKturn;

void double_L_distance(){
    distL[rabbitIndex[pid_T]]*=L;
}

void race(){
    //1. 우선순위가 가장 높은 토끼를 결정
    //   각 레이스마다 K번의 턴이 모두 진행된 직후에 우선순위가 높은 토끼를 골라야해서
    Rabbit selectedRabbit = pq.top(); pq.pop();
    int selectedIndex = rabbitIndex[selectedRabbit.pidi];
    checkRabbit[selectedIndex] = true;
    //2. 토끼가 상하좌우 이동했을 때 4방향 위치 구하기
    pos = priority_queue<pair<int,int>, vector<pair<int,int>>, compare2>(); //초기화
    //주어진 electedRabbit.d 5칸을 다 이동 해야 함.
    // cout << "mopve pidi : "<< selectedRabbit.pidi <<" "<<selectedRabbit.count<<endl;
    for(int d=0; d<4; d++){
        //주어진 electedRabbit.d 5번을 다 이동 해야 함.
        int nx = selectedRabbit.x, ny=selectedRabbit.y;
        int ndir = d;
        for(int nd=0; nd < distL[selectedIndex] ; nd++){
            nx += dirX[ndir];
            ny += dirY[ndir];
            
            //두 좌표 중 한곳이라도 그리드를 넘어간다면 교정해주기
            
            if(nx <0 || nx > N-1 || ny < 0 || ny > M-1){
                ndir^=2;
                //벽까지 이동한 후 반대로 한 칸 이동해야한다. nx = selectedRabbit.x + dirX[newdir];
                if(nx <0 || nx > N-1){
                    nx = nx > N-1 ? N-1 : 0;
                    nx = nx + dirX[ndir];
                }
                if(ny < 0 || ny > M-1){
                    ny = ny > M-1 ? M-1 : 0;
                    ny = ny + dirY[ndir];
                }
            }

            // cout << "{"<< nx<<", "<<ny<<"} ";
        }
        pos.push({nx,ny});
        // cout << "=> {"<< nx<<", "<<ny<<"} // ";
    }//cout<<endl;

    
    //3. 우선순위가 높은 칸으로 토끼 좌표 변경시키기
    selectedRabbit.x = pos.top().first;
    selectedRabbit.y = pos.top().second;
    selectedRabbit.count +=1;
    pos.pop();

    rabbit[selectedIndex] = selectedRabbit;
    pq.push(selectedRabbit);

    //4. 나머지 토끼들 점수 누적하기
     for(int i=0; i<P; i++){
        if(i==selectedIndex) continue;
        score[i] += (selectedRabbit.x+1 + selectedRabbit.y+1);
        // cout << "나머지 토끼들 점수 : "<<selectedRabbit.x +1 << ":"<<selectedRabbit.y +1<<endl;
    }

    

    // for(int i=0; i<P; i++){
    //     cout << i<<" 번째 토끼의 값\n";
    //     cout << "id : "<< rabbit[i].pidi<<"\n";
    //     cout << "dist : "<< distL[i]<<"\n";
    //     cout << "count : "<< rabbit[i].count<<"\n";
    //     cout << "score : "<< score[i]<<"\n";
    //     cout << "(x,y) : "<< rabbit[i].x <<", "<<rabbit[i].y <<"\n\n";
    // }
}

void printMaxRabbitScore(){
    long long maxScore = -1;
    for(int i=0; i<P; i++)
        maxScore = max(maxScore, score[i]);
    cout << maxScore;
}

void addBonusScore(){
    //5. 이번 k턴에 뽑혔던 토끼 구하기
    // for(int i=0; i<P; i++)
    //     cout << checkRabbit[i];
    afterKturn = priority_queue<Rabbit, vector<Rabbit>, compare3>();
    for(int i=0; i<P; i++)
        if(checkRabbit[i])
            afterKturn.push(rabbit[i]);
    
    Rabbit addSrabbit = afterKturn.top(); afterKturn.pop();
    score[rabbitIndex[addSrabbit.pidi]]+=S;

    rabbit[rabbitIndex[addSrabbit.pidi]]= addSrabbit;

    // cout <<"MAX"<<endl;
    // for(int i=0; i<P; i++){
    //     cout << i<<" 번째 토끼의 값\n";
    //     cout << "id : "<< rabbit[i].pidi<<"\n";
    //     cout << "dist : "<< rabbit[i].d<<"\n";
    //     cout << "count : "<< rabbit[i].count<<"\n";
    //     cout << "score : "<< rabbit[i].score<<"\n";
    //     cout << "(x,y) : "<< rabbit[i].x <<", "<<rabbit[i].y <<"\n\n";
    // }
}

void solve(){
    int Q;
    cin >> Q;
    for(int i=0; i<Q; i++){
        int command ; cin >> command;
        switch (command){
        case 100:
            //* 경주 시작 준비
            cin >> N >> M;  //격자
            cin >> P;   //토끼
            for(int j=0; j<P; j++){ //토끼의 고유번호, 이동 거리 
                cin >> rabbit[j].pidi;
                cin >> distL[j];
                rabbitIndex.insert({rabbit[j].pidi, j});
                // cout << rabbitIndex[rabbit[j].pidi]<<" "<<j<<endl;
            }
            break;
        case 200:  
            //* 경주 진행 단계
            cin >> K >> S;
            fill(checkRabbit, checkRabbit+2000, false); 
            pq = priority_queue<Rabbit, vector<Rabbit>, compare1>();
            for(int j=0; j<P; j++)
                pq.push(rabbit[j]);
            for(int j=0; j<K; j++){
                // cout <<j+1<<" round============\n";
                race();
            }
            //마지막 턴이 끝나면 S점수 더해주기
            addBonusScore();
            break;
        case 300:
            //* 이동 거리 변경 단계
            cin >> pid_T >> L;
            double_L_distance();
            break;
        case 400:
            //* 최고 토끼 선정 단계
            //P마리의 토기 최종 점수 중 최댓값 출력
            printMaxRabbitScore();
            break;
        default:
            break;
        }
    }
}

int main(){

    solve();

    return 0;
}