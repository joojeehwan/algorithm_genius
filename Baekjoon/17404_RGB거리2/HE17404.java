/*
 * 3차원 배열로 만들었는데, 그냥 2차원 배열로 푸는거다.
 * 시작이 R, G, B일때의 경우를 나는 배열에 다 기록했고, 다른 풀이는 for문돌려서 계산했다.
 * 하.. 조건 그냥 조금만 추가해주면 되는게 맞았는데, 너무 시간을 허비했다. 허탈하다.
 * */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HE17404 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		int[][] cost = new int[N][3];
		for(int house = 0; house < N; house++) {
			st = new StringTokenizer(br.readLine());
			cost[house][0] = Integer.parseInt(st.nextToken());
			cost[house][1] = Integer.parseInt(st.nextToken());
			cost[house][2] = Integer.parseInt(st.nextToken());
		}
		
		int[][][] dp = new int[N][3][3];
		
		//초기화
		for(int startColor = 0; startColor < 3; startColor++) {
			dp[0][startColor][0] = cost[0][startColor];
			dp[0][startColor][1] = cost[0][startColor];
			dp[0][startColor][2] = cost[0][startColor];
			
			for(int nowColor = 0; nowColor < 3; nowColor++) {
				if(startColor == nowColor) dp[1][startColor][nowColor] = Integer.MAX_VALUE;
				else dp[1][startColor][nowColor] = cost[0][startColor] + cost[1][nowColor];
			}
		}
		
		// 계산
		for(int house = 2; house < N; house++) {
			for(int startColor = 0; startColor < 3; startColor++) {
				dp[house][startColor][0] = cost[house][0] + Math.min(dp[house-1][startColor][1], dp[house-1][startColor][2]);
				dp[house][startColor][1] = cost[house][1] + Math.min(dp[house-1][startColor][0], dp[house-1][startColor][2]);
				dp[house][startColor][2] = cost[house][2] + Math.min(dp[house-1][startColor][0], dp[house-1][startColor][1]);
			}
		}
		
		// 최종 결과
		int ans = Integer.MAX_VALUE;
		for(int startColor = 0; startColor < 3; startColor++) {
			for(int lastColor = 0; lastColor < 3; lastColor++) {
				if (startColor == lastColor) continue;
				ans = Math.min(ans, dp[N-1][startColor][lastColor]);
			}
		}
		
		System.out.println(ans);
	}

}
