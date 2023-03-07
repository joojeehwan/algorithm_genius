#include <bits/stdc++.h>

using namespace std;

int main(){

    int N; cin >> N;
    vector<int> posi;
    vector<int> nega;  
    vector<int> zero;

    for(int i=0; i<N; i++){
        int a; cin >> a;
        if(a > 0) posi.push_back(a);
        else if(a==0) zero.push_back(a);
        else nega.push_back(a); 
    } 

    //sortcin >> arr[i];
    sort(posi.begin(), posi.end());
    sort(nega.begin(), nega.end());

    //뒤에서부터 곱하기
    //양수일때 처리
    int posi_sum = 0;
    if(posi.size()>0){
        for(int i = posi.size()-1; i>=0; i--){
            if(i-1 >= 0 && (posi[i] * posi[i-1] > posi[i] + posi[i-1])){    //1 1 1
                posi_sum += posi[i] * posi[i-1];
                i--;
            }
            else{
                posi_sum += posi[i];   
            }
        }
    }

    //음수일때 처리
    int nega_sum = 0;
    if(nega.size()>0){
        //0이 있는 경우
        if(zero.size()>0){
            //음수가 짝수개인경우
            if(nega.size()%2==0){
                //앞에서부터 2개씩 묶기
                for(int i=0; i+1<=nega.size()-1; i+=2){
                    nega_sum+=nega[i]*nega[i+1];
                }
            }
            //음수가 홀수개인 경우
            //-1(idx:0) 0(idx:1) 0
            else{
                for(int i=0; i+1<nega.size(); i+=2){
                    nega_sum+=nega[i]*nega[i+1];
                }
                //0이 있다면 남는 숫자는 skip
            }
        }   
        else{//0이 없는 경우
            //앞에서부터 두개씩 묶기
            //음수가 짝수개인경우
            if(nega.size()%2==0){
                //마지막(0)제외하고 앞에서부터 2개씩 묶기
                for(int i=0; i+1<=nega.size()-1; i+=2){
                    nega_sum+=nega[i]*nega[i+1];
                }
            }
            //음수가 홀수개인 경우
            else {
                for(int i=0; i+1<=nega.size()-1; i+=2){
                    nega_sum+=nega[i]*nega[i+1];
                }
                //마지막 수 더하기
                nega_sum+=nega[nega.size()-1];
            }
        }
    }
    cout << posi_sum + nega_sum<<endl;
    


    return 0;
}