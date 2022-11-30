from collections import deque


def is_right_str(q):
    temp = []
    for i in range(len(q)):
        now = q[i]
        if now == '(':  # '('
            temp.append(now)
        else:  # ')'
            if not temp:  # '('가 없는데 ')'가 나옴
                return 0
            temp.pop()
    if temp:  # ')'가 없는데 '('가 남음
        return 0
    return 1


def divide(q):
    temp = [0, 0]
    for i in range(len(q)):
        if q[i] == '(':
            temp[0] += 1
        else:
            temp[1] += 1
        if temp[0] == temp[1]:  # 균형잡인 문자열
            return q[:i+1], q[i+1:]


def flip(q):
    temp = ''
    for i in range(len(q)):
        if q[i] == '(':
            temp += ')'
        else:
            temp += '('
    return temp


def solution(p):
    if not is_right_str(p):  # "올바른 괄호 문자열" 이면
        u, v = divide(p)
        if is_right_str(u):  # u가 "올바른 괄호 문자열"이면
            return u + solution(v)
        else:  # u가 "올바른 괄호 문자열"이 아니면
            return '(' + solution(v) + ')' + flip(u[1:-1])
    return p


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))