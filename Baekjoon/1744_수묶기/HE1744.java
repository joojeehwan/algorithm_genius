import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;

public class HE1744 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int ans = 0;
		int N = Integer.parseInt(br.readLine());
		
		ArrayList<Integer> pos = new ArrayList<>(); // 양수 저장
		ArrayList<Integer> neg = new ArrayList<>(); // 음수 저장
		boolean isZero = false;
		
		for(int i = 0; i < N; i++) {
			int num = Integer.parseInt(br.readLine());
			if(num > 0) pos.add(num);
			else if (num < 0) neg.add(num);
			else isZero = true;
		}

		if (!pos.isEmpty()) {
			int posSize = pos.size();
			if (posSize >= 2) {
				pos.sort(Comparator.reverseOrder()); // 수의 절대값이 큰 값이 앞으로 오도록 정렬한다.
				if (posSize % 2 == 1) {
					// 양수가 홀수개인 경우, 가장 마지막(가장 절대값이 작은) 수를 미리 더하고, 그 앞까지만 2개씩 묶어서 계산한다.
					// [3, 2, 1] -> 1은 더하고, 3*2 진행
					ans += pos.get(posSize-1);
					posSize--;
				}
				for(int i = 0; i < posSize; i += 2) {
					int first = pos.get(i);
					int second = pos.get(i+1);
					// 둘 중 하나가 1이라면 곱하는 것 보다 더하는게 더 큰 값이 나온다.
					if (first == 1 || second == 1) ans += first + second;
					else ans += first * second;
				}
			} else ans += pos.get(0);  // 1개만 있다면 그냥 더한다.
		}
		if (!neg.isEmpty()) {
			int negSize = neg.size();
			if (negSize >= 2) {
				neg.sort(Comparator.naturalOrder()); // 수의 절대값이 큰 값이 앞으로 오도록 정렬한다.
				if (negSize % 2 == 1) {
					// 음수가 홀수개인 경우, 0이 있다면 가장 절대값이 작은 음수와 곱해서 0을 더한 처리를 하면 된다.
					// 이것은 0을 더하는 행위와 같으므로 따로 코드가 필요없다.
					// 하지만 0이 없다면 어쩔 수 없이 음수 값을 더해야한다.
					
					// priorityqueue를 쓰지 않고, 배열로 했기 때문에 remove를 하면 시간이 오래걸릴 것 같아서
					// 순회하는 수를 줄여주기 위해 홀수인 경우 1개를 덜 보도록 하기 위해 negSize를 줄였다.
					// 그리고 0의 개수는 중요하지 않다. 있기만 하면 된다. 
					// 음수가 홀수인 경우 0이 딱 하나 필요하다.
					if (!isZero) ans += neg.get(negSize-1);
					negSize--;
				}
				for(int i = 0; i < negSize; i += 2) {
					int first = neg.get(i);
					int second = neg.get(i+1);
					// 음수끼리 곱하면 양수가 되니깐!
					ans += first * second;
				}
			} else if (!isZero) ans += neg.get(0);
		}
		
		System.out.println(ans);
		
		
	}

}
