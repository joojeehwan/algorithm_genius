/*
 * 뭐랄까 킹받음 그 자체
 * */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class HE17298 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] comb = new int[N];
		int[] answer = new int[N];
		
		Arrays.fill(answer, -1); // 자바는 배열 초기화 해주려면 Arrays를 불러와야한다^^
		LinkedList<Integer> stack = new LinkedList<>();
		
		for(int i=0; i<N; i++) {
			// 수열 저장 중
			comb[i] = Integer.parseInt(st.nextToken());
		}
		
		for(int i=0; i<N; i++) {
			while(!stack.isEmpty() && comb[stack.peekLast()] < comb[i]) {
				// 지금 나보다 작은 애들 다 뽑자!
				answer[stack.pollLast()] = comb[i];
			}
			stack.add(i); // 순서를 넣어주고 있다. 순서 그 자체를 스택에 넣다니..
		}
		
		for(int i=0; i<N; i++) {
			sb.append(answer[i] + " ");
		}
		System.out.println(sb.toString());

	}

}
