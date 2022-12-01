n = int(input())
solution = list(map(int, input().split()))

left, right = 0, n-1
min_val = abs(solution[-1] + solution[0])
ans1, ans2 = solution[0], solution[-1]

while left < right:
    val = solution[left] + solution[right]

    if abs(val) < min_val:                              # 특성값을 비교
        ans1, ans2 = solution[left], solution[right]
        min_val = abs(val)

    if val < 0:             # 특성값이 0보다 작으면 왼쪽포인터 이동, 크면 오른쪽포인터 이동
        left += 1
    elif val > 0:
        right -= 1
    else:
        break

print(ans1, ans2)