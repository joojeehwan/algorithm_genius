/*
 * https://velog.io/@aurora_97/%EB%B0%B1%EC%A4%80-2812%EB%B2%88-%ED%81%AC%EA%B2%8C-%EB%A7%8C%EB%93%A4%EA%B8%B0-Swift
 * */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class HE2812 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		String str = br.readLine();
		int[] input = new int[N];
		for(int i = 0; i < N; i++) {
			// String을 int 배열로 변환하는 방법
			input[i] = str.charAt(i) - '0';
		}
		
		// deque를 사용하는 방법
		LinkedList<Integer> stack = new LinkedList<Integer>();
		
		for(int num : input) {
			// 스택의 마지막 숫자가 지금 넣으려는 숫자보다 작으면 들어가있는거 다 뺀다.
			// 이제까지 뺀 개수가 K개를 넘으면 안되므로 제한을 건다.(다빼도 앞에 K개만 빼야한다)
			while(K > 0 && !stack.isEmpty() && stack.getLast() < num) {
				stack.removeLast();
				K -= 1;
			}
			stack.add(num);
		}
		
		for(int i = 0; i < K; i++) {
			// 앞의 숫자가 커서 뒤의 작은 숫자가 다 더해진 경우 다시 빼야한다.
			// 만약 앞에서 다 뺐다면 K가 0이라 이 과정은 넘어간다.
			stack.removeLast();
		}
		
		// 자바에서 int 배열 문자열로 바꾸는 방법. 정말 귀찮다.
		StringBuilder sb = new StringBuilder();
		for(int num : stack) {
			sb.append(num);
		}
		
		System.out.println(sb.toString());
	}

}
