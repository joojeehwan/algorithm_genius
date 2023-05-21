import java.util.*;

public class Pair implements Comparable<Pair>    {
        int town;
        int time;
        Pair(int town, int time){
            this.town = town;
            this.time = time;
        }

        @Override
        public int compareTo(Pair o) {
            return this.time - o.time;  //-1, 0 이면 자리바꿈
        }
    }

class Solution {
    public  int solution(int N, int[][] road, int K) {
        int answer = 0;

        //마을의 개수 N은 1 이상 50 이하의 자연수
        ArrayList<Pair>[] graph = new ArrayList[N+1];
        for(int i=1; i<N+1; i++)
            graph[i] = new ArrayList<>(N+1);

        //마을간 가중치 연결
        //그래프 생성
        for(int i=0; i<road.length; i++){
            graph[road[i][0]].add( new Pair(road[i][1],road[i][2]));
            graph[road[i][1]].add( new Pair(road[i][0],road[i][2]));
        }

        //각 마을 최단비용경로 초기화
        int[] town = new int[N+1];
        Arrays.fill(town,500001);

        boolean visited[] = new boolean[N+1];
        Arrays.fill(visited, false);

        PriorityQueue<Pair> q = new PriorityQueue<>();
        q.add(new Pair(1,0));
        town[1] = 0;    //1부터 시작
        visited[0] = true;


        while(!q.isEmpty()){
            int t = q.poll().town;

            if(visited[t]) continue;
            visited[t] = true;

            for(int i=0; i< graph[t].size(); i++){
                // 지금 거치는 경로 시간이 더 짧다면
                Pair nt = graph[t].get(i);
                if(town[t] + nt.time < town[nt.town]) {

                    town[nt.town] = town[t] + nt.time;
                    q.add(new Pair(nt.town, town[nt.town]));
                }
            }
        }

        //배달 가능한 마을 갯수 세기
        for(int i=1; i<N+1; i++) {
            if(town[i] <= K) answer+=1;
            System.out.print(town[i] + " ");
        }

        return answer;
    }
}
