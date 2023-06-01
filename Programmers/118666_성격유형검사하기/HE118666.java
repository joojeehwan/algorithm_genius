import java.util.HashMap;

class Solution {
    public String solution(String[] survey, int[] choices) {
        StringBuilder sb = new StringBuilder();
        int cnt = survey.length;
        char[] types = {'R', 'T', 'C', 'F', 'J', 'M', 'A', 'N'};
        HashMap<Character, Integer> result = new HashMap<>();
        for(char t : types) {
            result.put(t, 0);
        }
        
        for (int idx = 0; idx < cnt; idx++) {
            int choice = choices[idx] - 4;
            char type1 = survey[idx].charAt(0);
            char type2 = survey[idx].charAt(1);
            if (choice == 0) continue;
            if (choice < 0) {
                // 비동의 -> type1
                result.put(type1, result.get(type1) + Math.abs(choice));
            } else {
                // 동의 -> type2
                result.put(type2, result.get(type2) + choice);
            }
        }
        
        sb.append((result.get('R') >= result.get('T')? "R" : "T"));
        sb.append((result.get('C') >= result.get('F')? "C" : "F"));
        sb.append((result.get('J') >= result.get('M')? "J" : "M"));
        sb.append((result.get('A') >= result.get('N')? "A" : "N"));
        
        
        return sb.toString();
    }
}