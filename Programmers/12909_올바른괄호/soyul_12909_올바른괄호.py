def solution(s):

    stack = []

    # ( 면 스택에 넣고 ) 면 스택에서 뺀다
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if stack:
                stack.pop(-1)
            else:                       # 스택에서 빼야할 차례인데 뺄 수 없을 경우는 바로 false 반환
                return False

    # 끝까지 실행했는데 만약 스택에 무언가 남아있다면 false
    if stack:
        return False

    return True
