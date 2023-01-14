/*
 * 플레더니만.. 오롯이 BFS로 푸는 문제가 아니었다!
 * https://www.acmicpc.net/board/view/35071
 * 짝수, 홀수 초를 나누는 것이 처음엔 이해가 잘 안되었는데,
 * 예로 100이라는 위치에 수빈이는 7초에 이미 갔었고, 동생은 41초쯤에 도착했다고 하면
 * 수빈이는 41초에 100에 도착할 수 있는 것이다. (왔다 갔다 가능)
 * 대강 이해는 했는데, 이 풀이를 발견해낸 사람은 20분 정도 생각하고 바로 찾아냈다는게
 * 격차를 느끼게 한다....
 * */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class HE17071 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N, K;
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		int time = 0;
		boolean[][] visited = new boolean[2][500001]; // [0]은 짝수, [1]은 홀수
		
		Queue<Integer> q = new LinkedList<>();
		q.add(N);
		visited[0][N] = true;
		boolean found = visited[0][K];
		
		while(!found) {
			time += 1;
			K += time;
			if(K > 500000) break;
			
			Queue<Integer> nextQ = new LinkedList<>();
			
			while(!q.isEmpty()) {
				int now = q.poll();
				
				if(now-1 >= 0 && visited[time%2][now-1] == false) {
					visited[time%2][now-1] = true;
					nextQ.add(now-1);
				}
				if(now+1 <= 500000 && visited[time%2][now+1] == false) {
					visited[time%2][now+1] = true;
					nextQ.add(now+1);
				}
				if(now*2 <= 500000 && visited[time%2][now*2] == false) {
					visited[time%2][now*2] = true;
					nextQ.add(now*2);
				}
			}
			q = nextQ;
			
			if(visited[time%2][K]) {
				found = true;
				break;
			}
		}
		
		if (found == false) {
			System.out.println(-1);
		} else {
			System.out.println(time);
		}
	}

}
