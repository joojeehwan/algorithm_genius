/*
 * 정답률을 보니 정확도를 맞춘 사람은 50%, 효율성을 맞춘 사람은 1%이다.
 * 게다가 문제도 6번이니만큼 효율성을 챙길게 아니라 완전탐색으로 정확도라도 맞춰야하는 문제.
 * 누적합과, 1차원의 누적합을 2차원의 누적합으로(여러 행의 동일한 열 값을 하나의 1차원 배열 누적합으로 생각) 변환하는 개념에 대해
 * 알아야 풀 수 있는 문제이다. 이런건 처음봤다.
 * */

class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int rowSize = board.length;  // 행 크기
        int colSize = board[0].length;  // 열 크기
        
        // 누적합을 저장할 board와 같은 크기의 2차원 배열
        int[][] point = new int[rowSize][colSize];
        
        for(int i = 0; i < skill.length; i++) {
            // skill = [타입(1,2), r1, c1, r2, c2, degree] 의 정보를 담는다.
            // 2차원 누적합을 위해 (r1, c1)과 (r2+1, c2+1)에 degree를,
            // (r2+1, c2)와 (r1, c2+1)에 -degree를 저장한다.
            int r1 = skill[i][1], c1 = skill[i][2], r2 = skill[i][3], c2 = skill[i][4];
            int degree = (skill[i][0] == 2) ? skill[i][5] : -skill[i][5]; // type이 2면 +, 1이면 - 값으로 내구도에 반영된다.
            
            point[r1][c1] += degree;
            // 이 밑은 범위가 밖이면 없어도 되는 값들이다.
            if (r2+1 < rowSize && c2+1 < colSize) point[r2+1][c2+1] += degree;
            if (r2+1 < rowSize) point[r2+1][c1] -= degree;
            if (c2+1 < colSize) point[r1][c2+1] -= degree;
        }
        
        // 누적합을 구하기 위해 다 설정을 해두었다면, 이제 실제로 구한다.
        // 위->아래 + 왼->오 방향으로 합해도 되고, 왼->오 + 위->아래 방향으로 합해도 된다.
        
        // 위->아래 행으로 내려가며 위의 값을 아래에 합한다.
        for(int r = 1; r < rowSize; r++) {
            for(int c = 0; c < colSize; c++) {
                point[r][c] += point[r-1][c];
            }
        }
        
        // 왼 -> 오른쪽으로 가며 이전 열의 값을 다음 열에 합한다.
        for(int c = 1; c < colSize; c++) {
            for(int r = 0; r < rowSize; r++) {
                point[r][c] += point[r][c-1];
            }
        }
        
        // point + board
        for(int r = 0; r < rowSize; r++) {
            for(int c = 0; c < colSize; c++) {
                if (board[r][c] + point[r][c] >= 1) answer++;
            }
        }
        
        return answer;
    }
}