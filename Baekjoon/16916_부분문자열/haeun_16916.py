import sys

# sys.stdin = open('input.txt', 'r')

S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()


len_S, len_P = len(S), len(P)
pattern = [0] * len_P
idx_pattern = 1
cnt = 0

while idx_pattern < len_P:
    if P[idx_pattern] == P[cnt]:
        cnt += 1
        pattern[idx_pattern] = cnt
        idx_pattern += 1
    else:
        if cnt:
            cnt = pattern[cnt-1]
        else:
            pattern[idx_pattern] = 0
            idx_pattern += 1


idx_S, idx_P = 0, 0
found = False

while not found and idx_S < len_S:
    if P[idx_P] == S[idx_S]:
        idx_P += 1
        idx_S += 1
        if idx_P == len_P:
            found = True
    else:
        if idx_P == 0:
            idx_S += 1
        idx_P = pattern[idx_P-1]


print(int(found))