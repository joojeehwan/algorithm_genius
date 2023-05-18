'''

정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

'''

# 무작정 머리속에 든 생각 풀이
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst1 = list(map(int, input().split()))

lst2 = list(map(int, input().split()))

lst3 = lst1 + lst2

lst3.sort()

#map을 통해 리스트 안의 값들을 하나씩 빼는 것도 가능하지..! 위에서 받는 것 처럼
answer = " ".join(map(str, lst3))

print(answer)

# 투 포인터 풀이1 https://velog.io/@uoayop/BOJ-11728-%EB%B0%B0%EC%97%B4-%ED%95%A9%EC%B9%98%EA%B8%B0Python

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
ai = 0
bi = 0
answer = []
while 1:
    if arr_a[ai] <= arr_b[bi]:
        answer.append(arr_a[ai])
        ai += 1
    else:
        answer.append(arr_b[bi])
        bi += 1
    if ai == N or bi == M:
        answer += arr_a[ai:] + arr_b[bi:]
        break
print(*answer)

# 투 포인터 풀이 2

import sys

input = sys.stdin.readline

n, m = map(int, input().rsplit())

a = list(map(int, input().rsplit()))
b = list(map(int, input().rsplit()))

l, r = 0, 0
result = []
while l < n and r < m:
    if a[l] < b[r]:
        result.append(a[l])
        l += 1
    else:
        result.append(b[r])
        r += 1

while l < n:
    result.append(a[l])
    l += 1

while r < m:
    result.append(b[r])
    r += 1

print(" ".join(map(str, result)))