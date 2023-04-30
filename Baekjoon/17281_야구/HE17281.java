import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HE17281 {
	
	static int N; //이닝 수
	static int[][] round; // 각 이닝별 선수 결과
	static boolean[] visited; // 순열 제작용. 이 선수가 이미 타순에 들었는지 확인
	static int cnt; // 순열 제작용. 순서
	static int[] players; // 순열 제작용. 실제 타순
	static boolean[] field; // 점수 계산용. 현재 1루, 2루, 3루 선수 존재 여부
	static int inning, outCnt, result, nowScore; // 현재 이닝수, 아웃수, 타자 결과, 점수
	static int score; // 최종 출력용 점수

	
	public static void makingOrder(int cnt) {
		if(cnt == 9) {
			caculateScore();
			return;
		}
		// 순열 만들기!
		for(int i = 1; i < 9; i++) {
			if(!visited[i]) {
				visited[i] = true;
				if(cnt == 3) cnt++;
				players[cnt] = i;
				makingOrder(cnt+1);
				// 갔다온 뒤
				visited[i] = false;
			}
		}
	}
	
	public static void caculateScore() {
		inning = 0;
		nowScore = 0;
		field = new boolean[4];
		// 9명의 순서를 다 정했고, 이제 점수를 계산해야한다.
		while(inning < N) {
			for(int player : players) {
				if(inning == N) break;
				result = round[inning][player];
				switch(result) {
				case 1:
					oneHit();
					break;
				case 2:
					twoHits();
					break;
				case 3:
					threeHits();
					break;
				case 4:
					// 홈런
					homeRun();
					break;
				case 0:
					out();
					break;
				}
			}
		}
		score = Math.max(score, nowScore);
	}
	
	public static void oneHit() {
		// 3루부터 계산
		if (field[3]) nowScore++;
		if (field[2]) {
			// 2루에 사람이 있어야 3루가 채워짐
			field[3] = true;
			field[2] = false;
		} else field[3] = false;

		// 2루
		if (field[1]) field[2] = true;
		
		// 1루 무조건 채워짐
		field[1] = true;
	
	}
	
	public static void twoHits() {
		// 1루에 있어야 3루 채워짐
		if (field[3]) nowScore++;
		if (field[1]) {
			field[3] = true;
			field[1] = false;
		} else field[3] = false;

		// 2루 무조건 채워짐... 와 2루 점수 계산 안해줘서 디버깅 오래걸림....
		if (field[2]) nowScore++;
		field[2] = true;
	}
	
	public static void threeHits() {
		for(int i = 1; i <= 3; i++) {
			if(field[i]) {
				nowScore++;
				field[i] = false;
			}
		}
		// 3루는 무조건 있다.
		field[3] = true;
	}
	
	public static void homeRun() {
		for(int i = 1; i <= 3; i++) {
			if(field[i]) {
				nowScore++;
				field[i] = false;
			}
		}
		nowScore++;
	}
	
	public static void out() {
		if(outCnt == 2) {
			for(int i = 1; i <= 3; i++) {
				// 다 나가자!
				field[i] = false;
			}
			inning++;
			outCnt = 0;
		} else {
			outCnt++;
		}
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		round = new int[N][9];
		
		// 이닝별 선수 결과 저장
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < 9; j++) {
				round[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 순열용 변수
		players = new int[9];
		visited = new boolean[9];
		
		// 감독님 최애
		visited[0] = true;
		cnt = 0;
		makingOrder(cnt);
		System.out.println(score);
	}

}
