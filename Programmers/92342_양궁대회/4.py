# 13 / 25

# def solution(n, info):
#     answer = []
#     ryan = info[:]
#     notfixed = sorted(ryan)
#     fixed = [0] * 11
#     while any(notfixed) or len(notfixed):
#         max_arrow = notfixed.pop()
#         for i in range(10, -1, -1):
#             if ryan[i] == max_arrow:
#                 ryan[i] = 0
#                 fixed[i] = 1
#                 break
#         for i in range(11):
#             if max_arrow <= 0:
#                 break
#             if not fixed[i]:
#                 notfixed.remove(ryan[i])
#                 ryan[i] += 1
#                 fixed[i] = 1
#                 max_arrow -= 1
#         if max_arrow:
#             ryan[10] += max_arrow
#             max_arrow = 0
#     ryanscore = 0
#     appeachscore = 0
#     for i in range(11):
#         if ryan[i]:
#             ryanscore += 10-i
#         elif info[i]:
#             appeachscore += 10-i
#     if ryanscore < appeachscore:
#         answer = [-1]
#     else:
#         answer = ryan[:]
#     return answer

def solution(n, info):
    answer = [0] * 11
    arrows = [0] * 11
    maxDif = 0

    for subset in range(1, 1 << 10): 
        R = 0
        A = 0
        cnt = 0

        for i in range(10):  
            if subset & (1 << i):
                R += 10 - i
                arrows[i] = info[i] + 1
                cnt += arrows[i]
            else:
                arrows[i] = 0
                if info[i]:
                    A += 10 - i    

        if cnt > n:
            continue

        arrows[10] = n - cnt

        if R - A == maxDif:
            for j in reversed(range(11)):
                if arrows[j] > answer[j]:
                    maxDif = R - A
                    answer = arrows[:]
                    break
                elif arrows[j] < answer[j]:
                    break

        elif R - A > maxDif:
            maxDif = R - A
            answer = arrows[:]

    if maxDif == 0:
        answer = [-1]
    return answer