
#초기 입력 및 세팅

n = int(input())

students = [list(map(int, input())) for _ in range(n * n)]

visited = [[False] * n for _ in range(n)]

#벡터 배열, 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



for num in range(n ** 2):

    #각 학생번호와 그 학생의 선호도 학생들이 번호로
    student = students[num]
    temp = []

    #완탐
    for row in range(n):
        for col in range(n):
            #일단 가지 않았 던 곳으로 가야한다.
            if not visited[row][col]:
                #자리를 선택하는 기준이 되는 선호도와 빈공간 counting
                like = 0
                blank = 0
                for k in range(4):
                    next_row = row + dr[k]
                    next_col = col + dc[k]

                    if 0 <= next_row < n and 0 <= next_col < n:
                        # 주위에 선호하는 학생이 있다면! 다 카운팅하기
                        if visited[next_row][next_col] in student[:] :
                            like += 1

                        if visited[next_row][next_col] == 0:
                            blank += 1

                temp.append([like, blank, next_row, next_col])

    #람다 관련해서 더 공부
    temp.sort(key = lambda x : (-x[0], -x[1], x[3], x[2]))
    #이제 실제 MAP에다가 넣기! 가장 맨 앞이 학생 번호 인 것.
    visited[temp[num][2]][temp[num][3]] = student[0]


#이제 점수를 계산해보자.
result = 0
#students.sort()

for row in range(n):
    for col in range(n):
     ans = 0
     for k in range(4):
         next_row = row + dr[k]
         next_col = col + dc[k]

         if 0 <= next_row < n and 0 <= next_col < n:
            if visited[next_row][next_col] in students[visited[row][col] - 1] :
                ans += 1
    if ans != 0:
        result += 10 ** (ans - 1)

print(result)






