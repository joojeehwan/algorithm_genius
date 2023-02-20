import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class HE9251 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// 파이썬 보고싶다!
		char[] stringA = br.readLine().toCharArray();
		char[] stringB = br.readLine().toCharArray();
		int answer = 0;
		int lenA = stringA.length;
		int lenB = stringB.length;
		int[][] LCS = new int[lenA+1][lenB+1];
		
		for (int a = 1; a <= lenA; a++) {
			for (int b = 1; b <= lenB; b++) {
				if(stringA[a-1] == stringB[b-1]) LCS[a][b] = LCS[a-1][b-1] + 1;
				else LCS[a][b] = Math.max(LCS[a][b-1], LCS[a-1][b]);
				answer = Math.max(answer, LCS[a][b]);
			}
		}
		
		System.out.println(answer);
	}

}
