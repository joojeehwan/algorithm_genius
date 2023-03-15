/*
 * 공부하기 좋은 링크 : https://st-lab.tistory.com/281
 * - parameter값 설정까진 성공했으나, 구하는 계산식을 떠올리지 못 했다.
 * 약수의 개수를 찾을까 했는데, 그냥 나누면 되는 것이다.
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
		
		System.out.println(high);
	}

}
