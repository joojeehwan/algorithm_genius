/* 해결되지 않는 경우를 단순히 두 큐의 길이의 2배로 하면 틀린다.
    예시 ) [1, 1, 1, 1, 1], [1, 1, 1, 9, 1] 기댓값 〉12
    그렇다면 최대값은 몇? 2를 1에 다 넣고 그 1을 다시 2에 넣는 경우... *3...
*/

import java.util.Arrays;
import java.util.LinkedList;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        int maximum = queue1.length * 3;
        
        LinkedList<Integer> a = new LinkedList<>(Arrays.stream(queue1).boxed().collect(Collectors.toList()));
        LinkedList<Integer> b = new LinkedList<>(Arrays.stream(queue2).boxed().collect(Collectors.toList()));
        long aSum = a.stream().mapToLong(Integer::longValue).sum();
        long bSum = b.stream().mapToLong(Integer::longValue).sum();
        long goal =  (aSum + bSum) / 2;
        
        int e;
        while (aSum != bSum && answer < maximum) {
            if (aSum > bSum) {
                e = a.pop();
                aSum -= e;
                b.add(e);
                bSum += e;
            } else {
                e = b.pop();
                bSum -= e;
                a.add(e);
                aSum += e;
            }
            answer++;
        }
        
        if (answer >= maximum) answer = -1;
        
        return answer;
    }
}