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

void move_right(int* y, int* d) {  // x, y 에서 d 만큼 오른쪽 이동을 시도. 만약 오른쪽 끝에 도달한다면 멈춤.
    if (M -1 >= *y + *d) {  // 오른쪽 끝까지의 거리보다 작거나 같게 이동한다면, 바로 이동하기 : 오른쪽 끝에 도달한거라면 오른쪽 끝에 멈추기
        *y += *d;
        *d = 0;
    }
    else {
        *d -= (M-1 - *y);   //이번에 이동한 거리는 빼주고 앞으로 이동해야하는 거리 갱신해준다.
        *y = M-1;
    }
}

void move_left(int* y, int* d) {
    if (*y-*d >= 0) { //y좌표에서 d만큼 완쪽으로 움직인 좌표가 0보다 크거나 같으면 y좌표 0으로 갱신
        *y -= *d;
        *d = 0;
    }
    else {  //더 작으면 이번에 이동한 거리 y좌표만큼은 빼주고 y도 0으로 갱신  
        *d -= *y;
        *y = 0;
    }
}

void move_up(int* x, int* d) {
    if (*x - *d >= 0) {
        *x -= *d;
        *d = 0;
    }
    else {
        *d -= *x;
        *x = 0;
    }
}
void move_down(int* x, int* d) {
    if (N-1>= *d + *x ) {
        *x += *d;
        *d = 0;
    }
    else {
        *d -= (N-1 - *x);
        *x = N-1;
    }
}

pair<int,int> jump(int cx, int cy, int cd){
    vector<pair<int, int>> goals;
    // 오른쪽으로 이동하기
    {
        int period = (M - 1) * 2;   //주기 : 왼쪽, 오른쪽을 period칸 움직이면 제자리
        int x = cx, y = cy;
        int d = cd % period;    //최종 움직여야 하는 거리
        move_right(&y, &d); //오른쪽 끝에 도달하는 경우
        move_left(&y, &d);  //남은 거리만큼 다시 움직여줌
        move_right(&y, &d);
        goals.push_back({ x, y });
    }
    // 왼쪽으로 이동하기
    {
        int period = (M - 1) * 2;
        int x = cx, y = cy;
        int d = cd % period;
        move_left(&y, &d);
        move_right(&y, &d);
        move_left(&y, &d);
        goals.push_back({ x, y });
    }
    // 윗쪽으로 이동하기
    {
        int period = (N - 1) * 2;
        int x = cx, y = cy;
        int d = cd % period;
        move_up(&x, &d);
        move_down(&x, &d);
        move_up(&x, &d);
        goals.push_back({ x, y });
    }
    // 아랫쪽으로 이동하기
    {
        int period = (N - 1) * 2;
        int x = cx, y = cy;
        int d = cd % period;
        move_down(&x, &d);
        move_up(&x, &d);
        move_down(&x, &d);
        goals.push_back({ x, y });
    }
    sort(goals.begin(), goals.end(), [](pair<int, int> A, pair<int, int> B) {
        if (A.first + A.second != B.first + B.second) return A.first + A.second > B.first + B.second;
        return A.first > B.first;
    });
    return goals[0];
}

void race(){
    //1. 우선순위가 가장 높은 토끼를 결정
    //   각 레이스마다 K번의 턴이 모두 진행된 직후에 우선순위가 높은 토끼를 골라야해서
    Rabbit selectedRabbit = pq.top(); pq.pop();
    int selectedIndex = rabbitIndex[selectedRabbit.pidi];
    checkRabbit[selectedIndex] = true;


    //2. 토끼가 상하좌우 이동했을 때 4방향 위치 구하기
    //주어진 electedRabbit.d 5칸을 다 이동 해야 함.
    pair<int,int> movePos = jump(selectedRabbit.x, selectedRabbit.y ,distL[selectedIndex]);

    //3. 우선순위가 높은 칸으로 토끼 좌표 변경시키기
    selectedRabbit.x = movePos.first;
    selectedRabbit.y = movePos.second;
    selectedRabbit.count +=1;


    rabbit[selectedIndex] = selectedRabbit;
    pq.push(selectedRabbit);

    //4. 나머지 토끼들 점수 누적하기
     for(int i=0; i<P; i++){
        if(i==selectedIndex) continue;
        score[i] += (selectedRabbit.x+1 + selectedRabbit.y+1);
    }

}

void printMaxRabbitScore(){
    long long maxScore = -1;
    for(int i=0; i<P; i++)
        maxScore = max(maxScore, score[i]);
    cout << maxScore;
}

void addBonusScore(){

    //5. 이번 k턴에 뽑혔던 토끼 구하기
    afterKturn = priority_queue<Rabbit, vector<Rabbit>, compare3>();
    for(int i=0; i<P; i++)
        if(checkRabbit[i])
            afterKturn.push(rabbit[i]);
    
    Rabbit addSrabbit = afterKturn.top(); afterKturn.pop();
    score[rabbitIndex[addSrabbit.pidi]]+=S;
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
            }
            break;

        case 200:  
            //* 경주 진행 단계
            cin >> K >> S;
            //race 진행
            fill(checkRabbit, checkRabbit+2000, false); 
            pq = priority_queue<Rabbit, vector<Rabbit>, compare1>();
            for(int j=0; j<P; j++)  pq.push(rabbit[j]);
            for(int j=0; j<K; j++)  race();
            
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