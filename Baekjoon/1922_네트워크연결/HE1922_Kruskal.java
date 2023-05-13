import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class HE1922_Kruskal {
	/**
	 * 각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라. 
	 * 최소 신장 트리 기본 문제. Prim(PriorityQueue) & Kruskal(Union + Find)
	 * 1. 모든 간선을 가중치에 따라 오름차순으로 정렬한다. (간선 = (비용, a, b))
	 * 2. 가중치가 가장 낮은 간선부터 선택하여 집합으로 만든다(Find하고 Union 시킴)
	 * 2-1. 이미 같은 상태라면? 다음 간선으로 넘어간다.
	 * 3. 했으면 그 다음 가중치가 낮은 간선을 보며 반복한다. 남은 간선이 없을때까지
	 */
	static int[] parent;
	
	static void union(int a, int b) {
		int parentA = find(a);
		int parentB = find(b);
		parent[parentB] = parentA;
	}
	
	static int find(int idx) {
		while (parent[idx] != idx) {
			idx = parent[idx];
		}
		return parent[idx];
	}
	
	static class Edge implements Comparable<Edge> {
        int cost;
        int a;
        int b;
        
        public Edge(int c, int a, int b) {
            this.cost = c;
            this.a = a;
            this.b = b;
        }
        
        @Override
        public int compareTo(Edge other) {
            return this.cost - other.cost;
        }
    }
    
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int answer = 0;
        
        // 노드간의 연결 관계 저장
        PriorityQueue<Edge> q = new PriorityQueue<>();
        
        // 각 노드 방문 확인
        parent = new int[N+1];
        for(int i = 1; i <= N; i++) {
        	// 처음엔 스스로가 부모
        	parent[i] = i;
        }
        
        
        StringTokenizer st;
        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            
            // 단방향 X
            q.add(new Edge(c, a, b));
        }

        
        while(!q.isEmpty()) {
            Edge e = q.poll();
            if(find(e.a) != find(e.b)) {
            	answer += e.cost;
            	union(e.a, e.b);
            }
        }
        System.out.println(answer);
    }
}
