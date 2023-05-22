// https://www.acmicpc.net/problem/1504

/* 방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 
 * => 시작점 ~ 끝점 최단 거리 = 다익스트라
 * 임의의 주어진 두 정점을 '반드시' 통과해야한다.
 * => 1번 ~ 점A + 점A ~ 점B + 점B ~ N번
 * => 1번 ~ 점B + 점B ~ 점A + 점A ~ N번
 * 두 경우 중 더 짧은 것
 * 다익스트라를 5번 돌려야 하나..?? (점A - 점B는 공통)
 * 
 * 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 
 * 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
 * => visited 체크 X, 길이만 비교해야함
 * 
 * 1. 정점간의 연결을 저장할 2차원 배열 필요
 * 2. 거리 기준으로 정렬할 PQ 필요
 * 
 * 그러한 경로가 없을 때에는 -1을 출력한다.
 * */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class HE1504 {
	static int N, E;
	static int MaxValue = 200_000 * 1000;
	static ArrayList<ArrayList<Node>> adj;
	
	static class Node implements Comparable<Node>{
		int num;
		int cost;
		
		public Node(int n, int c) {
			this.num = n;
			this.cost = c;
		}
		
		@Override
		public int compareTo(Node n) {
			return this.cost - n.cost;
		}
	}
	
	static int[] dijkstra(int s) {
		int[] dist = new int[N+1];
		
		for(int n = 1; n <= N; n++) {
			dist[n] = MaxValue;
		}
		
		PriorityQueue<Node> pq = new PriorityQueue<>();
		
		// 시작점을 넣는다.
		dist[s] = 0;
		pq.add(new Node(s, 0));
		
		
		while (!pq.isEmpty()) {
			// 가장 앞에 있는걸 꺼낸다.
			Node now = pq.poll();
			
			// 연결된 노드들을 본다.
			for(Node other : adj.get(now.num)) {
				// 기존에 시작점에서 other까지 가는 비용이
				// now 노드에서 other까지 가는 거리보다 멀다면 업데이트
				if (dist[other.num] > dist[now.num] + other.cost) {
					dist[other.num] = dist[now.num] + other.cost;
					pq.add(new Node(other.num, dist[other.num]));
				}
			}
		}
		
		
		return dist;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		adj = new ArrayList<>();
		
		for(int n = 0; n <= N; n++) {
			adj.add(new ArrayList<>());
		}
		
		for(int idx = 0; idx < E; idx++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			// 무방향 => 양쪽 다 추가해준다.
			adj.get(a).add(new Node(b, c));
			adj.get(b).add(new Node(a, c));
		}
		
		st = new StringTokenizer(br.readLine());
		int v1 = Integer.parseInt(st.nextToken());
		int v2 = Integer.parseInt(st.nextToken());
		
		int[] fromStart = dijkstra(1);
		int[] fromV1 = dijkstra(v1);
		int[] fromV2 = dijkstra(v2);
		

		int v1Tov2 = fromStart[v1] + fromV1[v2] + fromV2[N];
		int v2Tov1 = fromStart[v2] + fromV2[v1] + fromV1[N];
		
		int minDist = Math.min(v1Tov2, v2Tov1);
		System.out.println(minDist < MaxValue ? minDist : -1);		
	}
}
