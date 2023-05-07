import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class HE10816 {

	static int N, M;
	static int[] cards, query;
	
	// 원하는 숫자의 가장 첫 번째 인덱스를 찾는다.
	public static int findLowerBound(int q) {

		// low와 high는 각각 idx가 된다.
		// mid 는 숫자를 볼 인덱스. 
		// cards[mid]값이 q와 같으면, high를 계속 낮춰간다.
		// 나를 포함하는 가장 왼쪽 idx => high
		// 나를 포함하지 않는 가장 오른쪽 idx => high
		
		int low = -1;
		int high = N-1;
		int mid;
		
		while (low + 1 < high) {
			mid = (low + high) / 2;
			
			if (cards[mid] < q) {
				low = mid;
			} else {
				high = mid;
			}
		}
		
//		System.out.println( q + " : 나를 포함하지 않는 가장 오른쪽 idx =" + low + " 나를 포함하는 가장 왼쪽 idx = " + high);
		if (cards[high] != q) return -1; 
		return high;
	}
	
	public static int findUpperBound(int q) {

		// low와 high는 각각 idx가 된다.
		// mid 는 숫자를 볼 인덱스. 
		// cards[mid]와 q가 같으면 low를 계속 올린다.
		// 나를 포함하는 가장 오른쪽 idx => low
		// 나를 포함하지 않는 가장 왼쪽 idx => high
		
		int low = 0;
		int high = N;
		int mid;
		
		while (low + 1 < high) {
			mid = (low + high) / 2;
			
			if (cards[mid] <= q) {
				low = mid;
			} else {
				high = mid;
			}
		}
		if (cards[low] != q) return -1; 
		return low;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		N = Integer.parseInt(br.readLine()); // 1 <= N <= 50만
		cards = new int[N]; // -천만 ~ 천만. 같은 수가 적힌 경우는 X
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) {
			cards[i] = Integer.parseInt(st.nextToken());
		}
		// 이분 탐색 하려면 정렬은 필수
		Arrays.sort(cards);
		
		M = Integer.parseInt(br.readLine()); // 1 <= M <= 50만
		query = new int[M]; // -천만 ~ 천만. 같은 수가 적힌 경우는 X
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < M; i++) {
			query[i] = Integer.parseInt(st.nextToken());
		}
		
		
		// 이분 탐색
		// O(M) * O(log2천만)
		// 아마 upper과 lower를 쓰라는 것 같다.
		// 그럼 upper 구하는거랑 lower 구하는거 각각 구현해야한다.
		for(int i = 0; i < M; i++) {
			int q = query[i];
			int lower = findLowerBound(q);
			int upper = findUpperBound(q);
			if (lower != -1 && upper != -1) {
				int cnt = upper - lower + 1;
				sb.append(cnt+ " ");
			} else {
				sb.append(0 + " ");
			}
		}
		
		System.out.println(sb.toString());
	}


}
