package programmers;

import java.util.ArrayList;


class HE1830_1 {
	static String rule1(String sentence) {
        String result = "";
        if (sentence.length() < 3) return "false";
        
        char lowercase = sentence.charAt(1);
        boolean lowerExist = false;
            
        for(int i = 0; i < sentence.length(); i++) {
            // 소문자가 존재하는지 확인한다.
            if(Character.isLowerCase(sentence.charAt(i))) lowerExist = true;
            
            if(i % 2 == 0) {
                // 대문자들의 자리에 소문자가 있다면 안된다.
                if(Character.isLowerCase(sentence.charAt(i))) return "false";
                // 대문자면 계속 추가하고
                result += String.valueOf(sentence.charAt(i));
            }
            // 못 보던 다른 특수문자가 나오면 안된다.
            else if (lowercase != sentence.charAt(i)) return "false";
        }
        
        // 소문자가 없으면 안된다.
        if(!lowerExist) return "false";
        return result;
    }
    
    static String allUpper(String sentence) {
        String result = "";
        for(char letter : sentence.toCharArray()) {
            if(!Character.isUpperCase(letter)) return "false";
            result += String.valueOf(letter);
        }
        return result;
    }
    
    
    
    public static String shiiiit(String sentence) {
        String answer = "";
        boolean[] mark = new boolean[26];
        
        while(!sentence.isEmpty()) {
            String result = "";
            ArrayList<Integer> lowers = new ArrayList<Integer>();
            
            // 시작이 소문자인 경우
            if(Character.isLowerCase(sentence.charAt(0))) {
                // 이미 사용한 소문자
                if (mark[sentence.charAt(0) - 'a']) return "invalid";
                mark[sentence.charAt(0) - 'a'] = true;
                
                for(int i = 0; i < sentence.length(); i++) {
                    // 소문자라면 위치 저장
                    if(sentence.charAt(i) == sentence.charAt(0)) lowers.add(i);
                }
                
                // 2개 아니면 소문자로 시작할 수 없음
                if(lowers.size() != 2) return "invalid";
                
                // 가운데 문자열만 체크한다.
                // 규칙 2만 있는지, 1도 섞여있는지
                String needCheck = sentence.substring(1, lowers.get(1));
                if (needCheck.isEmpty()) return "invalid";
                
                // 1번 규칙을 만족하는가?(소문자가 제대로 있는가?)
                result = rule1(needCheck);
                
                if(result.equals("false")) {
                    // 그럼 다 대문자냐?
                    result = allUpper(needCheck);
                    // 그것 마저도 아니라면..
                    if (result.equals("false")) return "invalid";
                }
                else {
                    //rule1을 만족한다면, 같은 소문자가 또 나온건 아닌지 보자.
                    if(mark[sentence.charAt(2) - 'a']) return "invalid";
                    mark[sentence.charAt(2) - 'a'] = true;
                }
                // 뒤 소문자까지 짜르고 업데이트
                sentence = sentence.substring(lowers.get(1)+1);
            }
            else {
                // 대문자만 있을 때 한 글자씩 추가한다.
                if (sentence.length() == 1 || Character.isUpperCase(sentence.charAt(1))) {
                    result += String.valueOf(sentence.charAt(0));
                    sentence = sentence.substring(1);
                } else {
                    // 찾는 소문자에 대해서만 위치를 저장한다.
                    for(int i = 0; i < sentence.length(); i++) {
                        if(sentence.charAt(1) == sentence.charAt(i)) lowers.add(i);
                    }
                    
                    // 소문자가 2개가 아니라면
                    if(lowers.size() != 2) {
                        // 소문자의 마지막 위치가, 문장의 마지막 위치라면 불가능하다.
                        if(lowers.get(lowers.size()-1) == sentence.length()-1) return "invalid";
                        // 소문자 다음이 대문자가 아니라면, 불가능하다.
                        if(Character.isLowerCase(sentence.charAt(lowers.get(lowers.size()-1)+1))) return "invalid";
                        
                        // 고쳐야하는 문장 따로 뺌
                        String needFix = sentence.substring(0, lowers.get(lowers.size()-1)+2);
                        result = rule1(needFix);
                        
                        if(result.equals("false")) return "invalid";
                        if(mark[sentence.charAt(1) - 'a']) return "invalid";
                        mark[sentence.charAt(1) - 'a'] = true;
                        
                        // 자른 뒷 부분으로 갈아끼운다.
                        sentence = sentence.substring(lowers.get(lowers.size()-1)+2);
                    }
                    // 2개 짜리라면
                    else {
                        // 그냥 앞에만 떼어버린다.
                        result = String.valueOf(sentence.charAt(0));
                        sentence = sentence.substring(1);
                    }
                }
            }
            // 자른거 추가해준다.
            answer += result + " ";
        }
        answer = answer.stripTrailing();
        return answer;
    }
}
