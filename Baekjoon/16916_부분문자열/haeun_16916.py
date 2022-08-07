import sys

sys.stdin = open('input.txt', 'r')

S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

len_S, len_P = len(S), len(P)
pattern = [0] * len_P
j = 0

# 패턴 배열 만들기 j = 접두사 포인터
for i in range(1, len_P):
    # 같은걸 만나는 순간까지 돌아야한다.
    # j가 0이고 일치하지 않는 경우 무한 루프를 돌지 않도록.
    while j > 0 and P[i] != P[j]:
        j = pattern[j-1]
    # j의 값에서 1을 더한 만큼의 문자열의 개수가 일치한다.
    j += 1
    pattern[i] = j

# print(pattern)

idx_P = 0
found = False

# idx_S 는 절대 앞으로 가지 않는다. 앞으로 가는건 idx_P 뿐이다.
for idx_S in range(len_S):
    while idx_P > 0 and S[idx_S] != P[idx_P]:
        # 두 문자가 일치하지 않는 경우
        # idx_P는 직전에 일치했던 위치 기준으로
        # 어디로 이동해야할지 알 수 있다.
        idx_P = pattern[idx_P-1]
    # 두 문자가 일치하는 경우
    if idx_P == len_P-1:
        found = True
        break
    idx_P += 1

print(int(found))