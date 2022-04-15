import sys

def check(i, j):
    while i < j:
        if st[i] != st[j]:
            return 1
        i += 1
        j -= 1
    return 2

T = int(sys.stdin.readline())
for _ in range(T):
    st = sys.stdin.readline().rstrip()

    i = 0
    j = len(st) - 1
    cnt = 0
    flag = 0
    while i < j:
        if cnt:
            break
        if st[i] != st[j]:                     # 다른 문자가 나왔다면
            cnt += 1
        if cnt == 1:                            # 만약 다른 게 나왓으면 유사 회문이 되는지 확인
            if st[i+1] == st[j]:                # flag가 1이면 유사회문 안됨 2면 유사 회문 됨
                flag = check(i+1, j)
            if flag != 2 and st[i] == st[j-1]:      # 아직 유사 회문 확인 안되었지만 가능성이 있다면
                flag = check(i, j-1)
        if flag == 2:
            cnt -= 1
            break
        i += 1
        j -= 1

    if cnt == 1:                # 회문이 안되면
        print(2)
    else:
        if flag == 0:           # 회문이면
            print(0)
        if flag == 2:           # 유사회문이면
            print(1)