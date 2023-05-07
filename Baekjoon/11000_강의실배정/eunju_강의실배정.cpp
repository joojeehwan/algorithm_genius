#include <bits/stdc++.h>

using namespace std;

int N;

// 필요한 강의실 갯수를 계산할 큐
// 끝나는 시간을 사용해서 강의실이 더 필요한 지 필요하지 않은 지 비교예정
priority_queue<int, vector<int>, greater<int> > pq;


int main(void){

    vector<pair<int,int>> classes;  // 강의를 저장할 벡터

	cin >> N;
	for (int i=0; i<N; i++){
        int a, b; cin >> a >> b;
		classes.push_back({a,b});   
	}


    //solve
    sort(classes.begin(), classes.end()); //시작시간 기준으로 오름차순 정렬
    
    //끝나는 시간, 시작시간
    //가장 빨리 끝나는 강의가 pop될 예정
    pq.push(classes[0].second); 
    

    //모든 강의실을 탐색하면서
    for(int i=1; i<N; i++){
        
        //현재 강의의 시작시간이 pq.top(가장 빨리 끝나는 강의)시간보다 빠르다면
        //강의가 겹치므로 강의실이 하나 더 필요
        if(classes[i].first < pq.top()){
            pq.push(classes[i].second);
        }

        // 강의가 겹치지 않는다면 
        // pq top의 강의실과 같은 강의실로 사용 가능
        // 가장 늦게 끝나는 강의 시간을 사용해서 이후 강의들을 비교해야하므로
        // top을 빼고 새로운 강의를 insert
        else{
            pq.pop();
            pq.push(classes[i].second);
        }
    }

    cout << pq.size()<<"\n";

	return 0;
}

