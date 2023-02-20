import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class HE1976 {
	static int N, M;
	static int[][] connect;
	static int[] plan;
	static int[] parent;
	
	static int findSet(int a) {
		if(parent[a] == a) return a;
		parent[a] = findSet(parent[a]);
		return parent[a];
	}
	
	static void union(int a, int b) {
		int pa = findSet(a);
		int pb = findSet(b);

		parent[pb] = pa;
	}
	
	static boolean bfs(int start, int goal) {
		Queue<Integer> queue = new LinkedList<Integer>();
		boolean[] visited = new boolean[N];
		
		queue.add(start);
		visited[start] = true;
		
		while(!queue.isEmpty()) {
			int now = queue.poll();
			if (now == goal) return true;
			
			for(int next = 0; next < N; next++) {
				if (connect[now][next] == 1 && !visited[next]) {
					queue.add(next);
					visited[next] = true;
				}
			}
		}
		
		return false;
	}

	public static void main(String[] args) throws IOException {
		String answer = "YES";
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		connect = new int[N][N];
		plan = new int[M];
		parent = new int[N];
		
		for(int i = 0; i < N; i++) {
			parent[i] = i; // 스스로가 부모라고 설정해두기.
		}
		
		
		// 인접 행렬
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < N; j++) {
				connect[i][j] = Integer.parseInt(st.nextToken());
				if (connect[i][j] == 1) {
					union(i, j);
				}
			}
		}
		
		// 여행 계획
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < M; i++) {
			plan[i] = Integer.parseInt(st.nextToken()) - 1;
		}
		
		// 초기화 완료
		
		//BFS		
//		if(M > 1) {
//			// 2개씩 도시를 끊어서 본다.
//			for(int i = 0; i < M-1; i++) {
//				if (!bfs(plan[i], plan[i+1])) {
//					answer = "NO";
//					break;
//				}
//			}
//		}
		
		for(int i = 0; i < M-1; i++) {
			if(findSet(plan[i]) != findSet(plan[i+1])) {
				answer = "NO";
				break;
			}
		}
		System.out.println(answer);
	}
}



/* BFS가 통과는 하네..!
 * BFS => O(m*n²)
 * 유니온 파인드 => O(n²)
 * 
 * */
