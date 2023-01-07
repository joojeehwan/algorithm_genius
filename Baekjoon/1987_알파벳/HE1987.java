/*
 * 2번의 수정을 거치며 각각 시간, 메모리를 절약하였음
 * 1. visited 2차원 배열 + 알파벳 사용 확인용 HashMap 사용하였으나,
 * visited 1차원 배열의 index를 알파벳으로 활용하여(알파벳 - 'A') 압축할 수 있었다.
 * 2840ms -> 1128ms
 * 2. 지금 알파벳이 무엇인지 확인하고 인덱스를 미리 변수에 빼놨는데, 메모리를 상당히 잡아먹은 것 같다.
 * 심지어 String은 필요하지도 않은데 계속 생성하고 있었다.
 * 292200KB -> 12576 KB로 메모리를 절약했다. 
 * 아무래도 Java는 변수를 따로 생성할 경우 메모리 관리가 더 어려운것 같다.
 * */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HE1987 {
	
	static int row, col;
	static char[][] board;
	static boolean[] visited; // 어차피 알파벳당 한번씩이니까, 2차원 배열로 볼 필요가 없다.
	static int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
	static int answer = 1;
	
	static void DFS(int r, int c, int cnt) {
		visited[board[r][c] - 'A'] = true;
		if(answer < cnt) {
			answer = cnt;
		}
		
		for(int d = 0; d < 4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];
			
			// 1. 범위를 넘어가는지
			if(0 > nr || row <= nr || 0 > nc || col <= nc) continue;

			// 2. 이미 방문했는지
			if(visited[board[nr][nc] - 'A']) continue;
			
			// 여기로 간다.
			DFS(nr, nc, cnt+1);
			
			// 나왔다.
			visited[board[nr][nc] - 'A'] = false;
		}
	}
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		row = Integer.parseInt(st.nextToken());
		col = Integer.parseInt(st.nextToken());
		board = new char[row][col];
		visited = new boolean[26];
		
		// 입력 초기화
		for(int i = 0; i < row; i++) {
			char[] line = br.readLine().toCharArray();
			for(int j = 0; j < col; j++) {
				board[i][j] = line[j];
			}
		}
		
		DFS(0, 0, 1);
		
		System.out.println(answer);
	}

}
