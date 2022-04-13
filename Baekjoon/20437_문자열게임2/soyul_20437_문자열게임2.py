import sys

T = int(sys.stdin.readline())
for _ in range(T):
    w = sys.stdin.readline()
    k = int(sys.stdin.readline())

    check = [[] for _ in range(26)]

    for i in range(len(w) - 1):
        check[ord(w[i]) - 97].append(i)                 # idx 집어넣기

    min_value = len(w)
    max_value = 0
    for i in range(26):
        if len(check[i]) >= k:                         # k개 이상인 알파벳이면
            for j in range(len(check[i])-k+1):            # min 계산, max 계산
                min_value = min(min_value, check[i][j + k - 1] - check[i][j] + 1)
                max_value = max(max_value, check[i][j + k - 1] - check[i][j] + 1)

    if max_value == 0:
        print(-1)
    else:
        print(min_value, max_value)