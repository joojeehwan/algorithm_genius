#include <bits/stdc++.h>

using namespace std;

int q;  //명령 개수
int n;  //n개의 선물
int m;  //m개의 벨트

//각 벨트의 head, tail 관리
int head[10], tail[10];
bool broken[10]; //벨트의 고장 여부


unordered_map<int, int> weight; //각 id의 무게  weight[id] = w;
unordered_map<int, int> belt_num; //각 물건id의 벨트번호 belt[id] = 1~
unordered_map<int, int> prv, nxt; //각 id의 이전, 이후 값


void buildfactory(){
    //input
    cin >> n >> m; //초기 공장 정보 n개의 선물, m개의 벨트
    vector<int> id(n);
    vector<int> w(n);
    for(int i=0; i<n; i++)
        cin >> id[i];
    for(int i=0; i<n; i++)
        cin >> w[i];

    //각 id의 무게  weight[id] = w;
    for(int i=0; i<n; i++)
        weight[id[i]]=w[i];

    //각 벨트에 len개씩 상자넣기 
    int len = n/m;
    for(int i=0; i<m; i++){
        head[i] = id[i*len];    //각 벨트에 나눠담기
        tail[i] = id[(i+1)*len-1];

        for(int j=i*len; j<(i+1)*len; j++){
            belt_num[id[j]] = i+1;

            if(j<(i+1)*len-1){
                nxt[id[j]] = id[j+1];
                prv[id[j+1]] = id[j];
            }
        }
    }

}

void push_back(int id, int curr_id){
    nxt[id] = curr_id;
    prv[curr_id] = id;

    //위치시키고자하는 위치의 id가 tail이었다면 tail을 curr로 변경
    int b_num = belt_num[id] -1;
    if(tail[b_num] == id)
        tail[b_num] = curr_id;
}


void remove_id(int id, bool remove_belt){
    int b_num = belt_num[id] - 1;

    //벨트에서 번호 게서
    if(remove_belt)
        belt_num[id] = 0;
    
    //벨트에 하나 남은 상자이면 head, tail에서 삭제
    if(head[b_num] == tail[b_num]){
        head[b_num] = 0;
        tail[b_num] = 0;
    }
    //삭제할 상자가 그 벨트의 head라면, head에는 삭제할 상자의 다음 상자를 가리키도록하고 이전값은 아무것도
    else if(id == head[b_num]){
        int next_id = nxt[id];
        head[b_num] = next_id;
        prv[next_id] = 0;
    }
    else if(id == tail[b_num]){
        int prev_id = prv[id];
        tail[b_num] = prev_id;
        nxt[prev_id]= 0;
    }
    else{   //middle id 삭제
        int prev_id = prv[id];
        int next_id = nxt[id];
        //내 이전id의 다음이 가리키는 건 내 다음 값
        nxt[prev_id] = next_id;
        //내 다음값의 이전id는 이제 내 이전꺼
        prv[next_id] = prev_id;
    }

    nxt[id] = 0;
    prv[id] = 0;
}



void drop(){
    int w_max; cin >> w_max;

    //각 벨트의 가장 첫번째 상자 무게 확인
    int w_sum=0;
    for(int i=0; i<m; i++){
        if(broken[i]) continue;

        //head가 있으면
        if(head[i]!=0){
            int id = head[i];
            int w = weight[id];

            //head의 상자가 w_max이하 : drop
            if(w <= w_max){
                w_sum +=w;
                remove_id(id,true);
            }
            //그 외의 경우에, 뒤에도 상자가 있다면
            else if(nxt[id]!=0){
                remove_id(id, false);
                push_back(tail[i], id);
            }

        }
    }

    //하차한 상자의 무게
    cout << w_sum<<"\n";
}

void remove(){
    int rmv_id; cin >> rmv_id;

    //벨트에 없는 id라면 -1리턴
    if(belt_num[rmv_id] == 0){
        cout << -1 <<"\n";
        return;
    }
    remove_id(rmv_id, true);
    cout << rmv_id<<"\n";
}

void find(){
    int find_id; cin >> find_id;

    //벨트에 없는 상자라면
    if(belt_num[find_id]==0){
        cout <<-1<<"\n";
        return;
    }

    //맨앞상자가 아니면 맨앞으로
    int b_num = belt_num[find_id]-1;
    //찾는 상자가 head가 아닐 때, head로 옮기기
    if(head[b_num]!=find_id){
        //내 벨트의 head, tail 저장
        int tmp_tail = tail[b_num];
        int tmp_head = head[b_num];

        //가존 테일이 내 이전 값을 가리키도록
        int new_tail = prv[find_id];
        tail[b_num] = new_tail;
        nxt[new_tail] = 0;  //나는 0

        //내 tail의 next를 맨앞으로 가져오기
        nxt[tmp_tail] = tmp_head;
        prv[tmp_head] = tmp_tail;

        //head를 find로 지정
        head[b_num] = find_id;
    }

    cout <<b_num+1<<"\n";

}

void beltbroken(){
    int b_num; cin >> b_num; b_num-=1;

    if(broken[b_num]){
        cout << -1<<"\n";
        return;
    }

    //고장내기
    broken[b_num] = 1;
    if(head[b_num] == 0){
        cout <<b_num+1<<"\n";
        return;
    }

    //고장나지 않은 벨트를 오른쪽방향으로 돌면서 찾고
    //상자 옮겨주기
    int next_belt_num = b_num;

    while(1){
        //오른쪽으로 돌면서
        next_belt_num = (next_belt_num+1)%m;
        if(broken[next_belt_num]==false){   //정상벨트 찾음
            //만약 찾은 벨트가 빈벨트라면 내 벨트의 head, tail 복사해주기
            if(tail[next_belt_num] == 0){
                head[next_belt_num] = head[b_num];
                tail[next_belt_num] = tail[b_num];
            }
            else{
                //내 벨트의 head를 새 벨트의 tail뒤에 붙이기
                push_back(tail[next_belt_num], head[b_num]);
                //tail 새걸로 바꿔주기
                tail[next_belt_num] = tail[b_num];
            }
            
            //옮긴 belt들을 모두 보면서
            //belt number를 새로운 벨트 넘버로 모두 갱신해주기
            int id = head[b_num];
            while(id!=0){
                belt_num[id] = next_belt_num+1;
                id = nxt[id];
            }
            head[b_num] = 0;
            tail[b_num] = 0;
            break;
        }
    }
    cout << b_num+1<<"\n";
}


void input(){
    cin >> q;
    while(q--){
        int order; cin >> order;
        if(order==100)
            buildfactory();
        else if(order==200)
            drop();
        else if(order==300)
            remove();
        else if(order==400)
            find();
        else 
            beltbroken();
    }
}

int main(){

    input();

}