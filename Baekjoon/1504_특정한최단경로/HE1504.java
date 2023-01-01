/*
 * https://steady-coding.tistory.com/82
 * 1. 간선의 가중치가 있다면 다익스트라다.(음의 값이 있으면 벨만포드)
 * 2. "반드시" 지나야하는 정점은 그냥 각각 계산해주고 나중에 비교하면 된다.
 * 3. 인접행렬을 N * N 의 2차원 배열이 아닌, cost와 목적지를 합한 2차원 배열로 만들었다.
 * 4. 자바에서 PriorityQueue 를 사용하기 위해선 Comparable을 사용할 줄 알자!
 * */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


class Node implements Comparable<Node> {
	int num;
	int weight;
	
	Node(int num, int weight) {
		this.num = num;
		this.weight = weight;
	}
	
	@Override
	public int compareTo(Node o) {
		return weight - o.weight; // 오름차순 정렬. 내림차순은 둘을 반대로.
	}
}


public class Main {
	static ArrayList<ArrayList<Node>> graph;
	static int[] dist;
	static int N, E;
	static final int INF = 200000000;
	
	
	static int dijkstra(int start, int end) {
		// 최대값으로 거리 다 채우고, 최단거리 계산하면서 업데이트
		dist = new int[N+1];
		Arrays.fill(dist, INF);
		// PriorityQueue 사용법 : https://coding-factory.tistory.com/603
		PriorityQueue<Node> q = new PriorityQueue<>();
		q.add(new Node(start, 0));
		dist[start] = 0;
		
		while(!q.isEmpty()) {
			Node node = q.poll();
			int now = node.num;
			int weight = node.weight;
			
			// 굳이 업데이트할 필요가 없다면 넘어간다.
			if (dist[now] < weight) continue;
			
			for (int i = 0; i < graph.get(now).size(); i++) {
				Node next = graph.get(now).get(i);
				int cost = dist[now] + next.weight; // 거쳐가는 거리
				if (cost < dist[next.num]) {
					// 현재 노드를 거쳐 가는게, 다른 노드로 바로 가는 것 보다 빠를 경우
					dist[next.num] = cost;
					q.offer(new Node(next.num, cost));
				}
			}
		}
		return dist[end];
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		
		graph = new ArrayList<>();
		
		for(int i = 0; i <= N; i++) {
			graph.add(new ArrayList<>());
		}

		
		for(int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());

			graph.get(from).add(new Node(to, cost));
			graph.get(to).add(new Node(from, cost));
		}
		
		st = new StringTokenizer(br.readLine(), " ");
		int v1 = Integer.parseInt(st.nextToken());
		int v2 = Integer.parseInt(st.nextToken());
		
		// 1 -> v1 -> v2 -> N
		int path_1 = dijkstra(1, v1);
		path_1 += dijkstra(v1, v2);
		path_1 += dijkstra(v2, N);
		
		// 1 -> v2 -> v1 -> N
		int path_2 = dijkstra(1, v2);
		path_2 += dijkstra(v2, v1);
		path_2 += dijkstra(v1, N);
		
		// 둘 중에 더 가까운 거리를 찾는다.
		int answer = Math.min(path_1, path_2);
		
		if (answer >= INF) {
			System.out.println(-1);
		} else {
			System.out.println(answer);
		}
	}

}
