import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class HE16948 {
	
	static class Pos {
		int r;
		int c;
		
		public Pos(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}
	
	static int[] dr = {-2, -2, 0, 0, 2, 2};
	static int[] dc = {-1, 1, -2, 2, -1, 1};


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String[] input = br.readLine().split(" ");
		int startRow = Integer.parseInt(input[0]);
		int startCol = Integer.parseInt(input[1]);
		int goalRow = Integer.parseInt(input[2]);
		int goalCol = Integer.parseInt(input[3]);
		
		Queue<Pos> queue = new LinkedList<>();
		int[][] visited = new int[N][N];

		queue.add(new Pos(startRow, startCol));
		visited[startRow][startCol] = 1;
				
		while(!queue.isEmpty()) {
			Pos now = queue.poll();
			int nowRow = now.r;
			int nowCol = now.c;
			
			for (int d=0;d <6; d++) {
				int nextRow = nowRow + dr[d];
				int nextCol = nowCol + dc[d];
				
				if (0 <= nextRow && nextRow < N && 0 <= nextCol && nextCol < N) {
					if (visited[nextRow][nextCol] == 0) {
						visited[nextRow][nextCol] = visited[nowRow][nowCol] + 1;
						queue.add(new Pos(nextRow, nextCol));
					}
				}
			}
		}
		
		if (visited[goalRow][goalCol] == 0) System.out.println(-1);
		else System.out.println(visited[goalRow][goalCol]-1);
	}

}
