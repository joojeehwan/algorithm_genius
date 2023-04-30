package Programmers;

import java.util.LinkedList;
import java.util.Queue;

/**
 * 42892
 * @두 큐 합 같게 만들기
 * */

public class Eunju_118667 {
    public static class Solution {
        public int solution(int[] queue1, int[] queue2) {
            int answer = -2;
            long sum1=0, sum2=0;
            long halfSum = 0;

            Queue<Integer> q1= new LinkedList<>();
            Queue<Integer> q2= new LinkedList<>();


            //인풋 받을때 큐 자료구조에 넣어주기(배열-> 큐)
            for(int i=0; i<queue1.length; i++){
                //halfsum 만들려고
                sum1+=queue1[i];
                sum2+=queue2[i];

                q1.add(queue1[i]);
                q2.add(queue2[i]);
            }

            //목표값 : 두 큐 합의 절반 저장하기
            halfSum = (sum1+sum2)/2;

            //break 조건 : 모든 값을 insert pop 반복해도 Q1, Q2가 같아지지 않는 경우 존재 => 최대 횟수 필요
            // 두 큐 합이 같아질 수 있다는 전제에
            // 큐를 반복해서 넣었다 뺐다 하는 횟수는 queue1.length*3;
            int maxCount = queue1.length*3-1;

            int cnt=0; //반복 작업 횟수

            //Q1의 합을 기준으로 push, pop 작업
            while(sum1 != halfSum){
                //최대 작업 횟수를 초과하면 멈추기
                if(cnt >maxCount) break;

                //현재Q1의 합이 목표값보다 크면
                if(sum1 > halfSum){
                    int num = q1.poll(); sum1-=num; //Q1에서 pop하기
                    q2.add(num);
                }
                //현재Q1의 합이 목표값보다 작으면 Q2맨 뒤의 값 가져오기
                else{
                    int num = q2.poll(); sum1+=num;
                    q1.add(num);
                }
                cnt+=1;
            }

            //최대로 작업을 반복해서 해도 값이 안나오면 -1 리턴
            return cnt > maxCount ? -1 : cnt;
        }
    }

    public static void main(String[] args) {

        Solution solution = new Solution();
        int[] queue1 = {3, 2, 7, 2};
        int[] queue2 = {4, 6, 5, 1};

        int ans = solution.solution(queue1, queue2);
        System.out.println(ans);
    }
}