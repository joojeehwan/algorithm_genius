import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HE16987 {
	static int N;
	static int answer = 0;
	static int[] durability;
	static int[] weight;
	
	static void dfs(int idx, int[] eggs) {
		// 틀린이유 1 ) 종료조건을 idx == N-1로함.. 당연히 가장 오른쪽 계란으로 못 쳐보잖아;
		if (idx == N) {
			int broken = 0;
			for(int egg : eggs) {
				if(egg <= 0) broken++;
			}
			answer = Math.max(answer, broken);
			return;
		}
		// 든 계란이 깨진 경우, 그냥 넘어가야한다.
		if(eggs[idx] <= 0)  {
			dfs(idx+1, eggs);
		} else {
			for(int i = 0; i < N; i++) {
				if(idx == i) continue;  // 자기 자신을 깰 수는 없다.
				boolean broke = false;
				if(eggs[i] > 0) {
					// 두 계란을 깨트린다.
					eggs[i] -= weight[idx];
					eggs[idx] -= weight[i];
					broke = true;
				}
				dfs(idx+1, eggs);
				if(broke) {
					// 다음 계산을 위해 원상복구 시킨다.
					eggs[i] += weight[idx];
					eggs[idx] += weight[i];
				}
			}
		}
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine()); // 계란의 갯수
		durability = new int[N];
		weight = new int[N];
		
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			durability[i] = Integer.parseInt(st.nextToken());
			weight[i] = Integer.parseInt(st.nextToken());
		}
		
		
		dfs(0, durability);
		System.out.println(answer);
	}

}
