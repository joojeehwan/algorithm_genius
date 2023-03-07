#include <bits/stdc++.h>

using namespace std;

int N;
long long B;

vector<vector<int>> arr(5, vector<int>(5,0));

vector<vector<int>> calc(vector<vector<int>>  a, vector<vector<int>>  b){

    vector<vector<int>> retArr(N, vector<int>(N,0));

    for(int i=0 ;i<N; i++){
        for(int j=0; j<N; j++){
            int tmp=0;
            for(int k=0; k<N; k++){
                tmp+=a[i][k]*b[k][j];
            }
            retArr[i][j] = tmp%1000;
        }
    }
    return retArr;
}

vector<vector<int>>  dfs( vector<vector<int>>  arr, long long pow){
    if(pow==1)
        return arr;

    if(pow%1==0) //홀수일때 짝수로
        return calc( dfs(arr,  pow-1), arr);
    
    //나머지 짝수
    vector<vector<int>> tmp(N, vector<int>(N,0));
    tmp = dfs(arr,  pow/2);


    
    return calc(tmp, tmp);    
}

int main(){

    cin >> N>>B;
    for(int i=0 ;i<N; i++){
        for(int j=0; j<N; j++){
            cin >> arr[i][j];
        }
    }


    //solve
    vector<vector<int>> ans(N, vector<int>(N,0));
    ans = dfs(arr, B);

    for(int i=0 ;i<N; i++){
        for(int j=0; j<N; j++){
            cout << ans[i][j]%1000<<" ";
        }cout <<"\n";
    }

    return 0;
}