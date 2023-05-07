import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HE12100 {
	
	static int N;
	static int[][] init;
	static int answer;
	
	// 함수에 필요한 변수
	static int blank;
	static int[][] gap;
	static int[][] result;
	
	
	static int[][] upBlanks(int[][] board) {
		// 몇 칸 이동해야 하는지 위치별로 기록한다.
		gap = new int[N][N];
		// 이동한 결과를 반환한다.
		result = new int[N][N];
		
		// 빈칸의 개수를 센다 O(N^2)
		for (int c = 0; c < N; c++) {
			blank = 0;
			for (int r = 0; r < N; r++) {
				if (board[r][c] == 0) {
					blank++;
				} else {
					gap[r][c] = blank;
				}
			}
		}
		
		
		// 빈칸의 개수만큼 땡김 O(N^2)
		for (int c = 0; c < N; c++) {
			for (int r = N-1; r >= 0; r--) {
				if(board[r][c] > 0) {
					result[r-gap[r][c]][c] = board[r][c];
				}
			}
		}
		
		// 빈칸을 땡긴 보드
		return result;
	}
	
	static int[][] upCombine(int[][] board) {
		// 블록끼리 합침 O(N^2)
		for (int r = 0; r < N-1; r++) {
			for (int c = 0; c < N; c++) {
				if (board[r][c] == board[r+1][c]) {
					board[r][c] += board[r+1][c];
					board[r+1][c] = 0;
				}
			}
		}
		return board;
	}
	
	static int[][] downBlanks(int[][] board) {
		// 몇 칸 이동해야 하는지 위치별로 기록한다.
		gap = new int[N][N];
		// 이동한 결과를 반환한다.
		result = new int[N][N];
		
		// 빈칸의 개수를 센다 O(N^2)
		for (int c = 0; c < N; c++) {
			blank = 0;
			for (int r = N-1; r >= 0; r--) {
				if (board[r][c] == 0) {
					blank++;
				} else {
					gap[r][c] = blank;
				}
			}
		}
		

		// 빈칸의 개수만큼 땡김 O(N^2)
		for (int c = 0; c < N; c++) {
			for (int r = 0; r < N; r++) {
				if(board[r][c] > 0) {
					result[r+gap[r][c]][c] = board[r][c];
				}
			}
		}
		
		return result;
	}
	
	static int[][] downCombine(int[][] board) {
		// 블록끼리 합침 O(N^2)
		for (int c = 0; c < N; c++){
			for (int r = N-1; r > 0; r--) {
				if (board[r][c] == board[r-1][c]) {
					board[r][c] += board[r-1][c];
					board[r-1][c] = 0;
				}
			}
		}
		
		return board;
	}
	
	static int[][] rightBlanks(int[][] board) {
		// 몇 칸 이동해야 하는지 위치별로 기록한다.
		gap = new int[N][N];
		// 이동한 결과를 반환한다.
		result = new int[N][N];
		
		// 빈칸의 개수를 센다 O(N^2)
		for (int r = 0; r < N; r++) {
			blank = 0;
			for (int c = N-1; c >= 0; c--) {
				if (board[r][c] == 0) {
					blank++;
				} else {
					gap[r][c] = blank;
				}
			}
		}
		

		// 빈칸의 개수만큼 땡김 O(N^2)
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (board[r][c] > 0) {
					result[r][c+gap[r][c]] = board[r][c];
				}
			}
		}
		
		return result;
	}
	
	static int[][] rightCombine(int[][] board) {
		// 블록끼리 합침 O(N^2)
		for (int r = 0; r < N; r++){
			for (int c = N-1; c > 0; c--) {
				if (board[r][c] == board[r][c-1]) {
					board[r][c] += board[r][c-1];
					board[r][c-1] = 0;
				}
			}
		}
		
		return board;
	}
	
	static int[][] leftBlanks(int[][] board) {
		// 몇 칸 이동해야 하는지 위치별로 기록한다.
		gap = new int[N][N];
		// 이동한 결과를 반환한다.
		result = new int[N][N];
		
		// 빈칸의 개수를 센다 O(N^2)
		for (int r = 0; r < N; r++) {
			blank = 0;
			for (int c = 0; c < N; c++) {
				if (board[r][c] == 0) {
					blank++;
				} else {
					gap[r][c] = blank;
				}
			}
		}
		

		// 빈칸의 개수만큼 땡김 O(N^2)
		for (int r = 0; r < N; r++) {
			for (int c = N-1; c >= 0; c--) {
				if(board[r][c] > 0) {
					result[r][c-gap[r][c]] = board[r][c];
				}
			}
		}
		
		return result;
	}
	
	static int[][] leftCombine(int[][] board) {
		// 블록끼리 합침 O(N^2)
		for (int r = 0; r < N; r++){
			for (int c = 0; c < N-1; c++) {
				if (board[r][c] == board[r][c+1]) {
					board[r][c] += board[r][c+1];
					board[r][c+1] = 0;
				}
			}
		}
		
		return board;
	}
	

	
	static int getMaxBlock(int[][] board) {
		int max = 0;
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				max = Math.max(max, board[r][c]);
			}
		}
		return max;
	} 
	
	static void up(int step, int[][] board) {
		int[][] moved = upBlanks(board);
		moved = upCombine(moved);
		moved = upBlanks(moved);
		
		moving(step+1, moved);
	}
	
	static void down(int step, int[][] board) {
		int[][] moved = downBlanks(board);
		moved = downCombine(moved);
		moved = downBlanks(moved);

		moving(step+1, moved);
	}
	
	static void right(int step, int[][] board) {
		int[][] moved = rightBlanks(board);
		moved = rightCombine(moved);
		moved = rightBlanks(moved);

		moving(step+1, moved);
	}
	
	static void left(int step, int[][] board) {
		int[][] moved = leftBlanks(board);
		moved = leftCombine(moved);
		moved = leftBlanks(moved);

		moving(step+1, moved);
	}
	
	static void moving(int step, int[][] board) {
		// dfs 종료조건
		if(step == 5) {
			answer = Math.max(answer, getMaxBlock(board));
			return;
		}

		up(step, board);
		down(step, board);
		right(step, board);
		left(step, board);
	}
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		init = new int[N][N];
		
		// 입력 받기
		for(int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c = 0; c < N; c++) {
				init[r][c] = Integer.parseInt(st.nextToken());
			}
		}
		
		moving(0, init);
		
		System.out.println(answer);
	}

}