import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class HE2382 {
	static class Microbe implements Comparable<Microbe>{
		int row;
		int col;
		int count;
		int dir;
		
		public Microbe(int row, int col, int count, int dir) {
			this.row = row;
			this.col = col;
			this.count = count;
			this.dir = dir;
		}

		@Override
		public int compareTo(Microbe o) {
			// TODO Auto-generated method stub
			// 
			return o.count - this.count;
		}
	}
		
	static HashMap<Integer, ArrayList<Microbe>> microbes;
	static int[] dr = {0, -1, 1, 0, 0};
	static int[] dc = {0, 0, 0, -1, 1};


	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		System.setIn(new java.io.FileInputStream("src/swea2382/2382_input.txt"));

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int T = Integer.parseInt(st.nextToken());
		
		for(int tc=1; tc < T+1; tc++) {
			microbes = new HashMap<Integer, ArrayList<Microbe>>();
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			
			for(int i=0; i < K; i++) {
				st = new StringTokenizer(br.readLine());
				int r = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				int m = Integer.parseInt(st.nextToken());
				int d = Integer.parseInt(st.nextToken());
				// 2차원 배열을 N으로 곱하여 1차원 값으로 만든다.
				int pos = r * N + c;
				Microbe microbe = new Microbe(r, c, m, d);
				
				// 이미 다른 군집이 있는 곳이라면 추가만 한다.
				if(microbes.get(pos) != null) {
					microbes.get(pos).add(microbe);
				}
				else {
					// 원래 군집이 없었다면 HashMap에 새로 넣는다.
					ArrayList<Microbe> microbeList = new ArrayList<Microbe>();
					microbeList.add(microbe);
					microbes.put(pos, microbeList);
				}
			}
			
			// M번 반복한다.
			for(int time=0; time < M; time++) {
				HashMap<Integer, ArrayList<Microbe>> moveMicrobes = new HashMap<Integer, ArrayList<Microbe>>();
				
				// 군집을 각자의 방향에 맞게 움직인다.
				for(int pos:microbes.keySet()) {			
					ArrayList<Microbe> nowMicrobes = microbes.get(pos);
					
					for(int idx=0; idx < nowMicrobes.size(); idx++) {
						Microbe microbe = nowMicrobes.get(idx);
						int count = microbe.count;
						int dir = microbe.dir;
						int row = microbe.row + dr[microbe.dir];
						int col = microbe.col + dc[microbe.dir];
						
						if(row == 0 || row == N-1 || col == 0 || col == N-1) {
							count /= 2;
							if(dir % 2 == 0) {
								dir--;
							} else {
								dir++;
							}
						}
						int nextPos = row * N + col;
						Microbe movedMicrobe = new Microbe(row, col, count, dir);
						
						if(count > 0) {
							// 이미 있다면 배열에만 추가
							if(moveMicrobes.get(nextPos) != null) {
								moveMicrobes.get(nextPos).add(movedMicrobe);	
							}
							else {
								// 비었다면 moveMicrobes 해시맵에 추가
								ArrayList<Microbe> microbeList = new ArrayList<Microbe>();
								microbeList.add(movedMicrobe);
								moveMicrobes.put(nextPos, microbeList);
							}
						}
					}
				}
				
				// 같은 장소에 있는 미생물 군집을 합쳐야한다.
				for(int pos:moveMicrobes.keySet()) {
					ArrayList<Microbe> movedList = moveMicrobes.get(pos);
					int listSize = movedList.size();
					if(movedList.size() > 1) {
						Collections.sort(movedList);
						Microbe mostMicrobe = movedList.get(0);
						int mostDir = mostMicrobe.dir;
						int sumCount = 0;
						for(int m=0; m < listSize; m++) {
							sumCount += movedList.get(m).count;
						}
						
						Microbe finalMicrobe = new Microbe(mostMicrobe.row, mostMicrobe.col, sumCount, mostDir);
						movedList = new ArrayList<Microbe>();
						movedList.add(finalMicrobe);
						moveMicrobes.put(pos, movedList);
					}
				}
				microbes = moveMicrobes;
			}
			
			int answer = 0;
			for(ArrayList<Microbe> finMicrobes:microbes.values()) {

				for(Microbe microbe:finMicrobes) {
					answer += microbe.count;
				}

			}
			System.out.println("#"+tc+ " " + answer);
		}
	}
}