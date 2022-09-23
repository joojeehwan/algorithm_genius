def solution(p):

    # u와 v로 나누는 함수
    def divide(st):
        cnt_dict = {"(": 0, ")": 0}

        for i in range(len(st)):
            ch = st[i]
            cnt_dict[ch] += 1
            if cnt_dict["("] == cnt_dict[")"]:          # 괄호 갯수가 같아지면 나누기
                u = st[:i+1]
                v = st[i+1:]
                break

        return u, v

    # 올바른 괄호 문자열인지 확인하는 함수
    def check(u):

        stack = []

        for ch in u:
            if ch == "(":
                stack.append(ch)
            else:
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop(-1)

        return 1


    # 빈문자열인 경우 빈 문자열 반환
    if not p:
        return ""

    # 문자열을 u와 v로 나누기
    u, v = divide(p)

    # 올바른 괄호 문자열이라면 v 에 대해 1단계부터 수행한 후 u에 이어붙이기
    if check(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"

        # 앞 뒤를 짜르고 반대로 뒤집기
        for ch in u[1:len(u)-1]:
            if ch == "(":
                answer += ")"
            else:
                answer += "("
        return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

"""
'(' 와 ')' 로만 이루어진 문자열이 있을 경우, '(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열
그리고 여기에 '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부릅니다.

1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
"""