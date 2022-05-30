


'''

1. MAP에 종이의 상태를 저장하고 paper에 다섯 종류의 색종이를 각각 몇 장 사용했는지 저장한다

2. (0, 0)부터 시작해서 MAP[x][y]가 1인 모든 좌표에서 크기 1~5인 색종이를 붙여가면서 모든 케이스를 확인해야 한다

3. x좌표가 범위를 넘어가면 (0, y+1)로 재귀한다

   y가 범위를 넘어가면 맨 끝까지 탐색한 것이므로 최소값을 갱신한다

4. MAP[x][y]가 0이면 (x+1, y)로 재귀한다

   1이면 크기 1부터 5까지 색종이를 붙일 수 있는지 확인한다

5. 만약 색종이 5장을 이미 붙였거나 범위를 벗어나는 크기의 색종이라면 continue한다

6. 색종이를 붙일 수 있는지 확인한다. 단순히 반복문으로 0이 있는지 검사하면 된다

7. 붙일 수 있으면 다시 반복문으로 색종이를 붙이는 칸의 숫자를 0으로 바꿔준다

8. paper를 증가시켜 주고 (x+k+1, y)로 재귀한다

   그다음에는 paper와 지운 칸을 다시 되돌려준다

'''
import sys

input = sys.stdin.readline

def dfs(x, y, cnt):
    global ans

   #위에서 아래 다 본것!
    if y >= 10:
        ans = min(ans, cnt)
        return
    #범위를 벗어나니깐 아래로 내려가면서 왼쪽처음에서부터 시작
    if x >= 10:
        dfs(0, y + 1, cnt)
        return

    if MAP[x][y] == 1:
        #만약 색종이를 5장이미 붙엿거나, MAP의 범위를 벗어나는 크기의 색종이라면 continue
        #여기서 k는 색종이의 크기
        for k in range(5):
            if paper[k] == 5:
                continue
            if x + k >= 10 or y + k >= 10:
                continue

            flag = 0
            #색종이를 붙일 수 있는지 확인 => 반복문 / 온전한 사각형이어야지만! 붙일 수 있으니 이렇게 하는구나!
            # 그게 아니면 1x1를 붙여야 하니깐
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    if MAP[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break
            #온전하게 사각형 붙일 수 있다. 그러면 붙이는 칸의 숫자를 0으로 바꾼다.
            if not flag:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        MAP[i][j] = 0

                paper[k] += 1
                #그 다음 아래 칸으로 가!
                dfs(x + k + 1, y, cnt + 1)
                paper[k] -= 1
                #백트래킹 다시 풀어주면서 원복하는 부분 => k가 반복돌면서 최소의 갯수가 안될 수도 있기 떄문에! 다시 뗸다!
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        MAP[i][j] = 1
    else:
        #오른쪽으로 간다
        dfs(x + 1, y, cnt)

MAP = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = sys.maxsize
dfs(0,0,0)
if ans != sys.maxsize:
    print(ans)
else:
    print(-1)

