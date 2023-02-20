/*
 * 참고 : https://comdoc.tistory.com/entry/%EB%AF%B8%EB%A1%9C-%ED%83%88%EC%B6%9C-%EB%AA%85%EB%A0%B9%EC%96%B4
 * */


class Solution {
	// 아래, 왼쪽, 오른쪽, 위쪽 방향으로 만든다.
    int[] dr = {1, 0, 0, -1};
    int[] dc = {0, -1, 1, 0};
    String[] dir = {"d", "l", "r", "u"};
    
    // dfs 함수에서 필요한 변수때문에 전역변수로 저장했다.
    int N, M, R, C, K;
    String answer;
    String impossible;
    
    public void dfs(int row, int col, String route) {
    	// 길이를 초과했으면 그만 봐라.
        if(route.length() > K) return;
        // 못 찾아낸 시간초과 해결 조건 1
        // 현재 갈 수 있는 길이보다, 현재 위치에서 도착 지점까지의 길이가 더 멀다면 의미 없다.
        if(K-route.length() < Math.abs(row-R) + Math.abs(col-C)) return;
        // 못 찾아낸 시간초과 해결 조건 2
        // 같은 곳을 지나기 위해선 왔다, 갔다 즉 2번의 이동이 필요하다.
        // 도착지점까지 남은 거리와, 현재 갈 수 있는 거리의 홀짝이 안맞는다는건 결국 극복할 수 없는 차이가 있다는 뜻이다.
        // 만약 지금 5칸을 움직일 수 있고, 정답까지 3칸이 남았다면 한번 왔다 갔다 하면서 정답에 도달할 수 있다.
        // 하지만 예시3 처럼 3칸, 5칸 .. 으로 도달할 수 있는 거리를 4칸으로 가라고 하면 갈 수 없는 것이다.
        if(((K-route.length()) % 2) != ((Math.abs(row-R) + Math.abs(col-C)) % 2)) return;
        
        // 정답을 찾은 경우
        if(route.length() == K && row == R && col == C) {
            if(route.compareTo(answer) < 0) answer = route;
            return;
        }
        
        for(int d = 0; d < 4; d++) {
            int nRow = row + dr[d];
            int nCol = col + dc[d];
            if(!(0 < nRow && nRow <= N && 0 < nCol && nCol <= M)) continue;
            dfs(nRow, nCol, route+dir[d]);
            // 정답을 한번이라도 찾았다면, 그 뒤는 볼 필요가 없다.(사전 순으로 진행하기 때문에)
            if (!answer.equals(impossible)) return;
        }
    }
    
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
    	// dlru 보다 무조건 사전 순이 뒤인 z로 문자열 생성
        impossible = "z".repeat(k);
        answer = impossible;
        N = n;
        M = m;
        R = r;
        C = c;
        K = k;
        
        dfs(x, y, "");
        
        if(answer.equals(impossible)) answer = "impossible";
        
        return answer;
    }
}


// 이 사람 풀이 엄청 깔끔함!
class Janghongbeom {
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
    	
    	// 불가능한 경우는 처음에 바로 확인이 가능한 것이다.
    	// 이 조건을 만족했다면 일단 갈 수는 있다.
    	// x+y+r+c 조건은 좀 헷갈리는데, (1,1)에서 S, E까지의 거리와 K를 비교한다고 생각했다.
    	// 또는 가야할 거리가 갈 수 있는 거리보다 먼 경우
        if ((x + y + r + c) % 2 != k % 2 || Math.abs(r - x) + Math.abs(c - y) > k)
            return "impossible";

        StringBuilder sb = new StringBuilder();

        // d -> l -> r -> u
        // 아래부터 사전순대로 움직인다. 갈 수 있는 조건을 계속 확인해주고 있다.. 이게 되네?
        // 홀짝은 한번만 보면 되고, 남은 거리 비교는 계속 해주면 되나보다...
        while (k-- > 0) {

            int downX = x + 1, leftY = y - 1, rightY = y + 1, upX = x - 1;

            if (downX <= n && Math.abs(r - downX) + Math.abs(c - y) <= k) {
                // [1] down 가능?
                sb.append('d');
                x = downX;
            } else if (leftY > 0 && Math.abs(r - x) + Math.abs(c - leftY) <= k) {
                // [2] left 가능?
                sb.append('l');
                y = leftY;
            } else if (rightY <= m && Math.abs(r - x) + Math.abs(c - rightY) <= k) {
                // [3] right 가능?
                sb.append('r');
                y = rightY;
            } else if (upX > 0 && Math.abs(r - upX) + Math.abs(c - y) <= k) {
                // [4] up 가능?
                sb.append('u');
                x = upX;
            }

        }

        return sb.toString();
    }
}