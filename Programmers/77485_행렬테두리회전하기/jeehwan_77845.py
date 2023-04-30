'''





'''

# 굳이 함수로 뺄 필요가 있나 싶네!
# def rotate(row1, col1, row2, col2, MAP, rowsCount, columsCount):
#     new_MAP = [[0] for _ in range(columsCount) for _ in range(rowsCount)]
#
#     # 한 칸씩 이동 구현
#
#     for i in range(columsCount):
#         for j in range(rowsCount):
#             MAP[i][j] = new_MAP[i][j]
#
#     return MAP


def solution(rows, columns, queries):
    answer = []

    MAP = [[0 for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            MAP[i][j] = (j + 1) + (columns * i)

    for query in queries:
        x1, y1, x2, y2 = query
        x1 = x1 - 1 #0
        y1 = y1 - 1 #1
        x2 = x2 - 1 #2
        y2 = y2 - 1 #3

        temp = MAP[x1][y1]
        small = temp

        #left => 위에서 아래로의 값만 변하니 row의 값만 변화, col은 y1로 고정
        for i in range(x1 + 1, x2 + 1): # 3, 4, 5
            MAP[i-1][y1] = MAP[i][y1]
            small = min(small, MAP[i][y1])

        #bottom
        for i in range(y1 + 1, y2 + 1):  # 3, 4
            MAP[x2][i-1] = MAP[x2][i]
            small = min(small, MAP[x2][i])

        #right
        for i in range(x2 - 1, x1 - 1, -1):  # 4, 3, 2
            MAP[i + 1][y2] = MAP[i][y2]
            small = min(small, MAP[i][y2])

        #top
        for i in range(y2 - 1, y1 - 1, -1):  # 3, 2
            MAP[x1][i + 1] = MAP[x1][i]
            small = min(small, MAP[x1][i])

        MAP[x1][y1 + 1]  = temp

        answer.append(small)

    return answer


#roate 풀이 대박이네,,하은이 풀이생각난다

from collections import deque
def solution(rows, columns, queries):
    arr = [[i+columns*j for i in range(1,columns+1)] for j in range(rows)]
    answer, result = deque(), []
    for i in queries:
        a,b,c,d = i[0]-1,i[1]-1,i[2]-1,i[3]-1
        for x in range(d-b):
            answer.append(arr[a][b+x])
        for y in range(c-a):
            answer.append(arr[a+y][d])
        for z in range(d-b):
            answer.append(arr[c][d-z])
        for k in range(c-a):
            answer.append(arr[c-k][b])
        answer.rotate(1)
        result.append(min(answer))
        for x in range(d-b):
            arr[a][b+x] = answer[0]
            answer.popleft()
        for y in range(c-a):
            arr[a+y][d] = answer[0]
            answer.popleft()
        for z in range(d-b):
            arr[c][d-z] = answer[0]
            answer.popleft()
        for k in range(c-a):
            arr[c-k][b] = answer[0]
            answer.popleft()
    return result



#스택 자료구조 풀이

def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1


        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]


        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))


    return answer