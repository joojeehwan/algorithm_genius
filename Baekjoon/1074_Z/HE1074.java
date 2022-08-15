import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

/*
* 백준에 제출할 땐 class 이름은 Main으로!
*/

public class HE1074 {

  static int N;
  static int goalRow;
  static int goalCol;
  static int answer = 0;

  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    goalRow = Integer.parseInt(st.nextToken());
    goalCol = Integer.parseInt(st.nextToken());

    divideConquer(N, 0, 0);
    bw.write(String.valueOf(answer));
    // close the buffer
    br.close();
    bw.close();

  }

  static void divideConquer(int n, int row, int col) {
    if(row == goalRow && col == goalCol) {
      return;
    }

    n -= 1;
    int halfWidth = (int) Math.pow(2, n);

    boolean rowOver = (goalRow >= row+halfWidth)? true : false;
    boolean colOver = (goalCol >= col+halfWidth)? true : false;

    int blockCnt = (int) Math.pow(4, n);

    if(!rowOver) {
      if(!colOver) {
        divideConquer(n, row, col);
      }
      else {
        answer += blockCnt;
        divideConquer(n, row, col+halfWidth);
      }
    } else {
      if(!colOver) {
        answer += 2 * blockCnt;
        divideConquer(n, row+halfWidth, col);
      }
      else {
        answer += 3 * blockCnt;
        divideConquer(n, row+halfWidth, col+halfWidth);
      }
    }
  };
}
