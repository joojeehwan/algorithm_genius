/*
 * https://ddingmin00.tistory.com/82
 * 하... 이 간단한 문제에 시간을 얼마나 쓴거야..
 * 어떻게 개선해야할지도 모르겠어..
 * 애초에 내가 생각한 방법은 시간 초과가 나는 방법이었고..
 * 이 간단한걸 왜 생각하지 못 했을까?
 * */

public class HE150369 {
	
	public static long solution(int cap, int n, int[] deliveries, int[] pickups) {
		long answer = 0;
		int delivery = 0;
        int pickup = 0;
        
        for(int i = n-1; i >= 0; i--) {
        	// 매번 집에서 배달, 수거 동시에 진행
        	// cap을 매번 빼주면서 갱신할 필요가 없다.
            delivery += deliveries[i];
            pickup += pickups[i];
            // 혹시 물류창고에 돌아가야하는지 확인한다.
            while(delivery > 0 || pickup > 0) {
                delivery -= cap;
                pickup -= cap;
                // delivery나 pickup이 음수가 되면, 다음 집의 것을 미리 처리한 셈이다. 
                answer += (i + 1) * 2;
            }
        }
        return answer;
    }
}