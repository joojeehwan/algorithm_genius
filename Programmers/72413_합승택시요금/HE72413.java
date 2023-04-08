import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    static int[][] cost;
    static int N;

    class Node implements Comparable<Node> {
        int idx;
        int dist;

        public Node(int idx, int dist) {
            this.idx = idx;
            this.dist = dist;
        }

        @Override
        public int compareTo(Node n) {
            return this.dist - n.dist;
        }

    }

    public int[] dijkstra(int s) {
        int[] distance = new int[N+1];
        Arrays.fill(distance, 999_999);
        PriorityQueue<Node> q = new PriorityQueue<>();

        q.add(new Node(s, 0));
        distance[s] = 0;

        while(!q.isEmpty()) {
            Node now = q.poll();
            
            // cost가 0이면 pass 가능

            for(int i = 1; i <= N; i++) {
                // distance[i] = s에서 i 까지의 기존 거리
                // now.dist = s에서 now.idx까지의 거리 + now.idx에서 i까지의 거리
                if (distance[i] > now.dist + cost[now.idx][i]) {
                    distance[i] = now.dist + cost[now.idx][i];
                    q.add(new Node(i, distance[i]));
                }
            }
        }

        return distance;
    }


    public int solution(int n, int s, int a, int b, int[][] fares) {
        N = n;
        cost = new int[n+1][n+1];
        for(int i = 1; i <= N; i++) {
            Arrays.fill(cost[i], 999_999); // 100_001로 타이트하게 하니깐 틀린다...
        }

        for(int[] fare : fares) {
            int c = fare[0];
            int d = fare[1];
            int f = fare[2];
            cost[c][d] = f;
            cost[d][c] = f;
        }

        int[] solo = dijkstra(s);
        int Muji = solo[a];
        int Apeach = solo[b];
        int together = Integer.MAX_VALUE;
        for(int i = 1; i <= n; i++) {
        	// i -> A,B 말고 A-> 전체, B -> 전체 로 구하면 다익스트라 3번만 호출 가능 
            // 합승하는게 좋은지 봐볼거임.
            if (i == s) continue;
            int sToi = solo[i]; // s부터 i 까지의 거리를 기반으로
            int[] fromI = dijkstra(i); // i부터 다른 점들 까지의 거리를 보면서
            int sum = sToi + fromI[a] + fromI[b]; // 합승한 경우의 총 거리를 본다.
            together = Math.min(together, sum);
        }
        return (Muji + Apeach < together) ? Muji + Apeach : together;
    }
}