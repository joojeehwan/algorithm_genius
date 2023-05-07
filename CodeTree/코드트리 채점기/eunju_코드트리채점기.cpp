#include <bits/stdc++.h>
#include<string>

using namespace std;

// 정답 : 시간 t에 채점 대기 큐에 있는 채점 task의 수를 출력합니다.
//채점 대기 큐 사이즈 관리
int N;
int answer=0;

/*
 * @ machinePQ : 쉬고있는 채점기 중 가장 낮은 번호 리턴
*/
priority_queue<int, vector<int>, greater<int> > machinePQ;
int machine_domain[50001]; // 채점기들이 채점중인 도메인 인덱스 저장

/* 
 *  @ problemReadyQ :  우선순위가 가장 높은 채점 task를 선택하기 위해
 *  도메인 그룹별로 우선순위가 가장 높은 채점 task를 뽑아야하기 때문에 -
 *  301개 배열로 pq를 만들어줌
*/
struct Problem{ //Problem Struct
    int start_time; //가장 최근에 진행된 채점 시작 시간
    int priority;  //채점 우선순위
    int id;   //도메인 뒤 id 값

    bool operator <(const Problem &b) const {
        if(priority == b.priority){
             return start_time > b.start_time;
        }
        return priority > b.priority;
    }
};
priority_queue<Problem> problemReadyQ[301];

//각 도메인에 존재하는 문제 id중에서 어떤 문제ID가 채점대기 큐에 존재하는 지 관리 - 
// 채점하려는 task의 도메인이 현재 채점중인(채점 대기큐에 존재하는) 도메인 중 하나라면 불가능합니다.
set<int> idInReadyQ[301];


/**
 * @ domain 정보
 * 목적 : map으로 도메인들의 존재성을 판단하기 위함
 * 도메인을 index로 변환
*/
map<string, int> domainToIndex; //[domain] = index
int domainIndex = 0;
int s[301]; // 각 도메인별 start
int g[301]; // 각 도메인별 gap
int e[301]; // 각 도메인별 end 채점이 가능한 최소 시간


void CodeTreeReady(int N, string u0){
    //1~N까지 채점기 추가
    for(int i=1; i<=N; i++)
        machinePQ.push(i);

    //url 분리
    int sep_pos = u0.find("/", 0);
    string domain  = u0.substr(0,sep_pos); //도메인 부분
    int id = stoi(u0.substr(sep_pos+1, u0.size())); //id 부분

    //도메인을 인덱스로 관리
    if(!domainToIndex[domain]){
        domainIndex++;
        domainToIndex[domain] = domainIndex;
    }

    //도메인별로 레디큐에 id가 존재하는 지 여부를 관리하기 위해
    //도메인id 관리 set에 id를 추가해준다
    idInReadyQ[domainIndex].insert(id);

    //새로 들어온 문제를 조건에 맞게 추가
    Problem newProblem;
    newProblem.start_time = 0;
    newProblem.priority = 1;// 채점 우선순위가 1
    newProblem.id = id;// url : u0
    problemReadyQ[domainIndex].push(newProblem); //채점 대기 큐에 추가

    answer+=1;  //채점대기큐 사이즈 1 증가
}

//들어온 url이 현재 채점중인 url이라면 채점 불가
void RequestMachine(int t, int p, string url){    //t초, t초에 우선순위, url
    //url 분리
    int sep_pos = url.find("/", 0);
    string domain  = url.substr(0,sep_pos); //도메인 부분
    long long int id = stoll(url.substr(sep_pos+1, url.size())); //id 부분

    //처음 나온 도메인이라면 domainToindex에 새로 추가
    if(!domainToIndex[domain]){
        domainIndex++;
        domainToIndex[domain] = domainIndex;
    }

    //채점 대기 큐에 있는 task 중 정확히 u와 일치하는 url이 단 하나라도 존재한다면 큐에 추가하지 않고 넘어갑니다.
    //새로들어온 id의 도메인이 헤당 도메인의 채점대기큐에 존재하는 id라면 return == 채점중 
    if(idInReadyQ[domainIndex].find(id) != idInReadyQ[domainIndex].end())
        return;
    
    //채점 대기 큐에 없는 id라면 채점 대기 큐에 넣어준다.
    idInReadyQ[domainIndex].insert(id); //채점대기큐의 id를 관리하는 set에 id 추가

    Problem newProblem;
    newProblem.start_time = t;
    newProblem.priority = p;// 채점 우선순위가 1
    newProblem.id = id;// url : u0
    problemReadyQ[domainIndex].push(newProblem); //t초에, 우선순위 p, id값

    //채점 대기 큐 값 1 증가
    answer+=1;
}

