import java.awt.Point;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
	public int solution(int[][] maps) {
		int answer = -1;

		int[] dr = {-1, 1, 0, 0};
		int[] dc = {0, 0, -1, 1};

		int N = maps[0].length;
		int M = maps.length;

		int[][] visited = new int[M][N];

		Queue<Point> q = new LinkedList<Point>();
		q.add(new Point(0, 0));
		visited[0][0] = 1;

		while(!q.isEmpty()) {
			Point now = q.poll();
			int now_r = now.x;
			int now_c = now.y;

			for(int d=0; d<4; d++) {
				int new_r = now_r + dr[d];
				int new_c = now_c + dc[d];

				if (0 <= new_r && new_r < M && 0 <= new_c && new_c < N) {
					if (visited[new_r][new_c] == 0 && maps[new_r][new_c] == 1) {
						visited[new_r][new_c] = visited[now_r][now_c] + 1;
						q.add(new Point(new_r, new_c));
					}
				}
			}
		}

		if (visited[M-1][N-1] > 0) {
			answer = visited[M-1][N-1];
		}

		return answer;
	}
}
