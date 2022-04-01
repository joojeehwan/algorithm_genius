'''

1차원 bfs 생각하자!

예전에 어디 스타드 링크 계단 올라가는 문제!? 1학기 알고리즘 스터디 때 풀었던거 같은디?!

'''

from collections import deque

def bfs(A):
    #큐 생성
    q = deque()
    #초기값 / check배열 값 추가
    q.append([A, 0])
    visited.append(A)

    while q:
        now_point, cnt = q.popleft()

        #종료조건
        if now_point == B:
            return cnt + 1
        #1차원 선상에서 다음 수로 갈 수 있는 범위를 생각 -> x * 2 ~ x "1" 2개만 갈 수 있따.
        for next_point in (now_point * 2, int(str(now_point) + "1")):
            #for -> 범위 생각
            if next_point <= B :
                # 방문하지 않은 곳
                if next_point not in visited:
                    q.append([next_point, cnt + 1])
                    visited.append(next_point)
    return -1


A, B = map(int, input().split())
# visited = [False] * B
# 배열에 들어가 있으면! 안 가면 된다!
visited = []
print(bfs(A))


# for i in range(1, 4):
#     print(i)

#안에 있는 요소 보는 것
# for i in [1, 4]:
#     print(i)