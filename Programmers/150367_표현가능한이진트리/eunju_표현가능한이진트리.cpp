#include <bits/stdc++.h>

using namespace std;

bool check;

bool solve(string s, int cur, int left, int right){
    //마지막 노드인 경우
    if(left==right){
        if(s[cur] =='1') return true;
        else return false;
    }
    else{
        //왼쪽 트리 확인
        int l = left, r = cur -1;
        bool c1 = solve(s, (l+r)/2, l, r);

        //오른쪽 서브트리 확인
        l = cur+1, r=right;
        bool c2 = solve(s, (l+r)/2, l, r);
        
        //부모가 0인데 1인 자식이 잇는 경우
        if(s[cur] == '0' && (c1 || c2)) check = false;
        //부모가 1인경우 자식이 어떤 값이든 상관 없음(TT TF FT)
        if(c1 || c2 || s[cur]=='1') return true;
        // 0 0  0 가능
        else return false;
    }
}

vector<int> solution(vector<long long> numbers) {
    vector<int> answer;

    for(int i=0; i<numbers.size(); i++){
        long long num = numbers[i];
        string s = "";
        check = true;

        //이진수로 만들기 6 : 110 -> 011
        while(num){
            if(num%2) s+='1';
            else s+='0';
            num/=2;
        }
        
        int len = s.size(); //이진수의 길이
        int cnt = 1; //반복할 때마다 level1, 2, 3의 노드 개수
        int j = 2;
        //주어진 수의 길이를 초과하면 그만
        while(len > cnt){
            cnt+=j;
            j*=2;
        }

        //모자란 개수만큼 더미노드를 만들어서 포화이진트리로 만들기
        //숫자가 안변하도록 뒤에 추가
        for(j=0; j<cnt-len; j++)
            s+='0';
        
        reverse(s.begin(), s.end());
        len = s.size();

        //서브트리로서 존재 가능한 지 확인.
        //root가 0이면 이진트리로 존재 불가.
        int left = 0, right = len-1;
        solve(s, (left+right)/2, left, right);

        if(check) answer.push_back(1);
        else answer.push_back(0);

        
    }

    return answer;
}

int main(){

    vector<long long> numbers = {7, 42, 9};

    solution(numbers);

    return 0;
}