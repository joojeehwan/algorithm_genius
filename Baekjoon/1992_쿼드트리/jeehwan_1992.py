'''

범위를 정해주고, 그 범위 안에서, 한개라도 다른 것(0 or 1)이 있다면, 다시 4분면으로 나누어 검색

이 때, 4분면으로 나눌 때 괄호

'''

n = int(input())

MAP = [list(map(int, input())) for _ in range(n)]

ans = []

#print(MAP)
def solve(row, col, width) :

    global ans
    color = MAP[row][col]

    for i in range(row, row + width) :
        for j in range(col, col + width) :

            if MAP[i][j] != color :
                ans.append("(")
                solve(row, col, width // 2)   # 사분면 속 좌상단
                solve(row, col + width // 2, width // 2) # 사분면 속 우상단
                solve(row + width // 2, col, width // 2) # 사분면 속 좌하단
                solve(row + width // 2, col + width // 2 , width // 2 ) #사분면 속 우하단
                ans.append(")")
                return
    ans.append(color) #범위안의 모든 수가 같은 경우 check

solve(0, 0, n)

print(''.join(map(str, ans)))

