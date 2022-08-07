def solution(s):
    queue = []
    s = list(s)[::-1]
    while s:
        now = s.pop(-1)
        if now == '(':  # 여는 괄호
            queue.append(now)
        elif now == ')':  # 닫는 괄호
            if not queue:  # 여는 괄호가 없음
                return False
            else:  # 여는 괄호가 있음
                queue.pop(-1)  # pop
    if queue:  # 여는 괄호가 남았음
        return False
    return True


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))