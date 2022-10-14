n = int(input())
students = [list(map(int,input().split())) for _ in range(n**2)]
arr = [[0] * n for _ in range(n)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

for order in range(n**2):
    student = students[order]
    temp = []
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 0:
                like = 0
                blank = 0
                for i in range(4):
                    nx = r + dx[i]
                    ny = c + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in student[1:]:
                            like += 1
                        if arr[nx][ny] == 0:
                            blank += 1
                temp.append([like, blank, r, c])
    temp.sort(key= lambda x: (-x[0],-x[1],x[3],x[2]))
    arr[temp[0][2]][temp[0][3]] = student[0]

result = 0
students.sort()

for r in range(n):
    for c in range(n):
        ans = 0
        for k in range(4):
            nx = r + dx[k]
            ny = c + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] in students[arr[r][c] - 1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans - 1)

print(result)
