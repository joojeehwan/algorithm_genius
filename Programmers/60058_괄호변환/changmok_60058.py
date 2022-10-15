def solution(p):

    right = isRight(p)

    if right:
        answer = p
    else:
        answer = doCycle(p)

    return answer

def doCycle(p):
    if p == '':
        return ''
    u, v = splitString(p)
    if isRight(u):
        return u + doCycle(v)
    else:
        s = '(' + doCycle(v) + ')'
        s += flip(u[1:len(u)-1])
        return s

def flip(p):
    flipper = {'(':')', ')':'('}
    flipped = ''
    for c in p:
        flipped += flipper[c]
    return flipped

def isRight(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return True

def splitString(p):
    counter = {'(':0, ')':0}
    for c in p:
        counter[c] += 1
        if counter['('] == counter[')']:
            return p[:counter['(']*2], p[counter['(']*2:]


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
print(solution(""))