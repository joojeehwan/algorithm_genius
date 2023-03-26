#include <bits/stdc++.h>

using namespace std;

int arr[1001];
int sum = 0;

int main(){
    // 1000 10^3 *10^3 = 10^6
    // 다 합쳐서 만들 수 있는 무게 = 50
    // 50보다 작은 수 중에서 추로 만들 수 없는 무게
    // 추로 만들 수 있는 무게 :
    //  1 + 3 + 6 +...
    //  1 + 3
    //  1
    int N; cin >> N;
    for(int i=0; i<N; i++)
        cin >> arr[i];
    
    sort(arr, arr+N);

    // 1 1 2 3 4
    for(int i=0; i<=N; i++){
        //  sum , sum+1 , arr[i]
        if(arr[i] > sum+1){
            break;
        }
        sum += arr[i];
        // cout <<arr[i]<<endl;
    }
    cout << sum+1<<endl;

    return 0;
}