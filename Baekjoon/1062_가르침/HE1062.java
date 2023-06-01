import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HE1062 {
	static int answer = 0;
	static int N, K;
	static String[] words;
	static boolean[] learned;
	
	/**
	 * 알파벳 조합을 만들어 몇개의 단어를 읽을 수 있는지 확인하는 함수
	 * @param cnt : 몇 개의 알파벳을 배웠는가
	 * 
	 * @param alpha : 몇 번째 알파벳 까지 봤는가
	 */
	static void makeAlphaComb(int cnt, int alpha) {
		// 정해진 개수만큼 다 배웠다. (acint 제외)
		// 1번째 백트랙킹
		if (cnt == K-5) {
			// 이번 알파벳 조합으로 읽을 수 있는 단어의 수
			int wordsCnt = 0;
			
			for (String word : words) {
				// 해당 단어를 읽을 수 있는가?
				boolean possible = true;
				
				for(int c = 0; c < word.length(); c++) {
					if (!learned[word.charAt(c) - 'a']) {
						possible = false;
						break;
					}
				}
				
				if (possible) wordsCnt++;
			}
			answer = Math.max(answer, wordsCnt);
			return;
		}
		
		// 알파벳 조합을 만들어본다.
		// 2번째 백트랙킹 : 이전 알파벳으로 돌아갈 이유가 있을까? 
		// 아니, 우리는 조합을 보고있잖아. '순서'는 중요하지 않아.
		for(int idx = alpha; idx < 26; idx++) {
			// 해당 알파벳을 이미 배웠다면 넘어간다.
			if (learned[idx]) continue;
			
			// 안 배웠다면 배워본다.
			learned[idx] = true;
			makeAlphaComb(cnt+1, idx);
			// 다른 조합을 위해 false 처리를 진행한다.
			learned[idx] = false;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		// 특수한 경우 미리 처리
		if (K < 5) {
			// 기본으로 필요한 알파벳 acint 때문에 5개 미만이면 아무것도 읽을 수 없음
			System.out.println(0);
			return;
		}
		if (K == 26) {
			// 모든 알파벳을 배울 수 있다면 전부 읽을 수 있음
			System.out.println(N);
			return;
		}
		
		// 입력된 N개의 단어들
		words = new String[N];
		
		for(int i = 0; i < N; i++) {
			String input = br.readLine();
			// 3번째 백트랙킹 : 'anta' 와 'tica' 제거
			words[i] = input.substring(4, input.length()-4);
		}
		
		// 해당 알파벳을 배웠는지 표시
		learned = new boolean[26];
		// a c i n t
		learned['a' - 'a'] = true;
		learned['c' - 'a'] = true;
		learned['i' - 'a'] = true;
		learned['n' - 'a'] = true;
		learned['t' - 'a'] = true;
		
		makeAlphaComb(0, 0);
		
		System.out.println(answer);
	}

}
