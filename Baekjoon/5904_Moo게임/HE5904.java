import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class HE5904 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		// N의 최대값이 10^9 이다. S(K)의 길이는 2*S(K-1) + 1 + (K+2)로 늘어난다.
		// 아주 대충 2배씩 늘어난다 치면 3 * 2^?? = 10^9로 치고, ??의 값을 찾으면 된다.
		// 10^9 = 2^9 * 5^9(8^9보다 작다)이므로 2^36보다 훨씬 작다.
		// 그래서 S를 넉넉잡아 40길이로 만들고 계산해보면 Integer의 범위를 감안해 29 길이의 int 배열로 만들면 된다.
		// 29길이를 찾아낸 것은 직접 S 배열의 값을 출력해보고 나서 알았다.
		int[] S = new int[28];
		S[0] = 3;
		for(int i = 1; i < 28; i++) {
			S[i] = S[i-1] * 2 + (i+3);
		}
//		System.out.println(Arrays.toString(S));
		
		// 어느 K 인지 찾아낸다.
		int K = 0;
		for(int i = 0; i < 28; i++) {
			if (S[i] >= N) {
				// N보다 큰 순간, N까지 커버하는 K값이 된다.
				K = i;
				break;
			} 
		}
		
		// K를 줄여나가며 찾는다. K = 0이면 "moo" 에서 찾는거니까.
		// 그래서 N이 3보다 작다면 이 while문 안에 들어가지도 않는다.
		while(K > 0) {
//			System.out.println("현재 K는 = " + K + ", N은 = " + N + ", 앞 : 0 ~ " + S[K-1] + ", 뒤 : " + (S[K] - S[K-1]) + " ~ " + S[K]);
			if (S[K-1] >= N) K--;
			else if (S[K]- S[K-1] < N) {
				K--;
				N -= (S[K+1] - S[K]);
				// N이 뒤의 S(K-1)에 포함되는 경우, 앞 S(K-1)과 중간 문자열까지의 길이를 빼야
				// 정상적으로 계산이 가능하다. 이해 안되면 지우고 돌려보면 됨.
			}
			else {
				// 중간 문자열인 경우, 앞의 S(K-1)의 바로 뒤인 경우에만 m이다.
				if(S[K-1] +1 == N) System.out.println("m");
				else System.out.println("o");
				// break했더니 밑에 출력문이 진행되어서 return으로 바꿨다.
				return;
			}
		}
		// S(0) 까지 내려온 경우.
		System.out.println("moo".charAt(N-1));

	}

}
