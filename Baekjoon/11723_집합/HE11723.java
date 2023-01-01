import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int S = 0;
	static StringBuilder sb = new StringBuilder(); // StringBuilder 안썼더니 시간초과 남
	
	static void add(int x) {
		S |= 1 << x;
	}
	
	static void remove(int x) {
		S &= ~(1 << x);
	}
	
	static void check(int x) {
		sb.append((((S & (1 << x)) != 0))? 1 : 0);
		sb.append("\n");
	}
	
	static void toggle(int x) {
		S ^= (1 << x);
	}
	
	static void all() {
		S = (int) (Math.pow(2, 20) -1);
	}
	
	static void empty() {
		S = 0;
	}
	
//	static void print() {
//		System.out.println("S값은 : " + S + " / 비트값 : " + Integer.toBinaryString(S));
//	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int M = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			String order = st.nextToken();
			
			switch (order) {
				case "add":
					add(Integer.parseInt(st.nextToken()) - 1);
					break;
				case "remove":
					remove(Integer.parseInt(st.nextToken()) - 1);
					break;
				case "check":
					check(Integer.parseInt(st.nextToken()) - 1);
					break;
				case "toggle":
					toggle(Integer.parseInt(st.nextToken()) - 1);
					break;
				case "all":
					all();
					break;
				case "empty":
					empty();
					break;
			}
		}
		System.out.println(sb.toString());
	}
}
