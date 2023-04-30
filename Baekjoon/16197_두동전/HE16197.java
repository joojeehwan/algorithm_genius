/*
 * 셀프 피드백 : 쉬운 문제다. 더 빨리 풀어야한다. 그리고 조건 놓치지 말자.
 * */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HE16197 {
	
	static class Coin {
		int row;
		int col;
		
		public Coin(int _row, int _col) {
			this.row = _row;
			this.col = _col;
		}
	}
	
	static int ans = 11; // 정답(버튼을 누른 횟수. 10번을 넘어가면 안되므로 11은 될 수 없는 숫자다. 더 작을 때 업데이트 해주기 위해 11로 설정했다.)
	static int N, M; // 1 <= N, M <= 20
	static char[][] board; // 2차원 보드
	
	// 왼쪽, 오른쪽, 위, 아래에 맞춰 델타 배열 생성
	static int[] dr = {0, 0, -1, 1};
	static int[] dc = {-1, 1, 0, 0};
	
	// 코인
	static Coin coin1 = new Coin(-1, -1);
	static Coin coin2 = new Coin(-1, -1);
	
	/*
	 * 버튼 누른 대로 계산하는 함수.
	 * cnt는 버튼을 누른 횟수이다. (10번 초과하는지 체크)
	 * coin1, coin2의 값을 받는다.
	 * */
	static void dfs(int cnt, Coin c1, Coin c2) {
		// 기존에 찾은 답보다 크다면 넘어가도록 한다.(백트랙킹)
		if (cnt >= 10 || cnt > ans) return;
		
		for(int d = 0; d < 4; d++) {
			// 각 동전의 다음 위치를 찾는다.
			Coin nextC1 = new Coin(c1.row + dr[d], c1.col + dc[d]);
			Coin nextC2 = new Coin(c2.row + dr[d], c2.col + dc[d]);
			
			// 동전이 밖에 나갔는지 검사한다.
			boolean isOut1 = isOut(nextC1);
			boolean isOut2 = isOut(nextC2);
			
			// 동전 2개가 동시에 나가면 안된다.[조건]
			if(isOut1 && isOut2) continue;
			
			// 하나만 나간 경우(동시에 나간건 윗 줄에서 처리)
			if (isOut1 || isOut2) {
				if (ans > cnt) ans = cnt; // 정답보다 버튼을 적게 눌렀다면 업데이트한다.
			} else {
				// 둘다 보드 안에 있는 상황.
				// 각 동전이 가려는 위치가 벽인지 확인한다.ㄴ
				boolean isWall1 = isWall(nextC1);
				boolean isWall2 = isWall(nextC2);
				
				if (!isWall1 && !isWall2) dfs(cnt+1, nextC1, nextC2); // 두 동전 다 다음 위치가 벽이 아니라면 이동한다.
				else if (isWall1 && !isWall2) dfs(cnt+1, c1, nextC2); // 첫 번째가 벽에 막히면, 두 번째 동전만 이동한다.
				else if (!isWall1 && isWall2) dfs(cnt+1, nextC1, c2); // 두 번째가 벽에 막히면, 첫 번째 동전만 이동한다.
				// 두 동전 다 벽에 부딪히면 다른 방향으로 넘어간다.
			}
			
		}
	}
	
	/*
	 * 범위 밖인지 판단하는 함수
	 * */
	static boolean isOut(Coin c) {
		if (0 <= c.row && c.row < N && 0 <= c.col && c.col < M) return false;
		return true;
	}
	
	/*
	 * 벽인지 판단하는 함수
	 * */
	static boolean isWall(Coin c) {
		if (board[c.row][c.col] == '#') return true;
		return false;
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new char[N][M];
		
		for(int n = 0; n < N; n++) {
			char[] input = br.readLine().toCharArray();
			for(int m = 0; m < M; m++) {
				board[n][m] = input[m];
				if (input[m] == 'o') {
					// coin1을 이미 잧았다면 coin2의 값이다.
					// 아 구조 더 깔끔하게 안되려나...
					if (coin1.row == -1 && coin1.col == -1) {
						coin1.row = n;
						coin1.col = m;
					} else {
						coin2.row = n;
						coin2.col = m;
					}
					
				}
			}
		}
		dfs(0, coin1, coin2);
		
		if (ans == 11) System.out.println(-1);
		else System.out.println(ans+1);
		
	}

}
