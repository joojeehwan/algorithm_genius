import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class HE2437 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int answer;
		int N = Integer.parseInt(br.readLine());
		int[] weights = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) weights[i] = Integer.parseInt(st.nextToken());
		// 정렬 O(logN)
		Arrays.sort(weights);
		
		// 누적합을 사용하라..
		// sum까지 무게를 측정할 수 있다.
		int sum = 0;
		// O(N)
		for(int i = 0; i < N; i++) {
			// 누적합의 1 다음보다 무게추가 더 크다면, 끝났다.
			// (현재 올리려는 저울추의 무게)가 (지금까지 올린 저울추의 총 합 + 1) 보다 커지는 순간 (저울추의 총 합 + 1)이 측정할 수 없는 최소값
			if (sum+1 < weights[i]) break;
			// 아니라면 계속 누적해서 더해간다.
			// 직접 숫자를 만드는게 아니라, 그 수까지는 다 만들 수 있다는걸 믿는 것이다.
			sum += weights[i];
		}
		
		System.out.println(sum+1);
	}
}

/*
 * 이 코드의 시간 복잡도는 O(NlogN) 입니다.
 * 정렬에는 Arrays.sort()를 사용하였으며, 이는 평균적으로 O(NlogN)의 시간 복잡도를 갖습니다.
 * 이후에는 O(N)의 반복문을 한번 돌며, 계속해서 누적합을 구하고 비교하면서 
 * 측정할 수 없는 최소값을 구하고 있습니다. 따라서 전체적인 시간 복잡도는 O(NlogN) 입니다.
 * */
