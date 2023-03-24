import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class HE12738 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine()); // 수열의 크기. 1 <= N <= 1_000_000
		// N+1을 하는 이유는 가장 작은 값이 여러번 나올 때 길이를 1로 설정해주는 과정을 편하게 하기 위해
		// nums, min 모두 0을 추가해주었다.
		int[] nums = new int[N+1]; 
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 1; i <= N; i++) nums[i] = Integer.parseInt(st.nextToken());
		
		// min 배열 : min[i] = i 길이의 최장 부분 수열에서 마지막 수가 가장 작은 수열의 마지막 수.
		// ex) [1, 2] 랑 [1, 3]은 둘 다 길이기 2이지만, [1, 2] 마지막 수가 더 작기 때문에,
		// 2보다 큰 수가 나왔을 때 [1, 2, x]를 만들면 되므로 가장 작은 마지막 수를 저장하려고 하는 것이다.
		int[] min = new int[N+1];
		// 해당 길이의 마지막 수가 작은지 비교하기 위해 MAX값을 넣는다.
		Arrays.fill(min, Integer.MAX_VALUE);

		// nums를 쭉 돌면서 DP, min을 완성시킨다.
		for(int i = 1; i <= N; i++) {
			// 이분 탐색으로 min 안에서 나보다 작은 값중 가장 큰 값을 찾아낸다.(lower bound)
			// x는 min의 idx 값이다.
			int low = 0;
			int high = N;
			int mid;
			
			while(low+1 < high) {
				mid = (low + high) / 2;
				// 현재 숫자보다 마지막 숫자가 크면 뒤는 자르고, 작다면 앞을 자른다.
				if (min[mid] >= nums[i]) high = mid;
				else low = mid;
			}
//			System.out.println(nums[i] + "보다 작은 숫자 중 가장 큰 숫자의 인덱스 low : " + low);
			if (min[low+1] > nums[i]) min[low+1] = nums[i];
		}
		
		// min을 뒤에서 돌면서 MAX가 아닌 최초의 idx(길이)를 출력한다.
		for(int i = N; i > 0; i--) {
			if (min[i] != Integer.MAX_VALUE) {
				System.out.println(i);
				break;
			}
		}
		
	}

}
