public class HE12980{
    
    /* 주어진 거리 N을 이진수로 변환합니다.
	 * 이진수로 변환된 N의 1의 개수를 세면, 이것이 점프로 이동해야 하는 횟수, 즉 건전지 사용량의 최솟값이 됩니다.
	 * 
	 * Integer.bitCount(n)를 사용하여 이진수에서 1의 개수를 세는 방법으로 건전지 사용량의 최솟값을 계산합니다. 
	 * 이진수에서 1의 개수가 곧 점프로 이동해야 하는 횟수이기 때문입니다. 
	 * */
	public int solution1(int n) {
		return Integer.bitCount(n);
	}
	
	public int solution2(int n) {
		int ans = 0;
        
        while (n > 0) {
            if (n % 2 == 1) {
                n -= 1;
                ans += 1;
            } else {
                n /= 2;
            }
        }

        return ans;
	}
}