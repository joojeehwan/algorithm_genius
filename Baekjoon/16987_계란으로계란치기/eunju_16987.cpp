#include <bits/stdc++.h>

using namespace std;

int N;
struct Egg{
    int strong; //내구성
    int weight; //계란무게
};

Egg egg[8];
int maxnum = 0;

void dfs(int mine){
    if(mine == N){ //가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란깨기 종료
        int cnt = 0;
        for(int i=0; i<N; i++){
            if(egg[i].strong<=0) cnt++; //깨진 계란의 갯수 세기 
        }   
        maxnum = max(maxnum,cnt);
        return;
    }

    // 손에 든 계란이 깨진 경우 치지 않고 넘어간다.
    // 오른쪽 계란을 집어서 다시 진행
    if(egg[mine].strong <= 0){
        dfs(mine+1);
        return; //dfs 돌고 나와서 다음 명령을 진행 안하도록 
    }  
    
    //모든 계란을 둘러 보면서
    //살아있는 계란이 없으면.. 
    bool alive_egg = false;
    for(int i=0; i<N; i++){
        if(i == mine) continue;
        if(egg[i].strong <= 0) continue; //계란이 안깨진 것만 볼려고
        
        //안깨진계란 존재
        alive_egg = true;

        egg[i].strong -=egg[mine].weight;
        egg[mine].strong -=egg[i].weight;
        dfs(mine+1);

        egg[i].strong +=egg[mine].weight;
        egg[mine].strong +=egg[i].weight;
    }
    
    if(!alive_egg){ //깰 계란 중에 깨지지 않은 계란이 없으면 치지 않고 넘어간다
        dfs(mine+1);
    }
}

int main(){
    //각 계란의 내구도는 상대 계란의 무게만큼 깎이게 된다.

    cin >> N;
    for(int i=0; i<N; i++){
        cin >> egg[i].strong >> egg[i].weight;
    }

    //가장 왼쪽의 계란으로
    //나머지 계란 중 하나를 선택하는 모든 경우를 실행해본다
    int mine = 0; // 가장 왼쪽의 계란
    dfs(mine);
    
    cout << maxnum;
    return 0;
}