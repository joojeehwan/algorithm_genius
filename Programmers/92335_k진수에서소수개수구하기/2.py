def prime(num):
    for i in range(2, int(num ** (1/2) + 1)):
        if num % i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    
    tnl = []
    while n > 0:
        tnl.append(str(n % k))
        n //= k
    tnl = tnl[::-1]
    tns = ''.join(tnl)
    stack = []
    p = 0
    while p < len(tns):
        stack.append(tns[p])
        if tns[p] == '0':
            stack.pop()
            if any(stack):
                check = int(''.join(stack))
                if check >= 2 and prime(check):
                    answer += 1
            stack.clear()
        p += 1
    if any(stack):
        check = int(''.join(stack))
        if check >= 2 and prime(check):
            answer += 1
    
    return answer