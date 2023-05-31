/* 비트마스킹 116ms VS 일반 백트랙킹 224ms
 * */
 
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HE1062_비트마스킹 {
	static int N, K, answer;
	static int[] words;
	// 알파벳 사용 현황
//	static boolean[] selected;
	
	// 알파벳의 조합 => 부분 집합 => 비트 마스킹
	// 삽입 A | 1 << N
	// 조회 A & B == B (B에 있는 모든 원소가 A에 있다. 원래는 각 자리마다 둘다 1인지 비교함)
	// 그렇다면 (a, b, c) 조합은 1 << 0, 1 << 1, 1 << 2 이다.
	// 조합은 똑같이 backtracking으로 만들고, 점검할 때 비트 마스킹 활용 가능
	static void combination(int cnt, int idx, int combi) {
		if (cnt == K-5) {
			int wordCnt = 0;
			
			for (int word : words) {
				if ((word & combi) == word) wordCnt++;
			}
			
			answer = Math.max(answer, wordCnt);
			return;
		}
		
		for(int i = idx; i < 26; i++) {
			if ((combi & (1 << i)) == (1 << i)) continue;
			// i번 째 알파벳 삽입
			combi |= 1 << i;
			// i+1 대신 idx를 넣음으로써 idx 백트랙킹 전혀 사용 X
			// 변수명 더 제대로 짓자...
			combination(cnt+1, i+1, combi);
			// i번 째 알파벳 제거
			combi &= ~(1 << i);
		}
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		// 계산을 하지 않는 특수한 경우
		if (K < 5) {
			System.out.println(0);
			return;
		}
		if (K == 26) {
			System.out.println(N);
			return;
		}
		
		words = new int[N];
		
		for(int i = 0; i < N; i++) {
			String word = br.readLine();
			// 접두어, 접미어 제거
			word = word.substring(4, word.length()-4);
			
			int wordBinary = 0;
			for(char alphabet : word.toCharArray()) {
				wordBinary |= 1 << (alphabet - 'a');
			}
			
			words[i] = wordBinary;
		}
		
		// 접두어와 접미어에 있는 {a, c, i, n, t} 를 포함한다.
		int comb = 0;
		
		comb |= 1 << ('a' - 'a');
		comb |= 1 << ('c' - 'a');
		comb |= 1 << ('i' - 'a');
		comb |= 1 << ('n' - 'a');
		comb |= 1 << ('t' - 'a');
		
		answer = 0;
		combination(0, 0, comb);
		System.out.println(answer);
	}

}
