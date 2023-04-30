#include <bits/stdc++.h>

using namespace std;

//https://st-lab.tistory.com/281
//https://www.acmicpc.net/blog/view/109

int main(){

    int N, K;
    cin >> N >> K;
    // A[i][j] = i*j
    // A[N][N]을 정렬해서 B[N*N]을 만든다.
    // B[K] = x
    // K는 x보다 작거나 같은 수들의 개수이다.

    // 3보다 작은 수의 개수는
    // 3/1 = 3 => 1단에서 3개
    // 3/2 = 1 => 2단에서 1개
    // 3/3 = 1 => 3단에서 1개
    // 총 5개이므로 3보다 작거나 같은 수의 개수는 5개
    // x를 조정해가면서 K(x보다 작은 원소의 갯수)를 찾고
    // 문제에서 주어진 K랑 같은지 확인

    int left = 1;
    long right = K;

    while(left < right){

        //x 를 left와 right의 중간 값으로 잡눈다.
        int mid = (left + right) / 2;
        
        long  cnt = 0;
        //각 단계별로 전체 곱셈을 나누어서 mid보다 작거나 같은 수의 갯수를 구하여 sum한다.
        for(int i=1; i<=N; i++){

            //13(x)/1(i) = 13개 
            //근데 N의 범위는 4까지니깐 13개까지 필요 없다. 4개까지만 4보다 작은수인거다. 
            cnt += min(mid / i, N);
        }

        // x보다 작거나 같은 수의 갯수, K를 비교
        // K보다 작으면 cnt가 커지도록 x 값을 늘린다
        // x 를 늘리려면 left가 늘어나야함
        // left를 mid 다음값으로 하나 늘려줌
        if(cnt < K){
            left = mid+1;
        }
        else{
            right = mid;
        }

    }
    cout << left;
    // X <= K



    return 0;
}