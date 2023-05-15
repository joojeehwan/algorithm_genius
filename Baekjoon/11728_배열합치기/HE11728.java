import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class HE11728 {
	
	public static void divideConquer() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] A = new int[N];
		int[] B = new int[M];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < M; i++) {
			B[i] = Integer.parseInt(st.nextToken());
		}
		
		int a = 0;
		int b = 0;
		
		while(a < N && b < M) {
			if (A[a] < B[b]) {
				sb.append(A[a] + " ");
				a++;
			} else {
				sb.append(B[b] + " ");
				b++;
			}
		}
		
		while (a < N) {
			sb.append(A[a] + " ");
			a++;
		}
		
		while (b < M) {
			sb.append(B[b] + " ");
			b++;
		}
		
		sb.deleteCharAt(sb.length()-1);
		
		System.out.println(sb.toString());
	}

	public static void main(String[] args) throws IOException {
//		divideConquer();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] combine = new int[N+M];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) {
			combine[i] = Integer.parseInt(st.nextToken());
		}
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < M; i++) {
			combine[i+N] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(combine);
		
		for(int i = 0; i < N+M; i++) {
			sb.append(combine[i] + " ");
		}
		
		sb.deleteCharAt(sb.length()-1);
		
		System.out.println(sb.toString());
	}

}