/*
 * 공부하기 좋은 링크 : https://st-lab.tistory.com/281
 * - parameter값 설정까진 성공했으나, 구하는 계산식을 떠올리지 못 했다.
 * 	 약수의 개수를 찾을까 했는데, 그냥 나누면 되는 것이다.
 * - low가 정답일까, high가 정답일까? 
 * */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class HE1300 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int k = Integer.parseInt(br.readLine());
		
		long low = 1; // A와 B의 인덱스는 1부터 시작한다.
		long high = k;  // k까지만 찾고싶다.
		
		// low와 high가 경계를 두고 서있기 위해 1차이가 날때 끝난다.
		// 범위를 반씩 줄여나가는게 이분탐색이므로, 시간 복잡도는 O(logN)
		// high를 답으로 설정하는 이유는, mid가 K랑 같을 때 뒤는 잘라도 되지만 앞은 자르면 안되기 때문이다.
		while(low+1 < high) {
			long mid = (low + high) / 2;
			long idx = 0; // mid라는 수는 같거나 작은 수가 몇개인지 세기 위함
			
			for(long i = 1; i <= N; i++) {
				// mid/i 값이 N을 넘으면 안된다.(N=3인데 mid=5면 3개만 가능하다)
				idx += Math.min(mid/i, N);
			}
			
			// k보다 크거나 같으면 mid값을 낮춰보고, 적으면 mid값을 높여본다.
			if (idx >= k) high = mid;
			else low = mid;
		}
		// 시간 복잡도 = O(logN) * O(N) => O(NlogN)
		// 최악의 경우 : 10^5 * 16 => 1,600,000
		System.out.println(high);
	}

}

/* chatGPT의 시간 복잡도 답변
 * 이 코드의 시간 복잡도는 O(NlogN)입니다. 
 * 이분 탐색을 수행하는 동안, for 루프가 N번 실행되며 각각의 루프에서 Math.min() 함수도 호출됩니다. 
 * 이 루프에서 최대 k번까지 실행될 수 있습니다. 
 * 따라서 while 루프 내에서 실행되는 모든 작업의 총 시간 복잡도는 O(NklogN)이며, k는 N보다 작거나 같으므로 O(NlogN)이 됩니다.
 * */