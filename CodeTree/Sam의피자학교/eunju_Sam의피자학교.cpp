#include <bits/stdc++.h>

using namespace std;

int N, K;
int arr[100];

void plusOne(){
    int minNum = 0xffffff;
    vector<int> v;
    for(int i=0; i<N; i++)
        minNum = min(minNum, arr[i]);
    
    for(int i=0; i<N; i++)
        if(arr[i]==minNum) arr[i]+=1;
}

void rollDough(){
    

}

void pushDough(){

}

void foldDough(){

}


void solve(){
    //1. 밀가루 양이 가장 작은 위치에 밀가루 1만큼 더 넣어줍니다.(가장 작은 위치가 여러 개라면 모두 넣기)
    plusOne();
    //2. 도우를 말아줍니다.
    rollDough();
    //3. 도우를 꾹 눌러줍니다.
    pushDough();
    //4. 도우를 두 번 반으로 접어줍니다.
    foldDough();
    //5. 3의 과정만 한번 더 진행합니다.
    pushDough();

}

void input(){
    cin >> N >> K;
    for(int i=0; i<N; i++) cin >> arr[i];
}

int main(){

    input();

    solve();

    return 0;
}