#include <bits/stdc++.h>

using namespace std;

int N, M;
int card[500000];   //몇번째에 상근이가 원하는 카드가 있는 지 구하기 위해

int lowerBound(int x){

	int first = 0, last = N-1, mid;

	while(true){
		mid = (first+last) / 2;

        //while문 종료조건
		if (first > last){
            // first위치에 x가 있으면 first 위치 반환
			if (card[first] == x) return first;
            // 못찾으면 -1
			else return -1;
		}

        //x가 mid위치의 값보다 작으면 왼쪽에 있는거니
        //last = mid-1로 범위 변경
		if (x <= card[mid]) last = mid - 1;

        //오른쪽에 있는거면 first = mid+1로 범위 변경
		else first = mid + 1;
	}
}

int upperBound(int num){

	int first = 0, last = N-1, mid;

	while(true){
		mid = (first+last) / 2;
        
		if (first > last){
			if (card[last] == num) return last;
			else return -1;
		}

		if (card[mid] <= num) first = mid + 1;
		else last = mid - 1;
	}
}

int main(void)
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> card[i];
	
    //이분탐색을 위해 정렬
    sort(card, card + N);

	cin >> M; int num;
	for (int i = 0; i < M; i++){
		cin >> num;
        //num을 초과하는 num 바로 다음 숫자 위친
		int ret = upperBound(num);  

		if (ret == -1) cout << "0 ";
		else cout << ret - lowerBound(num) + 1 << " ";
	}

	return 0;
}