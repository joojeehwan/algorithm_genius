#include <bits/stdc++.h>

using namespace std;

string rule1(string sentence){
    string ret;
    if(sentence.size()<3) return "-1";

    char c = sentence[1];   //더미문자
    bool ok = 0;

    //BxBxB
    for(int i=0; i<sentence.size(); i++){
        if(islower(sentence[i])) ok=1;  //더미문자 있는 지 check
        if(i%2==0){ //더미문자 아닐때 == 대문자
            if(islower(sentence[i])) return "-1";
            ret+=sentence[i];
        }
        else{   //더미문자가 다 같은지 check
            if(c!=sentence[i]) return "-1";
        }
    }

    if(!ok) return "-1";
    return ret;
}

//대문자만 뽑아서 return, 소문자 나오면 바로 return
// XXXX 대문자 형태인지 check
string allUpper(string sentence){
    string ret;
    for(auto c : sentence){
        if(!isupper(c)) return "-1";
        ret+=c;
    }
    return ret;
}

string solution(string sentence) {
    vector<bool> used(26,0); //a~z 자리
    string answer = "";
    int it = 0;


    while(!sentence.empty()){
        string ret;         //정답 저장 변수
        vector<int> pos;    //확인된 문자 위치 체크하기 위해서 저장. 내가 검사한 소문자 위치

        //1. sentence[0]이 소문자인 경우 aBBa aBxBxBa
        if(islower(sentence[0])){
            if(used[sentence[0]-'a']==1) return "invalid"; //이미 사용한 소문자라면 invalid
            used[sentence[0]-'a'] = 1;  //현재 소문자(특수문자) 사용했음 표시

            for(int i=0; i<sentence.size(); i++){   //0번째 특수문자랑 같은 문자가 2개 있는 지 check
                if(sentence[i] == sentence[0])
                    pos.push_back(i);   //특수문자 위치 저장
            }

            if(pos.size()!=2) return "invalid"; // 2개가 아니면 invalid

            //가운데 문자열만 check 
            //kXXXXk  or kBcBcBk 인지 확인
            string center = sentence.substr(1, pos.back()-1);
            if(center=="") return "invalid";    //빈문자열이면 문자가 없는거니깐 return;
            
            //kBcBcBk
            ret = rule1(center);    //rule1을 만족하는 지 check 
            string target;
            if(ret == "-1"){    // rule1을 만족하지 않을 때 
                ret = allUpper(center); // BBB인건지 체크
                if(ret=="-1") return "invalid";
            }
            else{ //rule1 만족 kBcBcBk 
                 //한번 쓰인 소문자는 다시 쓰일 수 없다.
                //규칙1 만족 문자열 내부 특수문자가 이미 쓰인 더미 문자면 invalid
                if(used[sentence[2]-'a'])  return "invalid";
                used[sentence[2]-'a'] = 1;    
            }
            //다음 검사할 문장을 확인된 부분까지 제거하고 업데이트
            sentence = sentence.substr(pos.back()+1);
        }
        //2. sentenct[0]이 대문자인 경우
        
        //BxBxB / BxBxBxB  / BBBB / SpIpGpOpNp    G JqOqA
        else{
            // case1. BBBB BB -> sentence[0], [1] 모두 쭉 대문자 
            if(sentence.size() == 1 || isupper(sentence[1])){
                ret = sentence[0];  //answer에 추가
                sentence = sentence.substr(1);  //이후 검사할 문자열 업데이트, 다음에 check
            }
            // case2. BxBx -> sentence[1]이 소문자 
            // -> 문장 길이별로 케이스 분류하여 체크
            else{
                //소문자 모두 push, 마지막 소문자 위치 저장
                for(int i=0; i<sentence.size(); i++){
                    if(sentence[1] == sentence[i])
                        pos.push_back(i);
                }
                // BxC / BxBxBxBxB 형태 -> 일반적인 rule1 글자 사이사이 마다 소문자 넣는 형태
                if(pos.size()!=2){
                    if(pos.back() == sentence.size()-1) return "invalid";   //맨 마지막 특수문자 위치가, 문장의 마지막 위치가 아닐때 BxBxBxBx
                    if(islower(sentence[pos.back()+1])) return "invalid";   //맨 마지막 문자가 대문자가 아니라면 return BxBxBxBxb

                    string center = sentence.substr(0,pos.back()+1);
                    ret=rule1(center);

                    if(ret=="-1") return "invalid";
                    if(used[sentence[1]-'a']) return "invalid";
                    used[sentence[1]-'a'] = 1;

                    sentence = sentence.substr(pos.back()+2);    
                }

                //BxDDxB / AxDDDDDxC(규칙2) 특정 단어의 앞 뒤에 같은 소문자 끼워넣기
                else{
                    ret = sentence[0];
                    sentence = sentence.substr(1);
                }
            }
        }


        answer += ret + " ";
    }

    answer.pop_back();
    return answer;
}

int main(){

    //특정 단어를 선택하여 글자 사이마다 같은 기호를 넣는다.
    //특정 단어를 선택하여 단어 앞뒤에 같은 기호를 넣는다.
    //원래 문구에 있던 공백을 제거한다.

    
    cout << solution("BxBxBxBxb");
    



    return 0;
}