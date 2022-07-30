# 솔루션 1


def solution(triangle):

    answer = 0
    #이중 포문?! 픙 하나 찍고 그 안에서 반복
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0 : #왼쪽끝
                triangle[i][j] += triangle[i-1][j]

            elif j == i : #오른쪽 끝
                triangle[i][j] += triangle[i-1][j-1]


            else: #끝에 있는 게 아닐 때!
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    #마지막 층(맨 아래층에서의 가장 큰수를 구하면 된다)
    return max(triangle[-1])

#솔루션 2
'''

    0   7   0
  0   10  15   0
0  18  16   15   0
양 옆에 0을 두어서! 인덱스 에러가 안나게끔! 
'''
def solution(triangle):
    answer = 0
    # 아 밑에 처럼 적을 수가 있그나,,
    #양옆으로 0을 넣어주네
    triangle = [[0] + t + [0] for t in triangle ]
    for i in range(1, len(triangle)):
        for j in range(1, i + 2):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    answer = max(triangle[-1])
    return answer