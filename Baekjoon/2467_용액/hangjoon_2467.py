solutions = int(input())  # 용액 수
solution_lst = list(map(int, input().split()))  # 용액 리스트
solution_lst.sort()

start, end = 0, solutions - 1
ret = 2000000000
while start != end:
    # 계산
    temp = solution_lst[start] + solution_lst[end]

    # 비교
    if abs(ret) > abs(temp):
        ans = (solution_lst[start], solution_lst[end])
        ret = temp

    # 다음 step
    if temp < 0:  # 너무 작음
        start += 1
    elif temp > 0:  # 너무 큼
        end -= 1
    else:  # 딱 0임
        break

print(ans[0], ans[1])
