# from collections import deque

# def solution(begin, target, words):
#     answer = 0
#     #target이 words에 없는 경우 0 리턴
#     if target not in words:
#         return 0

#     q = deque()
#     q.append((begin, 0))
#     while q:
#         now, depth = q.popleft()
#         for word in words:
#             diff = 0
#             for i in range(len(word)): #하나 다른 것 찾기! 지금 내가 가지고 있는 단어와 words의 안의 word단어가 하나 다른지 확인!
#                 if now[i] != word[i]:
#                     diff += 1
#             #위에 포문이 끝날떄까지 아래의 코드는 실해되지 않는다!
#             #만약에 글자 하나가 다르고! 내가 찾는 단어라면!
#             if (diff == 1) and (word == target):
#                 #depth 하나 증가 시키면서 return
#                 depth += 1
#                 return depth

#             #그것이 아니라면 q에 넣고! 다시 다른 단어를 보아야하지!
#             elif diff == 1:
#                 q.append((word, depth + 1))

#     return answer


# bfs 풀이


# from collections import deque

# def solution(begin, target, words):

#     answer = 0
#     #만약에 tartget이 아예 words에 없다?!
#     if target not in words:
#         return 0


#     #질문,
#     '''
#     q = deque((begin, 0)) 이랑
#     q = deque()
#     q.append((begin, 0)) 이 다른것이냐?!
#     '''
#     q = deque()
#     q.append((begin, 0))

#     while q:

#         now_word, cnt = q.popleft()

#         #다음 단계로 넘어가기 위해서 words안에서 for문으로 이동해보자
#         for next_word in words:
#             diff = 0
#             #현재 내가 가지고 있는 단어와, 다음 단어가 글자 하나만 다른것을 찾자
#             for i in range(len(next_word)):
#                 if now_word[i] != next_word[i]:
#                     diff += 1

#             #다음 단어중에서 글자가 하나 다르고, target의 단어가 똑같다면
#             if diff == 1 and next_word == target:
#                 cnt += 1
#                 return cnt
#             #아직은 같은 target이 아니지만, 글자 하나가 다른 것 => 그 다음으로 이동할 수 있는 단어
#             elif diff == 1:
#                 q.append((next_word, cnt + 1))

#     return answer

# dfs 풀이

# import sys
# sys.setrecursionlimit(10 ** 9)

# visited = []
# result = [] #각각의 lev들을 모아서 가장 작은것을 찾아야 한다.

# def solution(begin, target, words):
#     answer = 0

#     for _ in range(len(words)):
#         visited.append(0)

#     if target not in words:
#         return 0

#     def dfs(lev, word):
#         if word == target:
#             result.append(lev)
#             return

#         #탐색 시작 => 단어 하나씩 본다.
#         #방문한곳 가지 않는다.
#         for i in range(len(words)):
#             if visited[i] == 1:
#                 continue

#             #방문하지 않았고, diff가 하나 다른 녀석
#             diff = 0
#             for i in range(len(word)):
#                 if word[i] != words[i]:
#                     diff += 1

#                 if diff == 1:
#                     visited[i] = 1
#                     dfs(lev + 1, words[i])
#                     visited[i] = 0

#     dfs(0, begin)

#     answer = min(result)
#     return answer


import sys

sys.setrecursionlimit(10 ** 6)

visited = []
result = []


def solution(begin, target, words):
    answer = 0

    for _ in range(len(words)):
        visited.append(0)

    if target not in words:
        return answer  # if문 안에서 리턴을 하는경우 else를 쓰지 않아도 됨

    def dfs(word, depth):
        if word == target:
            result.append(depth)
            return

        for i in range(len(words)):
            # 이미 방문한 노드는 처리하지 않는다.
            if visited[i] == 1:
                continue

            # 현재노드와 방문처리되지 않은 노드중 차이가 1인것
            if checkDiff(word, words[i]) == 1:
                visited[i] = 1
                dfs(words[i], depth + 1)
                visited[i] = 0  # 이부분..! dfs가 끝나면 다시 방문처리를 풀어주는것

    dfs(begin, 0)

    answer = min(result)
    return answer


def checkDiff(word, target):
    diff = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            diff += 1
    return diff