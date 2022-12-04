''''

1) 이차원 배열에서 이루어지는 상황(송도는 직사각형 모양으로 생김)

2) 두 좌표 사이의 거리 -> 맨해튼 거리

3)
한 박스 - 맥주 20개
50m에 한 병씩 섭취
편의점에서 맥주 구매 - 맥주 20병 이상 가질 수 없음


즉, 노드들 간의 거리가 1000m를 넘어서는 안된다.
즉, 시작지점과 도착지점의 (ex,상근이네 - 편의점  / 편의점 - 편의점 / 상근이네 - 도착지 / 편의점  - 도착지) 거리가 1000미터 이내여야 한다.





'''



#bfs

from collections import deque


def bfs(start_node):

    q = deque()
    q.append((nodes[start_node]))
    visited[start_node] = True


    # 이런 방식으로 하는 게 아니라, for문 + visited 배열을 사용해 check 하는 방식
    # for next_node in nodes[1:]:
    #     pass

    while q :

        now_row, now_col = q.popleft()

        # 도착지는 맨 리스트의 맨 마지막에
        if (now_row, now_col) == nodes[-1] :
            return "happy"

        # for + if => 이미 방문한 곳 거르기
        for i in range(n + 2):

            #방문한 곳이라면
            if visited[i] :
                continue

            Manhattan_dis = abs(nodes[i][0] - now_row) - abs(nodes[i][1] - now_col)

            if Manhattan_dis <= 1000:
                q.append((nodes[i]))
                visited[i] = True

    # while - else / for - else 다시 정리
    else:
        return "sad"

T = int(input())

for _ in range(T):

    n = int(input())

    nodes = []
    for _ in range(n + 2):
        temp_row, temp_col = map(int, input().split())
        nodes.append((temp_row, temp_col))

    #일차원 배열인 이유?! 방문을 기록하는 건, 이차원배열의 좌표가 아니라, 해당 노드를 방문했는지?!의 여부
    # N + 2 인것, 시작점 , N개의 편의점, 도착점 이기에 N + 2 인 것
    visited = [False] * (n + 2)

    print(bfs(0))





#dfs

