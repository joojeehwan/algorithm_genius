#include <bits/stdc++.h>

using namespace std;


void dfs(int start, int end, int mid, int N){

    //S(0) = "m o o" 3자리
    //S(1) = "m o o / m o o o / m o o" 10자리 
    //S(2) = "m o o m o o o m o o / m o o o o / m o o m o o o m o o" 25자리 - 4
    if(end - start + 1 == 3){
        char retVal = (N == start ? 'm' : 'o');
        cout << retVal << "\n";
        return;
    }

    //S(k) = S(k-1) + m+o(k+2) + S(k-1)
    int first = ((end - start + 1) - mid) / 2 + start - 1;    //첫번째 S(k-1)의 끝 지점
    int second = first + mid + 1;   //두번째 S(k-1)이 시작 지점

    // cout << "first: " << first <<", mid : "<<mid<< ", second : "<<second<<endl;

    if(N <= first)  //구하려는 자리가 첫번째 S(k-1)범위에 있을 때
        dfs(start, first, mid-1, N);
    else if(N>=second)  //구하려는 자리가 두번째 S(k-1)범위에 있을 때
        dfs(second, end, mid-1, N);
    else{   //구하려는 자리가 가운데 범위 값일 때
        cout << (N == first + 1 ? 'm' : 'o') << "\n";
        return;
    }
                                                                                                                                            
}

int main(){         

    int N;
    cin >> N;

    int strlen = 0;
    int k=0;

    //길이가 N보다 크거나 같은 S(k)의 길이 구하기
    //S(k) = S(k-1) + m+o(k+2) + S(k-1)
    //     = 2S(k-1) + (k+3)개
    for(k=0; strlen < N; k++){
        strlen*=2;
        strlen+=(k+3);  //moo
    }
    // cout << strlen <<", " <<k-1 <<endl; 
    //N번째를 셀 수 있는 최소의 k-1 찾음
    dfs(1, strlen, 1+(k-1)+2, N);

    return 0;
}