from itertools import permutations

def solution(numbers):
    answer = 0
    length = len(numbers)
    primes = [True] * (10 ** length + 1)
    checked = [False] * (10 ** length + 1)
    
    primes[0] = False
    primes[1] = False
    
    for i in range(2, int((10 ** length) ** (1 / 2))+1):
        if not primes[i]:
            continue
        else:
            j = i * 2
            while j <= 10 ** length:
                primes[j] = False
                j += i
    
    for l in range(1, length + 1):
        strnums = permutations(numbers, l)
        for strnum in strnums:
            strnum = ''.join(strnum)
            num = int(strnum)
            if checked[num]:
                continue
            checked[num] = True
            if primes[num]:
                answer += 1
    
    return answer