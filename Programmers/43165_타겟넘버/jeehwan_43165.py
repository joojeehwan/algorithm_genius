# from collections import deque

# def solution(numbers, target):

#     ans = 0
#     q = deque()
#     n = len(numbers)
#     q.append((0, 0))
#     while q:
#         now_sum , index = q.popleft()
#         if index == n:
#             if now_sum == target:
#                 ans += 1

#         else:
#             q.append((now_sum + numbers[index], index + 1 ))
#             q.append((now_sum - numbers[index], index + 1 ))


#     return ans

# #1 bfs 풀이
# from collections import deque


# def solution(numbers, target):

#     #bfs 풀이

#     ans = 0
#     #큐 생성 => 초기값 합, 인덱스
#     q = deque()
#     q.append([0, 0])

#     while q:
#         now_sum , index = q.popleft()

#         #배열의 끝까지 와서 연산을 끝냈고!
#         if index == len(numbers):
#             #tartget조건을 만족하면
#             if now_sum == target:
#                 ans += 1
#         else:
#             q.append([now_sum + numbers[index], index + 1])
#             q.append([now_sum - numbers[index], index + 1])

#     return ans


# answer = 0

# def dfs(lev, numbers, target, value):

#     global answer
#     #끝까지 다 연산했고
#     if lev == len(numbers):
#         # 그 값이 내가 원하는 값이면
#         if target == value:
#             answer += 1
#         return

#     else:
#         dfs(lev + 1, numbers, target, value + numbers[lev])
#         dfs(lev + 1, numbers, target, value - numbers[lev])

# def solution(numbers, target):
#     global answer

#     dfs(0, numbers, target, 0)
#     return answer


def solution(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)
    return answer
