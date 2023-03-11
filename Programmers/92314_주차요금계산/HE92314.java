import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.TreeMap;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        int oTime = fees[0]; // 기본 시간
        int oFee = fees[1];  // 기본 요금
        int aTime = fees[2]; // 단위 시간
        int aFee = fees[3];  // 단위 요금
        
        StringTokenizer st; // records 문자열 parsing
        TreeMap<String, ArrayList<Integer>> recordMap = new TreeMap<>(); // key : 번호판, value = [분, 분, 분..]
        
        // 각 기록을 저장한다.
        // key : 차 번호, value = [분, 분, 분] => 입차-입차,출차-출차, 출차-입차는 없으므로 2개씩 자르면 된다.
        for(String record : records) {
            st = new StringTokenizer(record);
            String time = st.nextToken(); // HH:MM
            String car = st.nextToken(); // int로 했다가 0000 -> 0이 됨 ^^;;
            String type = st.nextToken(); // 신경 안씀.
            
            int hour = Integer.parseInt(time.substring(0, 2));
            int minute = Integer.parseInt(time.substring(3, 5));
            // String temp[] = time.split(":");
            
            // 이미 값이 있는 배열이 있다면 가져오고, 아니라면 생성한다.
            ArrayList<Integer> times = recordMap.getOrDefault(car, new ArrayList<Integer>());
            // 배열에 현재 시간을 추가하고, TreeMap에 저장한다.
            times.add(hour * 60 + minute);
            recordMap.put(car, times);
        }
        int[] answer = new int[recordMap.size()];
        int idx = 0;
        
        // 각 차별 요금 계산
        for (String car : recordMap.keySet()) {
            ArrayList<Integer> times = recordMap.get(car);
            int allTime = 0;
            int timeCnt = times.size();
            
            // 홀수인경우 마지막 1개를 보지 않기 위해 size()-1을 한다.
            for(int i = 0; i < timeCnt-1; i += 2) {
                allTime += times.get(i+1) - times.get(i);
            }
            // 당일 출차하지 않은 경우
            if(timeCnt % 2 == 1) {
                allTime += (23*60+59) - times.get(timeCnt-1);
            }
            
            // 요금 계산. 들어오면 일단 기본요금은 원래 낸다.
            int fee = oFee;
            
            // 1. 기본 시간을 넘겼는가?
            if (allTime > oTime) {
                allTime -= oTime; // 기본 시간을 빼고
                // 남은 시간을 단위시간으로 나누고 올림한 값으로 바꿈.
                allTime = (int) Math.ceil((double) allTime / aTime); 
                // Math.ceil 안쓰고 하는 법
                // cost += (time%fees[2] == 0 ? time/fees[2] : time/fees[2]+1)*fees[3];
                fee += allTime * aFee;
            }
            answer[idx++] = fee;
        }
        
        return answer;
    }
}