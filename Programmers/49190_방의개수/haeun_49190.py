"""
처음엔 중복으로 방문할 때에 도형을 만들면 된다고 생각했다.
그러자 2개의 문제점이 있었다. 좌표가 아닌 곳을 또 지나가는 경우(대각선 교차),
이미 방문했던 곳을 또 방문하지만 도형이 되진 않는 경우.
중간에 교차해서 도형이 만들어지는 경우는 2배로 늘려버려서 해결했지만,
선 위를 왔다갔다 하는 경우는 해결할 수 없었다.
힌트를 보니 '이미 그려졌던 선인지 확인하라'고 해서
좌표만 저장하는게 아니라 선분도 저장했다.
대신 선분을 저장할 때 좌표를 정렬해서 저장해서
같은 선분인데 좌표가 달라서 중복 저장되는 경우를 막아야 한다.
오래걸렸다. 2시간 정도
점수 : 1123 (+15)
"""

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def solution(arrows):
    answer = 0

    # 시작 위치(정점)
    row, col = 0, 0
    # 방문한 좌표를 저장한다. (r1, c1) = True
    visited = {(0, 0): True}
    # 지나온 선을 저장한다. ((r1, c1), (r2, c2)) = True
    path = dict()

    for arrow in arrows:
        # 대각선 처리를 위해 2번씩 이동한다.
        # 무조건 중간을 지나가기 때문이다. 1/3 지점을 지나가는 일 같은건 없다.
        for i in range(2):
            next_row = row + dr[arrow]
            next_col = col + dc[arrow]
            # 만들어진 선을 표시
            # 이때 순서가 뒤집혀서 중복 기록되는걸 막아야한다.
            # list는 hashable 하지 않으므로 tuple로 형변환을 했다. 이것보다 더 깔끔하게 하는 방법 없나...
            line = tuple(sorted([(row, col), (next_row, next_col)]))
            # 방문한 적이 있는 경우
            if visited.get((next_row, next_col)):
                # 만들어진 선도 없어서 도형이 되는 경우
                if not path.get(line):
                    answer += 1
                    path[line] = True
            # 방문한 적이 없는 경우, 방문했다고 표시
            else:
                visited[(next_row, next_col)] = True
                path[line] = True
            # 업데이트
            row, col = next_row, next_col
    return answer


print(solution([2, 7, 2, 5, 0]))
