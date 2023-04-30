#include <bits/stdc++.h>

using namespace std;
 
int N;
int arr[1000000];
vector<int> v;
int pos[1000000];   //arr의 index번째 숫자의 위치는 pos[index]이라는 의미
// 10 20 30 
//pos[0] = 2

void solve(){
    for(int i=0; i<N; i++){

        if(v.size()==0 || v[v.size()-1] < arr[i]) {
            v.push_back(arr[i]);
            pos[i] = v.size()-1;
        }
        else{
            int left=0;
            int right = v.size()-1;
            //오름차순으로 넣어야해서 내가 넣어야하는 숫자는 특정 수보다 작은 쪽에
            while(left < right){
                int mid = (left + right)/2;
                if(arr[i] <= v[mid]) right = mid; //내가 넣으려는 숫자가 v배열에 있는 mid보다 작으면 v배열 왼쪽에서 탐색
                else left = mid+1;    //v배열의 mid 값보다 내가 넣으려는 숫자가 크면 오른쪽에서 탐색
            }
            v[left] = arr[i];
            pos[i] = left;
        }
    }
    //10 20 30 50
    //10 15 30 50

    //10 20 10 30 15 50
    //1   2  1  3  2  4
    vector<int> ans;
    cout << v.size() <<"\n";
    int index = v.size()-1;
    for(int i = N-1; i>=0; i--){
        if(pos[i] == index) {
            ans.push_back(arr[i]);
            index--;
        }
    }

    // reverse(ans.begin(), ans.end());
    // for(auto a : ans)
    //     cout << a<<" ";
}


int main(){

    cin >> N;
    for(int i=0; i<N; i++)
        cin >> arr[i];

    solve();

    return 0;
}