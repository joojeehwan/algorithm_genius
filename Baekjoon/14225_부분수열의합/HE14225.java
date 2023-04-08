import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


/* 96ms, 13496KB
 * https://velog.io/@abc5259/%EB%B0%B1%EC%A4%80-14225-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9-JAVA
 * DFS로 풀고싶으면 해당 숫자를 고르는 경우와, 고르지 않는 경우를 둘 다 DFS로 돌아주면 된다.
 * */


public class HE14225_DFS {
	static int N;
	static int[] num;
	static boolean[] exist;
	
	public static void dfs(int idx, int sum) {
		if (idx == N) exist[sum] = true;
		else {
			// 완전 탐색
			dfs(idx+1, sum + num[idx]);
			dfs(idx+1, sum);
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		num = new int[N];
		exist = new boolean[20*100000+1];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) num[i] = Integer.parseInt(st.nextToken());
		
		dfs(0, 0);
		
		for(int i = 1; i < 20*100000+1; i++) {
			if (!exist[i]) {
				System.out.println(i);
				break;
			}
		}
	}

}


/*
 * 196ms , 14216KB
 * https://colin-sh.tistory.com/49
 * 
 * 이 문제의 핵심은 부분순열을 만들어보는건데, DFS 또는 비트마스킹으로 가능하다.
 * 비트마스킹을 활용하면 부분 수열을 N의 수만큼 만들어서 (1 << N)
 * N의 idx만큼 회전하며 해당 숫자가 존재하는지 확인한다. (1 << idx)
 * */



public class HE14225_BitMask {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] num = new int[N];
		boolean[] possible = new boolean[20*100_000+1]; // 최대 숫자까지 존재하는지 여부
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) num[i] = Integer.parseInt(st.nextToken());
		
		// N의 부분 수열의 개수 = 1 << N
		// N = 3이면 000, 001, 010, 011, 100, 101, 110, 111
		for(int subPerm = 0; subPerm < (1 << N); subPerm++) {
			// 이번 부분 수열의 합으로 나오는 숫자
			int sum = 0;
			// idx = 입력 받은 수열의 index
			for (int idx = 0; idx < N; idx++) {
				// 지금 만든 부분 수열(subPerm)에, 어떤 숫자(num[idx])가 있는지 
				// 확인하고( & (1 << idx)) , 존재하는 숫자라면 합해주기 위함.
				if((subPerm & (1 << idx)) != 0) {
					sum += num[idx];
				}
			}
			possible[sum] = true;
		}
		
		// 1부터 보면서 어떤 숫자가 존재하지 않는지 찾아낸다.
		for(int i = 1; i < 20*100_000+1; i++) {
			if (!possible[i]) {
				System.out.println(i);
				break;
			}
		}
	}
}
