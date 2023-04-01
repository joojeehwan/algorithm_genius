import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HE12865 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken()); // 1 <= 물품의 수 <= 100
		int K = Integer.parseInt(st.nextToken()); // 1 <= 버틸 수 있는 무게 <= 100_000
		int[] W = new int[N+1]; // 1 <= 물건의 무게 <= 100_000
		int[] V = new int[N+1]; // 0 <= 물건의 가치 <= 1000
		
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			W[i] = Integer.parseInt(st.nextToken());
			V[i] = Integer.parseInt(st.nextToken());
		}
		
		// 정답 => 배낭에 넣을 수 있는 물건들의 가치의 최댓값
		// DP배열을 어떻게 만들어야 할까?
		// 물건 중복 선택 방지를 위한 하나의 인덱스가 더 필요하다.
		// (해당 번호까지의 물건을 고려했을 때) + (무게당 최대 가치)
		int[][] DP = new int[N+1][K+1];

		
		// N개의 물건을 하나씩 보면서
		// 조합할 물건의 전체 무게가 K보다 작거나 같고, 현재 선택한 무게보다 크거나 같을 수 있다.
		// K에서부터 보며 내려가는 이유는 
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= K; j++) {
				// i번째 물건의 무게를 담을 수 없는 경우, 이전 값을 가져온다.
				if (W[i] > j) DP[i][j] = DP[i-1][j];
				// 넣을 수 있는 경우,
				// i-1 번째 물건을 봤을때 j일때 최대 가치와 (이전 값)
				// i 번째 물건의 무게와 j 에서 그 무게를 빼고 i 직전까지의 물건을 본 상황과 비교
				else DP[i][j] = Math.max(DP[i-1][j], DP[i-1][j-W[i]] + V[i]);
			}
		}
		
		System.out.println(DP[N][K]); // 모든 물건을 다 고려했을 때 K일때 최대 가치
	}

}