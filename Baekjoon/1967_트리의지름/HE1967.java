
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class HE1967 {
	static int N;
	static ArrayList<ArrayList<Node>> list;
	
	static class Node {
		int num;
		int cost;
		
		public Node (int n, int c) {
			this.num = n;
			this.cost = c;
		}
	}
	
	static Node howFarIwillGo(int start) {
		Node far = new Node(0, 0);
		
		boolean[] visited = new boolean[N+1];
		visited[start] = true;
		
		ArrayDeque<Node> deque = new ArrayDeque<>();
		deque.add(new Node(start, 0));
		
		// BFS로 start 노드와 다른 노드까지의 거리 
		while(!deque.isEmpty()) {
			Node now = deque.poll();
			
			// now 노드와 연결된 다른 노드들을 본다.
			for(Node con : list.get(now.num)) {
				if (visited[con.num]) continue;
				visited[con.num] = true;
				deque.add(new Node(con.num, now.cost + con.cost));
				
				// 현재 가장 먼 노드의 거리보다
				// 지금 나까지 온 거리에 + con까지 가야하는 거리
				if (far.cost < now.cost + con.cost) {
					far.cost = now.cost + con.cost;
					far.num = con.num;
				}
				
			}
		}
		
		return far;
	}
	
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		list = new ArrayList<>();
		for (int i = 0; i <= N; i++) {
			list.add(new ArrayList<Node>());
		}
		
		for (int i = 0; i < N-1; i++) {
			st = new StringTokenizer(br.readLine());
			int parent = Integer.parseInt(st.nextToken());
			int child = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			
			list.get(parent).add(new Node(child, weight));
			list.get(child).add(new Node(parent, weight));			
		}
		
		Node far = howFarIwillGo(1);
		Node farthest = howFarIwillGo(far.num);
		
		System.out.println(farthest.cost);
	}

}
