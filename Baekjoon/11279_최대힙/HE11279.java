import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class HE11279 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < N; i++) {
			int num = Integer.parseInt(br.readLine());
			if (num == 0) {
				if (q.isEmpty()) {
					sb.append(0);
				} else {
					sb.append(q.poll());
				}
				sb.append("\n");
			} else {
				q.add(num);
			}
		}
		System.out.println(sb.toString());
	}

}