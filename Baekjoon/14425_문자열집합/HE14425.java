import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

/*
 * 백준에 제출할 땐 class 이름은 Main으로!
 */

public class HE14425 {
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int answer = 0;
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    
    Set<String> S = new HashSet<String>();


    for(int i = 0; i < n; i++) {
      S.add(br.readLine());
    }

    for(int i = 0; i < m; i++) {
      if (S.contains(br.readLine())) {
        answer++;
      }
    }

    System.out.println(answer);

  }
}