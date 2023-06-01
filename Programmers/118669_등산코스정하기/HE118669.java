import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.PriorityQueue;

class Solution {
    class Node implements Comparable<Node>{
        int num;
        int cost;
        
        public Node (int n, int c) {
            this.num = n;
            this.cost = c;
        }
        
        @Override
        public int compareTo(Node n) {
            return this.num - n.num;
        }
    }
    
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        ArrayList<ArrayList<Node>> adj;
        HashSet<Integer> peaks = new HashSet<>();
        int maxIntensity = Integer.MAX_VALUE;
        int maxNode = Integer.MAX_VALUE;
        
        // 연결리스트 생성
        adj = new ArrayList<>();
        
        for(int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }
        
        for(int[] path : paths) {
            int a = path[0];
            int b = path[1];
            int c = path[2];
            
            // 양방향 연결
            adj.get(a).add(new Node(b, c));
            adj.get(b).add(new Node(a, c));
        }
        
        // i번째 노드까지 본 intensity중 최대값
        int[] intensity = new int[n+1];
        Arrays.fill(intensity, Integer.MAX_VALUE);
        
        // 산봉우리 Set -> 다익스트라 볼 때 산봉우리는 pq에 추가 안하려고
        for(int summit : summits) {
            peaks.add(summit);
        }
        
        // 다익스트라 시작
        PriorityQueue<Node> pq = new PriorityQueue<>();
        
        // PQ에 출입구 넣기 + 출입구는 시작이므로 최대 intensity가 없음
        for(int gate : gates) {
            pq.add(new Node(gate, 0));
            intensity[gate] = 0;
        }
        
        while(!pq.isEmpty()) {
            Node now = pq.poll();
            
            // 지금 나보다 같거나 크면, 그 쪽으로 가볼 이유가 없음
            if (intensity[now.num] < now.cost) continue;
            intensity[now.num] = now.cost;
            
            // 나랑 연결된 노드들 중에서
            for(Node other : adj.get(now.num)) {
                // now까지의 최대 intensity랑, 내 cost랑 비교해서 더 큰 값
                // 지금 pq라서 cost가 작은 것 부터 보면서 지나오고 있다.
                // 둘 중 큰 값을 찾는 이유는, 최대 intensity를 찾아야 하기 때문
                // pq를 쓰는 이유는, 그 최대 intensity의 값이 가장 작길 원하기 때문
                int newIntensity = Math.max(intensity[now.num], other.cost);
                if (newIntensity < intensity[other.num]) {
                    intensity[other.num] = newIntensity;
                    // 산봉우리는 못 간다.
                    if (!peaks.contains(other.num)) pq.add(new Node(other.num, intensity[other.num]));
                }
            }
        }        
        // 다익스트라 끝났으면, 산봉우리만 보면서 '최소' intensity값을 찾는다. (그게 최대 intensity가 최소인 등산경로)
        for(int summit : summits) {
            if (intensity[summit] < maxIntensity) {
                maxIntensity = intensity[summit];
                maxNode = summit;
            } else if (intensity[summit] == maxIntensity && maxNode > summit) {
                maxNode = summit;
            }
        }
        
        return new int[] {maxNode, maxIntensity};
    }
}