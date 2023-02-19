#include <bits/stdc++.h>>

using namespace std;


void dfs(int start, int end, int mid, int N){
    if(end - start + 1 == 3){
        //첫번째이면 m 그외 o
        cout << (N == start ?'m' : 'o') << "\n";
        return;
    }

    int first = (end - start + 1 - mid) / 2 + start - 1;
    int second = first + mid + 1;

    if(N <= first)
        dfs(start, first, mid-1, N);
    else if(N>=second)
        dfs(second, end, mid-1, N);
    else{
        cout << (N == first +1 ?'m' : 'o') << "\n";
        return;
    }
                                                                                                                                            
}

int main(){         

    int N;
    cin >> N;

    int strlen = 0;
    int k=0;

    //길이가 N보다 크거나 같은 S(k)의 길이 구하기
    for(k=0; strlen < N; k++){
        strlen*=2;
        strlen+=(k+3);
    }

    dfs(1, strlen, k+2, N);

    return 0;
}