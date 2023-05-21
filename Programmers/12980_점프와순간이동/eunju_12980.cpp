#include <bits/stdc++.h>

using namespace std;

int solution(int n)
{
    int ans = 0;
    
    // 현재까지 온 거리 * 2
    // 모든 경우의 수를 다 해봐야 함

    // 5 ==> 0~4
    // [n=4] 4 % 2 == 0 )) cnt : 1
    // [n=2] 2 % 2 == 0 )) cnt : 1
    // [n=1] cnt : 2

    // 6 
    // [n=3] 6 % 2 == 0  )) cnt : 0
    // [n=2] 3 % 2 == 1 ==> )) cnt : 1
    // [n=1] 1 % 2 == 1 ==> )) cnt : 2

    // 마지막 숫자로 n을 만들어야 한다
    // 홀수이면 만들 수 없으니 -1, 짝수이면 만들 수 있으니 //2
    // 
    
    while(n!=0){
        if(n%2==1){
             ans+=1;
             n-=1;
        }
        else{
            n/=2;
        }
    }


    return ans;
}

int main(){
    cout << solution(5000);

    return 0;
}
