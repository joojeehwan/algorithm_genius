import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class HE1992 {
	static int N;
	static boolean[][] img;
	static StringBuilder sb;
	
	
	/** 해당 구역에 0과 1의 개수를 확인하여 판단
	 * @param r : 시작 행 위치
	 * @param c : 시작 열 위치
	 * @param l : 범위
	 * @return 0 (0만 있다), 1 (1만 있다), 2 (둘 다 있다)
	 */
	static int check(int r, int c, int l) {
		int zeroCnt = 0;
		int oneCnt = 0;
		
		for(int dr = 0; dr < l; dr++) {
			for(int dc = 0; dc < l; dc++) {
				// 해당 위치에서 true = 1, false = 0
				if (img[r+dr][c+dc]) oneCnt++;
				else zeroCnt++;
			}
		}
		if (zeroCnt == l*l) return 0;
		if (oneCnt == l*l) return 1;
		return 2;
	}
	
	
	/** 4등분 하는 함수. check의 결과에 따라 1 또는 0 추가
	 * 아니라면 다시 4등분(재귀)
	 * @param r : 현재 행
	 * @param c : 현재 열
	 * @param l : 현재 길이
	 */
	static void quater(int r, int c, int l) {
		// 지금 보는 범위가 1 또는 0 으로만 이루어져 있는지 확인한다.
		int result = check(r, c, l);
		
		if (result == 1) {
			sb.append("1");
			return;
		}
		
		if (result == 0) {
			sb.append("0");
			return;
		}
		
		// 1과 0이 혼합된 상태
		int half = l / 2;
		sb.append("(");
		for (int dr = 0; dr < 2; dr++) {
			for (int dc = 0; dc < 2; dc++) {
				quater(r + dr * half, c + dc * half, half);
			}
		}
		sb.append(")");
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		// sb = 정답이 될 문자열. String을 매번 생성하면 메모리 낭비
		sb = new StringBuilder();
		// 0,1로 이루어진 이미지를 boolean 2차원 배열로 저장한다.
		img = new boolean[N][N];
		
		for(int r = 0; r < N; r++) {
			char[] row = br.readLine().toCharArray();
			for(int c = 0; c < N; c++) {
				img[r][c] = row[c] == '1' ? true : false;
			}
		}
		// 분할 정복 시작
		quater(0, 0, N);
		
		System.out.println(sb.toString());
	}

}
