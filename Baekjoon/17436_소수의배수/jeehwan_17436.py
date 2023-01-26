'''



소수?!
1과 자기 자신 외의 약수를 가지지 않는 1보다 큰 자연수

즉, 양의 약수가 1과 자신뿐인 2개로 구성된 자연수



포함배제의 원리?????

이 문제 뭐야...?!

겹치는 부분이 홀수면 더하고, 겹치는 부분이 짝수면 뺀다.


모르겟다...!
'''

#풀이1
# 17436번 소수의 배수
# 포함 배제의 원리
from itertools import combinations
N, M = map(int, input().split())
primes = list(map(int, input().split()))
total = 0
for i in range(1, N+1):
    for tpl in combinations(primes, i):
        print(tpl)
        k = 1
        for prime in tpl:
            print(prime)
            k *= prime
        if i % 2 == 0:
            total -= (M//k)
        else:
            total += (M//k)
print(total)


#풀이2

# [N, M] = list(map(int, input().split()))
# primes = list(map(int, input().split()))
#
#
# def count_fast(n):
# 	count = 0
# 	stack = [(1, 0, 1)]
# 	while stack:
# 		(sign, index, accumulation) = stack.pop()
# 		if index >= len(primes) or (accumulation * primes[index]) > n:
# 			continue
# 		count += sign * (n // (accumulation * primes[index]))
# 		stack.append((sign, index + 1, accumulation))
# 		stack.append((-sign, index + 1, accumulation * primes[index]))
# 	return count
#
# print(count_fast(M))



#풀이3

# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split(' '))
# li = list(map(int, input().split(' ')))
#
#
# cnt = 0
# for size in range(1, n+1):
#     if size % 2 == 1:
#         for i in combinations(li, size):
#             tmp = 1
#             for j in i:
#                 tmp *= j
#             cnt += m // tmp
#     else:
#         for i in combinations(li, size):
#             tmp = 1
#             for j in i:
#                 tmp *= j
#             cnt -= m // tmp

#print(cnt)