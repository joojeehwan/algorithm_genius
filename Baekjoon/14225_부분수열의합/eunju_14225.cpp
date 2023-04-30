#include <bits/stdc++.h>

using namespace std;

int N;
int arr[21];
bool possible[2000001];

void dfs(int el, int sum){
    possible[sum] = true;

    if(el == N) return;

    dfs(el+1, sum);
    dfs(el+1, sum + arr[el]);
}

int main(){

    cin >> N;
    for(int i=0; i<N; i++)
        cin >> arr[i];


    dfs(0,0);

    int i=1;
    for(; i<2000001; i++)
        if(!possible[i]) break;
    cout << i;
    return 0;
}