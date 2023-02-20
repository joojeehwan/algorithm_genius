package programmers;


import java.util.ArrayList;

public class HE1830 {
static String answer;
	// 이미 사용한 소문자인지 확인한다.
static boolean[] marks;
static ArrayList<Integer> lowers;
static boolean only;

	// 소문자의 개수를 센다.
	static int countLower(String st, char mark) {
		int otherIdx = st.length();
		if (marks[mark - 'a']) return -1;
        marks[mark - 'a'] = true;
        
		lowers = new ArrayList<Integer>();
		
		for(int i = 0; i < st.length(); i++) {
			if (st.charAt(i) == mark) lowers.add(i);
			else if (Character.isLowerCase(st.charAt(i))) otherIdx = Math.min(i, otherIdx);
			if (lowers.size() > 2 && i % 2 == 0 && Character.isLowerCase(st.charAt(i))) return -1;
		}
		
		if (lowers.size() == 2 && otherIdx < lowers.get(1)) only = false;
		
		return lowers.size();
	}
    
    // 1번 규칙이 적용되어있는지 판단한다.
    // 올바를 경우 마지막 인덱스를, 아닐경우 -1을 반환한다.
//    static int isRule1(String st, char mark) {
//        if (marks[mark - 'a']) return -1;
//        marks[mark - 'a'] = true;
//        
//        for(int idx = 2; idx < st.length(); idx++) {
//        	System.out.println(st.charAt(idx));
//            // 짝수는 대문자
//        	if(idx % 2 == 0 && Character.isLowerCase(st.charAt(idx))) return -1;
//        	// 홀수는 소문자
//        	if(idx % 2 == 1 && Character.isUpperCase(st.charAt(idx))) return idx;
//        	if(idx % 2 == 1 && Character.isLowerCase(st.charAt(idx)) && st.charAt(idx) != mark) return idx;
//        	if(idx == st.length()-1 && Character.isUpperCase(st.charAt(idx))) return idx+1;
//        }
//        return -1;
//    }
    
    // 1번 규칙에 맞춰 소문자들을 제거한다.
    static String rule1Fix(String st, char mark, int lastIdx) {
        if (lastIdx == st.length()-1) return "invalid";
    	String fix = "";
        for(int i = 0; i <= lastIdx+1; i++) {
        	if (Character.isUpperCase(st.charAt(i))) fix += String.valueOf(st.charAt(i));
        	else {
        		if (mark != st.charAt(i)) return "invalid";
        	}
        }
        answer += fix + " ";
        return st.substring(lastIdx+2);
    }
    
    // 2번 규칙이 적용되어있는지 판단한다.
    // 올바를 경우 소문자를 제외한 마지막 인덱스를, 아닐경우 -1을 반환한다.
    static int isRule2(String st, char mark) {
        if (marks[mark - 'a'] || Character.isLowerCase(st.charAt(1))) return -1;
        marks[mark - 'a'] = true;
        
        for(int idx = 1; idx < st.length(); idx++) {
            if (st.charAt(idx) == mark) return idx;
        }
        return -1;
    }
    
 // 2번 규칙에 맞춰 소문자들을 제거한다.
    static String rule2Fix(String st, int idx) {
    	// 소문자를 뗀 문자들
        String trimed = st.substring(1, idx);
        // 앞에 단어를 뗀 문자들
        String left = st.length() >= idx+1 ? st.substring(idx+1) : "";
        
        boolean allCap = true;
        for(char ch : trimed.toCharArray()) {
        	if(Character.isLowerCase(ch)) {
        		allCap = false;
        		break;
        	}
        }
        // 소문자를 제거한답시고 한게 정말 대문자만 남았다면, 정답에 추가한다.
        // 아니라면 규칙1이 적용되어있을 수 있어서 다시 기존 sentence에 추가하고 이후 과정을 거친다.
        if(allCap) {
        	answer = answer + trimed + " ";
        	return left;
        }
        else return trimed + left;
    }
    
