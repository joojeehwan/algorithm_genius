/*
 * 참고 : https://st-lab.tistory.com/251
 * 중간 계산에서 모듈러 연산을 해도 되는 이유?
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class HE10830 {
	static int N;
	
	public static int[][] multiMatrix(int[][] m1, int[][] m2) {
		int[][] result = new int[N][N];
		for(int r = 0; r < N; r++) {
			for(int c = 0; c < N; c++) {
				for(int x = 0; x < N; x++) {
					// 왜 중간 과정에서 1000으로 미리 나눠도 되는거지?
					result[r][c] += (m1[r][x] * m2[x][c]) % 1000;
				}
			}
		}
		return result;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		long B = Long.parseLong(st.nextToken());
		int[][] A = new int[N][N];
		int[][] matrix = new int[N][N];
		
		// 입력받기
		for(int i = 0; i < N; i++) {
			matrix[i][i] = 1;  // matrix를 단위행렬로 초기화
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < N; j++) {
				A[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		while(B > 0) {
			if(B % 2 == 1) {
				matrix = multiMatrix(matrix, A); // 홀수일경우 한번 더 곱해줌
			}
			A = multiMatrix(A, A); // A를 제곱함
			
			B /= 2;
		}
		
		for(int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				System.out.print(matrix[i][j] % 1000);
				if (j < N-1) System.out.print(" ");
			}
			if(i < N-1) System.out.println();
		}
		
	}

}
