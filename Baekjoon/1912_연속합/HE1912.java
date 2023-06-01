/*
 * 투포인터인줄 알았는데, DP였음
 * 투포인터는 배열 안에서 합, 차가 '특정 값'이 되는 서브배열 찾을 때. (배열 정렬)
 * DP는 문제를 작은 문제로 나누어 푸는 방식. DP 중 카데인 알고리즘 사용 
 * (합이 음수가 되었을 때에만 현재부터 다시 센다. 왜냐면 음수면 뒤에 뭘 더하든 계속 안더하는것보다 적은 값이 나오기 때문이다.)
 * '연속된 서브 배열의 최대 합을 찾는 문제' -> '현재까지 최대 서브 배열 합'이란 문제로 나누고, 이를 누적해서 사용한다.
 * */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HE1912 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] num = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i = 0; i < N; i++) {
			num[i] = Integer.parseInt(st.nextToken());
		}
		
		int answer = num[0];
		int now = num[0];
		
		for(int i = 1; i < N; i++) {
			// now + num[i] : 현재 원소를 포함한 부분 배열의 합
			// 만약 now + num[i]가 음수라면, 초기화를 하는게 낫다. 이때 0으로 설정하는게 아니다.
			// 현재 위치부터 다시 합한다고 생각하고, 현재 위치의 값부터 시작한다.
			// num[i]: 현재 원소를 새로운 시작으로 한다 (이전 까지의 부분 배열 버림) 
			now = Math.max(now + num[i], num[i]);
			answer = Math.max(answer, now);
		}
		
		System.out.println(answer);
	}

}
