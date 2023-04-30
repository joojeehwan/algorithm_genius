/* 
 * 무슨 쉬운 BFS 문제 하나 푸는데 배워야할게 이렇게 많은지.. 진짜 Java 골때린다.
*/
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
	// N * N인줄 알고 난리남^^;;
	// 전역변수로 써야할게 왜이렇게 많냐
    int N, M;
    boolean[][] visited;
    int[][] island;
    
    // java는 왤케 튜플 쓰기가 귀찮냐!!
    class Pair {
        int r;
        int c;
        
        public Pair(int _r, int _c) {
            this.r = _r;
            this.c = _c;
        }
    }
    
    // 지나갈수 있는지 함수로 보고싶었고, 그렇다 보니 N과 M, visited, island 다 클래스 변수로 만들었다.
    boolean isPassable(int r, int c) {
        if (0 > r || r >= N || 0 > c || c >= M) return false;
        if (visited[r][c]) return false;
        if (island[r][c] == 0) return false;
        return true;
    }
    
    public int[] solution(String[] maps) {
        N = maps.length;
        M = maps[0].length();
        // 문자열 2차원 배열 maps : 'X' => 바다, 1 ~ 9 => 무인도 식량
        // 상하좌우로 이어진 무인도의 식량의 합 = 최대 며칠 머무를 수 있는가.
        // 오름차순으로 저장. 없으면 -1
        // 무인도의 수는 몇개? 정해지지 않았으니 ArrayList로 만들었다.
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        // 상 하 좌 우
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        
        visited = new boolean[N][M];
        island = new int[N][M];
        
        // 입력처리
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if (maps[i].charAt(j) != 'X') island[i][j] = maps[i].charAt(j) - '0';
            }
        }
        
        for(int r = 0; r < N; r++) {
            for(int c = 0; c < M; c++) {
                if (!visited[r][c] && island[r][c] > 0) {
                    visited[r][c] = true;
                    
                    // ArrayDeque를 사용한 이유
                    // 1. queue나 deque 역할을 할 자료구조가 필요했고
                    // 2. 빠른 접근이 필요했음
                    ArrayDeque<Pair> q = new ArrayDeque<Pair>();
                    q.add(new Pair(r, c));
                    int foods = island[r][c];
                    
                    while(!q.isEmpty()){
                        Pair now = q.poll();
                        
                        for(int d = 0; d < 4; d++) {
                            int nextR = now.r + dr[d];
                            int nextC = now.c + dc[d];
                            
                            if (isPassable(nextR, nextC)) {
                                visited[nextR][nextC] = true;
                                q.add(new Pair(nextR, nextC));
                                foods += island[nextR][nextC];
                            }
                        }
                    }
                    
                    list.add(foods);
                }
            }
        }
        
        // 반환을 int[] 배열로 해야함
        // Array 문서 : https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Array.html
        // List<Integer> -> int[] : https://stackoverflow.com/questions/960431/how-can-i-convert-listinteger-to-int-in-java
        // ArrayList를 int 배열로 바꿀때 고민할 점이 있다.
        // 우선 ArryaList의 크기를 받고 반복문으로 해줄 수도 있지만, stream을 활용할 수도 있다.
        // 	Java의 Stream은 자바 8에서 추가된 새로운 기능(API) 중 하나로, 컬렉션, 배열, I/O 등의 데이터 소스를 다루는 데 사용됩니다. 
        //  그냥 toArray는 Object[]를 반환한다. 타입을 넣어준다 한들, primitive type은 사용할 수 없다.
        int[] answer = list.stream().mapToInt(i -> i).toArray();
        
        if (answer.length == 0) {
            answer = new int[] {-1};
        } else {
            Arrays.sort(answer);
        }
        
        return answer;
    }
}