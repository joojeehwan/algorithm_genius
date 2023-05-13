import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * 각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라. 
 * 최소 신장 트리 기본 문제. Prim(PriorityQueue) & Kruskal(Union + Find)
 * 1. 각 노드간의 비용을 저장해야 한다. 인접 리스트
 * 2. 1에 연결된 노드들을 PQ에 넣는다. 1번은 방문처리 한다.
 * 3. 하나씩 꺼내면서, 방문했는지 확인하고(방문 했으면 이미 최소값이라서),
 * 3-1. 방문 안했으면 방문 표기하고, 정답(최종 비용)에 현재 비용 추가한다.
 * 3-2. 현재 방문 노드에 연결된 다른 노드들을 다 PQ에 넣는다.
 * 4. PQ가 빌 때까지 반복한다.
 */
public class HE1922_Prim {
	
	static class Node implements Comparable<Node>{
		int num;
		int price;
		
		public Node(int n, int p) {
			this.num = n;
			this.price = p;
		}
		
		@Override
		public int compareTo(Node n) {
			return this.price - n.price;
		}
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		HashMap<Integer, ArrayList<Node>> cost = new HashMap<>();
		
		StringTokenizer st;
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()) - 1;
			int b = Integer.parseInt(st.nextToken()) - 1;
			int c = Integer.parseInt(st.nextToken());
			ArrayList<Node> listA = cost.getOrDefault(a, new ArrayList<>());
			ArrayList<Node> listB = cost.getOrDefault(b, new ArrayList<>());
			
			listA.add(new Node(b, c));
			cost.put(a, listA);
			
			listB.add(new Node(a, c));
			cost.put(b, listB);
		}
		
		boolean[] visited = new boolean[N];
		PriorityQueue<Node> q = new PriorityQueue<>();
		
		// 0 번째(시작) 노드 연결된 곳 PQ에 넣고 시작하기
		for(Node n:cost.get(0)) {
			q.add(n);
		}

		// 시작점은 계산 할게 없음
		visited[0] = true;
		
		
		int answer = 0;
		
		while(!q.isEmpty()) {
			Node now = q.poll();
			// 이미 갔던 곳이면 pass
			if (visited[now.num]) continue;
				
			// 연결된 곳 까지 가는 비용
			answer += now.price;
				
			// 연결된 곳 가기
			visited[now.num] = true;
			
			// 연결된 곳에서 또 찾기
			for(Node n : cost.get(now.num)) {
				q.add(n);
			}
		}
		System.out.println(answer);
	}

}
