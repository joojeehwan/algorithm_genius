/*
 * 참고 : https://school.programmers.co.kr/learn/courses/30/lessons/77485/solution_groups?language=java
 * */

class HE77485 {
	
	public static int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        // 1 ~ rows * columns 까지의 2차원 배열
        int[][] matrix = new int[rows][columns];
        for(int r = 0; r < rows; r++) {
            for(int c = 0; c < columns; c++) {
                matrix[r][c] = r * columns + c + 1;
            }
        }
        
        for(int q = 0; q < queries.length; q++) {
        	int[] query = queries[q];
            int[][] moved = new int[rows][columns];
            // 기존 값 저장 후 덮어쓰기
            for(int r = 0; r < rows; r++) {
            	for(int c = 0; c < columns; c++)
            		moved[r][c] = matrix[r][c];
            }
            
            int minimum = rows * columns + 1;
            
            // 직사각형 값 가져오기.
            int x1 = query[0]-1, y1 = query[1]-1, x2 = query[2]-1, y2 = query[3]-1;
            
            // 오른쪽 이동
            for(int i = 0; i < y2-y1; i++) {
            	moved[x1][y1+i+1] = matrix[x1][y1+i];
            	minimum = Math.min(minimum, moved[x1][y1+i+1]);
            }
            // 아래로 이동
            for(int i = 0; i < x2-x1; i++) {
            	moved[x1+i+1][y2] = matrix[x1+i][y2];
            	minimum = Math.min(minimum, moved[x1+i+1][y2]);
            }
            // 왼쪽 이동
            for(int i = 0; i < y2-y1; i++) {
            	moved[x2][y2-i-1] = matrix[x2][y2-i];
            	minimum = Math.min(minimum, moved[x2][y2-i-1]);
            }
            // 위로 이동
            for(int i = 0; i < x2-x1; i++) {
            	moved[x2-i-1][y1] = matrix[x2-i][y1];
            	minimum = Math.min(minimum, moved[x2-i-1][y1]);
            }

            // 기존 값에 옮겨주기
            for(int r = 0; r < rows; r++) {
            	for(int c = 0; c < columns; c++)
            		matrix[r][c] = moved[r][c];
            }
            answer[q] = minimum;
        }
        return answer;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		int[][] ihatejava = {{2, 2, 5, 4}, {3, 3, 6, 6}, {5, 1, 6, 3}};
//		int[][] ihatejava = {{1, 1, 100, 97}};
//		System.out.println("정답 : " + Arrays.toString(solution(6, 6, ihatejava)));
//		System.out.println("정답 : " + Arrays.toString(solution(100, 97, ihatejava)));

	}

}
