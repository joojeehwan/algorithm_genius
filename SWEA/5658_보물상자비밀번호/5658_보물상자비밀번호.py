T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    str = input()

    can = []

    # l 번 회전 가능
    l = len(str) // 4
    for i in range(l):
        str = (str[-1] + str)[:len(str)]            # 회전시킨 후
        for k in range(4):
            can.append(int(str[k * l: (k * l) + l], 16))                # 갯수만큼 잘라 16진수로 넣어줌

    can = set(can)
    ans = sorted(can, reverse=True)[K-1]

    print(f'#{tc+1} {ans}')