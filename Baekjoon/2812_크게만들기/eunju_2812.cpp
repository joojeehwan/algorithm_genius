#include <bits/stdc++.h>

using namespace std;

char number[5000000];
int N,k; //N자리 숫자, K개 지우기


void solve(){
    int erased=0;
    int end = 1;

    for(int i=1; i<N; i++){
        char c; cin >>c; 
        // 이전 숫자가 더 작으면 배열에서 지우기
        while(number[end-1]<c && end>0){
            if(erased==k) break;    //다 지웟으면 break
            erased++;
            end--;
        }
        number[end] = c;
        ++end;
    }


    for(int i=0; i<N-k; i++){
        cout <<number[i];
    }cout <<"\n";

}

int main(){

    //첫번째 수 먼저 받아놓기 924부터 비교
    cin >>N>> k>> number[0];
    solve();

    return 0;
}