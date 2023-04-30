import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class HE2606 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		boolean[][] network = new boolean[N+1][N+1];
		boolean[] visited = new boolean[N+1];
		
		int M = Integer.parseInt(br.readLine());
		StringTokenizer st;
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			network[a][b] = true;
			network[b][a] = true;
		}
		
		int answer = 0;
		ArrayDeque<Integer> q = new ArrayDeque<Integer>();
		q.add(1);
		visited[1] = true;
		
		while(!q.isEmpty()) {
			int now = q.poll();
			
			for(int next = 1; next <= N; next++) {
				if (network[now][next] && !visited[next]) {
					visited[next] = true;
					answer +=1;
					q.add(next);
				}
			}
		}
		System.out.println(answer);
	}

}
