# import sys
# sys.stdin = open('input.txt', 'r')
"""
반례가 많은데 처리를 제대로 안해서 몇번 틀렸다.
그래도 반례찾는게 어렵지 않아서 다행이었다.
푼 시간 : 1시간 51분
메모리 : 61,960kb
실행시간 : 185ms

"""
T = int(input())

for tc in range(T):
    answer = 0
    N, X = map(int, input().split())
    grid = list(list(map(int, input().split())) for _ in range(N))

    for col in range(N):
        # 열을 행으로 만든다.
        trans_col = [0] * N
        for row in range(N):
            trans_col[row] = grid[row][col]
        grid.append(trans_col)

    for way in grid:
        prev, continuous, idx, possible = way[0], 1, 1, True
        while idx < N:
            step = way[idx]
            if step == prev:
                continuous += 1
            elif step == prev+1:
                # 지금와서 높아진 경우
                if continuous >= X:
                    continuous = 1
                else:
                    possible = False
                    break
            elif step == prev-1:
                # 지금와서 낮아진 경우
                # 남은게 별로 없다 -> 탈락
                if N - idx < X:
                    # 바로 슬라이싱하면 indexError나니까 이거부터 봐야됨
                    possible = False
                    break
                # 남긴 했는데 경사 만들어지기전에 높이 바뀐다.
                if way[idx:idx+X] != [step] * X:
                    possible = False
                    break
                # 한번에 X만큼 넘어가라
                idx += X - 1
                # 넘어간 위치에서 연속이면 1로 바뀜
                # 넘어간 위치에서 다른 숫자면 경사로가 부족해서 안됨
                continuous = 0
            else:
                # 무조건 탈락이야닌
                possible = False
                break
            # 탈락하지 않았다면 다음 index를 본다.
            idx += 1
            prev = step
        if possible:
            # print(f"{way} 는 가능하다네요!")
            answer += 1
        else:
            pass
            # print(f"{way} 는 불가능함")
    print(f"#{tc+1} {answer}")