//채점 시도
void TryCalculateScore(int t){
    //쉬고있는 채점기가 없다면 리턴
    if(machinePQ.empty()) return;

    //대기 큐에서 즉시 채점이 가능한 경우 중 우선순위가 가장 높은 채점 task
    //가장 우선순위가 높은 url을 찾는다.
    int min_domainindex = 0;
    Problem minProblem; minProblem.priority = 0xffffff; 
    
    //현재까지 추가된 문제들 중에서
    for(int i=1; i<=domainIndex; i++){
        //t가 현재 채점이 불가능한 시간이라면
        //현재 도메인의 채점 가능한 시간은 e[i]이상
        if(e[i] > t) continue;

        // 어떤 도메인 그룹의 문제 중에
        // 해당 도메인 그룹에서 가장 우선순위가 높은 url을 뽑아서 갱신해준다.
        if(!problemReadyQ[i].empty()){
            Problem curr = problemReadyQ[i].top();

            if(minProblem < curr){
                minProblem = curr;
                min_domainindex = i;
            }
        }
    }

    //가장 우선순위가 높은 도메인을 찾았다면
    //해당 도메인 - 쉬고있는 가장 낮은 번호의 채점기 연결
    if(min_domainindex > 0){
        int machine_index = machinePQ.top(); machinePQ.pop();

        //해당 도메인의 가장 우선순위가 높은 문제id를 지운다
        problemReadyQ[min_domainindex].pop();

        //해당 도메인의 start, end 갱신
        s[min_domainindex] = t;
        e[min_domainindex] = 0xffffff;
        
        //machine_index의 채점기가 채점하고있는 도메인을 업데이트 시켜준다.
        machine_domain[machine_index] = min_domainindex;
        // 채점 관리큐에 해당 도메인의 id가 들어가있는 지를 관리하는 set에서 해당 문제 id를 지운다
        idInReadyQ[min_domainindex].erase(idInReadyQ[min_domainindex].find(minProblem.id));
        answer-=1;
    }
}

void StopMachine(int t, int J_id){  //J_id 채점기 번호
    //만약 해당 채점기가 채점중이라면
    if(machine_domain[J_id] == 0) return;

    //쉬고있는 채점기 리스트로 보내버리기
    machinePQ.push(J_id);
    int domain_index = machine_domain[J_id];
    machine_domain[J_id] = 0;

    //해당 도메인의 gap, end값을 갱신
    g[domain_index] = t - s[domain_index];
    e[domain_index] = s[domain_index] + 3*g[domain_index];
}

void RetvReadyQueue(){
    cout << answer <<"\n";
}

void input(){
    int Q; cin >> Q;
    while(Q--){
        int command; cin >> command;
        switch(command){
            //코드트리 채점기 준비
            case 100:
            {   
                //N개의 채점기, url 담은 u0 
                string u0; 
                cin >> N >> u0;
                CodeTreeReady(N, u0);
                break;
            }
            //채점 요청
            case 200:
            {
                int t, p; cin >> t >> p;
                string u; cin >> u;
                RequestMachine(t, p, u);
                break;
            }
            //채점 시도
            case 300:
            {   
                int t; cin >> t;
                TryCalculateScore(t);
                break;
            }
            //채점 종료
            case 400:
            {   
                //t초에 J_id번 채점기가 진행하던 채점을 종료시킴
                int t, J_id; cin >>t >> J_id;
                StopMachine(t, J_id);
                break;
            }
            //채점 대기큐 조회
            case 500:
            {
                int t; cin >> t;
                RetvReadyQueue();
                break;
            }
            default:
            break;
        }
    }
}


int main(){

    input();

    return 0;
}