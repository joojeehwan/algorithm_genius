import sys


n, m = map(int, sys.stdin.readline().split())  # 집합을 이루는 문자열의 수, 입력 문자열 수
arr = {}
for _ in range(n):
    arr[sys.stdin.readline().strip()] = True
cnt = 0
for _ in range(m):
    if sys.stdin.readline().strip() in arr.keys():
        cnt += 1
print(cnt)