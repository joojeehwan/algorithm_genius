#include <bits/stdc++.h>

using namespace std;

int N;
int arr[1000];
bool used[1000];
int maxEnerge = -0xffffff;
int len;


void dfs(int x, int sum){
    // cout <<x <<" "<< len <<" " <<sum<<endl;

    if(len==2){
        maxEnerge = max(maxEnerge, sum); 
        return;
    }


    // pick x-1
    int left = x-1;
    while(left >= 0){
        if(!used[left]){
            break;
        }
        left-=1;
    }

    // pick x+1
    int right = x+1;
    while(right<=N-1){
        if(!used[right]){
            break;
        }
        right+=1;
    }

    // cout << arr[left]*arr[right]<<endl;
    for(int i=1; i<N-1; i++){

        sum += arr[left]*arr[right];
        used[x] = true;
        len -=1;
        
        if(!used[i] || len ==2)
            dfs(i, sum);
        
        len+=1;
        sum -= arr[left]*arr[right];
        used[x] = false;
    }
}

int main(){

    cin >> N; 
    len = N;
    for(int i=0; i<N; i++)
        cin >> arr[i];


    for(int i=1; i<N-1; i++){
        dfs(i, 0);
    }

    cout << maxEnerge <<"\n";
    
    return 0;
}