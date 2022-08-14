'''

분할 정복?! 흠흠



0, 0 부터 본다.


와 이거 이해가 어렵네

개념 설명 조금 친절하게 적어 놓은 블로그들.
https://mygumi.tistory.com/284

https://ggasoon2.tistory.com/11


r, c 를 사분면 마다 다르게 빼주는 이유는?!

큰 사이즈에서 작은 사이즈로 줄여갈수록, 처음의 큰 사분면의 위치에서,

분할에서 작아졌을떄의 r,c 의 좌표가 바뀌기 때문에

사분면에 맞게 계속 r, c를 뺴주는 것

ex)

n = 3일때의

7, 7의 좌표는 분할에서 4분면이 작아질 수 록,

3, 3

1, 1 로 내가 찾고자 하는 값이 바뀐다.


어느 사분면에 위치하는 지 안다면, 사분면까지의 좌표값을 더해서 현재 위치를 구한다.

마이구미 블로그 예시 확인


이거 수학 문제네
'''

#반복문 풀이
n, r, c = map(int, input().split())


ans = 0

while n != 0:

    n -= 1 # 여기서 바로 n이 하나 줄고 시작
    size = 2 ** n

    # 1사분면

    if r < size and c < size:
        ans += (2 ** n) * (2 ** n) * 0


    # 2사분면

    elif r < size and c >= size:
        ans += (2 ** n) * (2 ** n) * 1
        c -= size

    # 3사분면
    elif r >= size and c < size:
        ans += (2 ** n) * (2 ** n) * 2
        r -= size

    else:

        ans += (2 ** n) * (2 ** n) * 3
        r -= size
        c -= size

print(ans)




# dfs 풀이 // 메모리 초과


import sys
sys.setrecursionlimit(10**7)

N, r, c = map(int, sys.stdin.readline().split())


def dfs(N, r, c) -> int:

    if N == 0:
        return 0

    mid = 2 ** N // 2

    if r < mid and c < mid:
        return dfs(N - 1, r, c) + mid ** 2 * 0

    elif r >= mid and c < mid:
        return dfs(N - 1, r - mid, c) + mid ** 2 * 1

    elif r < mid and c >= mid:
        return dfs(N - 1, r, c - mid) + mid ** 2 * 2

    elif r >= mid and c >= mid:
        return dfs(N - 1, r - mid, c - mid) + mid ** 2 * 3

    return 0

print(dfs(N, c, r))


#dfs ver 2

import sys

N, r, c = map(int, sys.stdin.readline().split())

def dfs(N, r, c):


    size = 2 ** (N - 1)

    if N == 1:
        if (r == 0 and c == 0):
            return 0
        elif (r == 0 and c == 1):
            return 1
        elif (r == 1 and c == 0):
            return 2
        else:
            return 3

    else:
        if (r < size and c < size):
            return dfs(N - 1, r, c)

        elif (r < size and c >= size):

            return (2 ** (2 * (N - 1))) * 1 + dfs(N - 1, r, c - size)

        elif (r >= size and c < size):

            return (2 ** (2 * (N - 1))) * 2 + dfs(N - 1, r - size, c)

        else:

            return (2 ** (2 * (N - 1))) * 3 + dfs(N - 1, r - size, c - size)


print(dfs(N, r, c))

