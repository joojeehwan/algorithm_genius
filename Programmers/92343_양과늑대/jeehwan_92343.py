# #백트래킹! dfs!
# answer = 0
# def solution(info, edges):
#     new_edges = [[] for _ in range(len(info))] # new_edges[[]] * len(info) 이런 실수 하지 말자
#     #데이터 전처리! 내가 좋아하는 형태로 바꾸자,,!
#     for edge in edges:
#         frm, to = edge
#         new_edges[frm].append(to)
#         new_edges[to].append(frm)
#     # print(new_edges)
#     visited = [False] * len(info)
#     visited[0] = True
#     dfs(new_edges, visited, info, 1, 0)
#     return answer

# def dfs(new_edges, visited, info, sheep, wolf):
#     global answer
#     answer = max(answer, sheep)
#     #종료 조건 늑대가 같거나 많아지면! 양을 다 잡아먹자나!
#     if sheep <= wolf :
#         return

#     for edge in new_edges:
#         for node in edge:
#             if not visited[node]:
#                 visited[node] = True
#                 if info[node] == 1: #늑대면
#                     dfs(new_edges, visited, info, sheep, wolf + 1)
#                     visited[node] = False
#                 elif info[node] == 0:
#                     dfs(new_edges, visited, info, sheep + 1, wolf)
#                     visited[node] = False

# ??? 아니 왜 실행시간,, 후후,,, 미치것구먼,,ㅠㅠㅠ

from collections import defaultdict

answer = 0


def solution(info, edges):
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    v = [0] * len(info)
    v[0] = 1
    tracking(graph, v, info, 1, 0)
    return answer


def tracking(graph, visited, info, sheep, wolf):
    global answer
    answer = max(answer, sheep)
    if sheep <= wolf:
        return
    for i in range(len(visited)):
        if visited[i]:
            for e in graph[i]:
                if not visited[e]:
                    visited[e] = 1
                    if info[e] == 1:
                        tracking(graph, visited, info, sheep, wolf + 1)
                        visited[e] = 0
                    else:
                        tracking(graph, visited, info, sheep + 1, wolf)
                        visited[e] = 0