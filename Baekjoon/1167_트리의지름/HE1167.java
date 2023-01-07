/*
 * 가장 먼 정점(A,B)끼리의 경로는, 한 정점(C)에서 부터 가장 먼 정점까지의 경로와 일부 겹친다.
 * C에서 가장 먼 정점도 A 또는 B가 된다. 그 이유는 트리의 특성 때문인데,
 * 트리는 모든 정점이 사이클 없이 연결되어있으며, 한 정점에서 다른 정점으로 가는 길은 유일하다.
 * 이러한 특성으로 인해 C에서 가장 먼 정점(만약 B라 하면)까지의 경로를 구하면, 
 * 그 정점(B)에서 가장 먼 정점(A)을 구할 경우
 * 그 경로가 가장 먼 정점끼리의 경로가 되는 것이다.
 * 
 * 또, 갑자기 IndexOutOfBounds 런타임 에러가 발생했는데, ArrayList를 배열로 바꾸니 해결되었다.
 * ArrayList<ArrayList<Node>> 형태로 만들었는데, 왜 인덱스 에러가 났는지 모르겠다.
 * for문에서 ArrayList 추가하기 전에 한개 추가해서, 총 V+1개가 생기도록 만들었는데...
 * */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Node {
	int num;
	int distance;
	
	Node(int num, int distance) {
		this.num = num;
		this.distance= distance;
	}
}

public class HE1167 {
	
	static ArrayList<Node>[] dist;
	static boolean[] visited;
	
	static int farNum = 0;
	static int answer = 1;
	
	static void dfs(int nodeNum, int distance) {
		if (answer < distance) {
			farNum = nodeNum;
			answer = distance;
		}
		
		visited[nodeNum] = true;
		
		for(int i = 0; i < dist[nodeNum].size(); i++) {
			Node nextNode = dist[nodeNum].get(i);
			if (visited[nextNode.num]) continue;
			dfs(nextNode.num, distance + nextNode.distance);
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int V = Integer.parseInt(br.readLine());
		
		dist = new ArrayList[V+1];
		
		for(int i = 0; i < V; i++) {
			st = new StringTokenizer(br.readLine());
			int point = Integer.parseInt(st.nextToken());
			dist[point] = new ArrayList<Node>();
			// 일단 최대값으로 채워놓는다. 나중에 플로이드 워샬로 계산하기 위함
			
			while(true) {
				int nPoint = Integer.parseInt(st.nextToken());
				if (nPoint == -1) break;
				int nDist = Integer.parseInt(st.nextToken());
				// 입력 값에 애초에 양방향을 본다...
				dist[point].add(new Node(nPoint, nDist));
			}
		}
		
		visited = new boolean[V+1];
		dfs(1, 0);
		
		visited = new boolean[V+1];
		dfs(farNum, 0);
		
		System.out.println(answer);
	}

}
