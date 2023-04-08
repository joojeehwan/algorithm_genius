import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int K = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int[] wire = new int[K];

		long min = 1;
		long max = 0;
		long mid = 0;
		long cnt = 0;
		
		for(int k = 0; k < K; k++) {
			wire[k] = Integer.parseInt(br.readLine());
			if(wire[k] > max) {
				max = wire[k];
			}
		}
		
		while(min <= max) {
			mid = (min + max) / 2;
			cnt = 0;
			
			for(int i = 0; i < K; i++) {
				cnt += (wire[i] / mid);
			}
			
			if(cnt >= N) {
				min = mid + 1;
			}
			else {
				max = mid - 1;
			}
		}
		System.out.println((min+max)/2);
	}

}
