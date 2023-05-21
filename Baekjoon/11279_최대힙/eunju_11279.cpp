#include <bits/stdc++.h>

using namespace std;

int N;
int arr[100050];
int pqSize = 0;

void push(int x){
    arr[++pqSize] = x;
    int index = pqSize;
    int tmp;
    while(index > 1){   
        //새로들어온게 부모보다 클경우
        //자리 변경
        if(arr[index] > arr[index / 2]){
            tmp = arr[index];
            arr[index] =  arr[index / 2];
            arr[index / 2] = tmp;
        }
        else break;
        
        index /= 2;
    }
}

void top(){
    if(pqSize<=0){
        cout << 0<<"\n";
        return;
    }


    cout << arr[1] << "\n";
    // 맨 마지막 원소 가져오기
    arr[1] = arr[pqSize];  pqSize-=1;

    // 자리 재정렬
    int index = 1;
    int tmp;
    int change_flag=0;
    while(index < pqSize){

        change_flag = 0;

        //자기랑 왼쪽 자식이랑 비교
        if(arr[index]< arr[index*2] && index*2 <=pqSize ){
            change_flag = 1;
            //오른쪽 자식이 더 크다면 오른쪽 자식을 올리기
            if(arr[index*2]< arr[index*2+1] && index*2+1 <=pqSize){
                change_flag = 2;
            }
        }
        //오른쪽 자식이 더 크면 오른쪽 올리기
        else if(arr[index]< arr[index*2+1] && index*2+1 <=pqSize){
            change_flag = 2;
        }

        // 자리바구기
        if(change_flag==0) break;
        else if(change_flag==1){    //왼쪽 자식이랑 바꾸기
            index *=2;
            tmp = arr[index];
            arr[index] = arr[index/2];
            arr[index/2] = tmp;
        }
        else if(change_flag==2){
            index = index*2+1;
            tmp = arr[index];
            arr[index] = arr[index/2];
            arr[index/2] = tmp;
        }
    }

}


int main(){
    cin.tie(0);
    cin.sync_with_stdio(0);
    cin >> N;
    for(int i=0; i<N; i++){ 
        int x; cin >> x;
        if(x == 0) top();
        else push(x);
        
    }

    return 0;
}