    public static String solution(String sentence) {
        answer = "";
        marks = new boolean[26];
        
        // 규칙이 적용되지 않은 대문자들을 합해준다.
        String capitals = "";
        
        // 입력된 문장을 다 쓸때까지 점검한다.
        // 점검하면서 sentence는 앞에서부터 줄어든다.
        while(!sentence.isBlank()) {
            // 현재 문장의 첫 번째가 소문자일 경우, 규칙 2일 가능성이 있다.
            if(Character.isLowerCase(sentence.charAt(0))) {
                if(!capitals.isBlank()) {
                    // 현재까지 모인 대문자들을 정답에 추가해주고 작업한다.
                    answer += capitals + " ";
                    capitals = "";
                }
                // 규칙 2번이 제대로 적용되어있는지 확인한다.
                int idx = isRule2(sentence, sentence.charAt(0));
                // System.out.println(idx);
                if (idx > 0) {
                	sentence = rule2Fix(sentence, idx);
                } else return "invalid";
            }
            if (sentence.isEmpty()) break;
            // 현재 문장의 첫 번째가 대문자일 경우, 규칙 1일 가능성이 있다.
            if (Character.isUpperCase(sentence.charAt(0))) {
            	// 다음이 소문자인 경우
                if(sentence.length() > 2 && Character.isLowerCase(sentence.charAt(1))) {
                	if(!capitals.isBlank()) {
                        // 현재까지 모인 대문자들을 정답에 추가해주고 작업한다.
                        answer += capitals + " ";
                        capitals = "";
                    }
                	// [@@@@@ 틀린 이유 @@@@@]
                	// 대문자 뒤에 소문자가 나왔다고 무조건 규칙1만 가능한게 아니다.
                	// 규칙 1,2를 판가름하기 위해 처음 찾은 소문자가 몇개나 등장하는지 확인해야한다.
                	only = true;
                    int cnt = countLower(sentence, sentence.charAt(1));
                    if (cnt == 2) {
                    	if (only) {
                    		sentence = rule1Fix(sentence, sentence.charAt(1), lowers.get(lowers.size()-1));
                    	}
                    	else {
                    		answer += sentence.substring(0, 1) + " ";
                    		sentence = rule2Fix(sentence.substring(1), lowers.get(1)-1);
                    	}
                    	if (sentence.equals("invalid")) return "invalid";
                    } 
                    else if (cnt > 0) {
                    	sentence = rule1Fix(sentence, sentence.charAt(1), lowers.get(lowers.size()-1));
                    	if (sentence.equals("invalid")) return "invalid";
                    } else return "invalid";
                }
                else {
                	// 계속 대문자가 이어진다면, 한 단어이므로 한자리씩 잘라나간다.
                    capitals += sentence.substring(0, 1);
                    sentence = sentence.substring(1);
                }
            } 
            // 둘다 아니라면(공백) 이상한 광고문이다.
            else return "invalid";
        }
        // 규칙이 적용되지 않은 단어인 경우, 위의 과정에서 추가해주는 부분이 없어서
        // 혹시 모르니 마지막에 정답에 남은 대문자들을 추가해줬다.
        // 없으면 아무것도 안붙으니깐 상관없음.
        answer += capitals;
        answer = answer.stripTrailing();
        
        
        return answer;
    }

	public static void main(String[] args) {
		String[] inputs = {"HaEaLaLaObWORLDb", "SpIpGpOpNpGJqOqA", "AxAxAxAoBoBoB",
				"aIaAM", "AAAaBaAbBBBBbCcBdBdBdBcCeBfBeGgGGjGjGRvRvRvRvRvR", "aaA",
				"Aaa", "HaEaLaLaOWaOaRaLaD", "aHELLOWORLDa",
				"HaEaLaLObWORLDb", "HaEaLaLaObWORLDb", "aHbEbLbLbOacWdOdRdLdDc",
				"abAba", "HELLO WORLD", "xAaAbAaAx",
				"AbAaAbAaCa", "AbAaAbAaC"
				};
		String[] answers = {"HELLO WORLD", "SIGONG JOA", "invalid",
				"I AM", "AAA B A BBBB C BBBB C BB GG G G G RRRRRR\nor    AA ABA BBBB C BBBB C BB GG GGG RRRRRR", "invalid",
				"invalid", "invalid", "HELLOWORLD",
				"HELL O WORLD", "HELLO WORLD", "HELLO WORLD",
				"invalid", "invalid", "invalid",
				"invalid", "invalid"
				};
		
		for(int i = 0; i < inputs.length; i++) {
			String result = HE1830_1.shiiiit(inputs[i]);
			System.out.println("내 결과 = " + result);
			System.out.println("정답 = " + answers[i]);
			System.out.print("일치 여부 : = ");
			if (result.equals(answers[i])) System.out.println("O");
			else System.out.println(">>>>>>>>>> X <<<<<<<<<< ");
			System.out.println("----------------------------------");
		}
		
	}

}
