/*
* 플로이드 와샬 알고리즘을 사용한다. 
* 지문을 읽고 플로이드 와샬을 생각해내는건 쉽지 않다고 생각한다.
* "A 선수는 B 선수를 항상 이깁니다" 라는 문장이 힌트이다.
* A-B, B-C의 결과를 알면 A-C의 결과를 알 수 있기 때문이다.
* 2차원 배열을 생성하여 가중치를 설정해주는 점도 그래프 탐색을 떠올릴 기준이 된다.
* https://github.com/joojeehwan/algorithm_genius/blob/master/Programmers/49191_%EC%88%9C%EC%9C%84/haeun_49191.py
* 이때의 나는 이걸 어떻게 생각해낸건지 모르겠다.
*/

public class HE49191 {


	class Solution {
	    public int solution(int n, int[][] results) {
	        int answer = 0;
	        int[][] match = new int[n+1][n+1];
	        
	        for(int i = 0; i < results.length; i++) {
	            int win = results[i][0];
	            int lose = results[i][1];
	            // match[i][j] => 1 : i가 j 이김. -1 : i가 j에게 짐 0 : 모름
	            match[win][lose] = 1;
	            match[lose][win] = -1;
	        }
	        
	        for(int k = 1; k < n+1; k++) {
	            for(int i = 1; i < n+1; i++) {
	                for (int j = 1; j < n+1; j++) {
	                    // k선수를 거쳐서 비교했을 때 i가 k를 이기고 k가 j를 이기면 i가 j를 이김
	                    if (match[i][k] == 1 && match[k][j] == 1) {
	                        match[i][j] = 1;
	                        match[j][i] = -1;
	                    }
	                    // k선수를 거쳐서 비교했을 때 i가 k에게 지고 k가 j에게 지면 i가 j에게 짐
	                    if (match[i][k] == -1 && match[k][j] == -1) {
	                        match[i][j] = -1;
	                        match[j][i] = 1;
	                    }
	                }
	            }
	        }
	        
	        // 한명씩 돌면서 0의 수가 1개면 순위 확정
	        for (int p = 1; p < n+1; p++) {
	            int zero = 0;
	            for (int q = 1; q < n+1; q++) {
	                if (q != p && match[p][q] == 0) {
	                    zero += 1;
	                }
	            }
	            if (zero == 0) answer += 1;
	        }
	        return answer;
	    }
	}
}
