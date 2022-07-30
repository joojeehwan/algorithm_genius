import sys

n, m = map(int, sys.stdin.readline().split())

name_list = {}

# 듣도 못한 사람으로 딕셔너리를 만듬
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    name_list[name] = 1

# 보도 못한 사람들의 리스트가 듣도 못한 사람들 리스트 안에 있는지 검사
cnt = 0
answer = []
for _ in range(m):
    name = sys.stdin.readline().rstrip()
    if name in name_list:
        cnt += 1
        answer.append(name)

print(cnt)
for ans in sorted(answer):
    print(ans)