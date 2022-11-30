def greedy(lst, num, ans=0):
    for i in range(1, num):
        if lst[i - 1] != end[i - 1]:
            lst[i - 1] = 1 - lst[i - 1]
            lst[i] = 1 - lst[i]
            if i + 1 < num:
                lst[i + 1] = 1 - lst[i + 1]
            ans += 1
        if lst == end:
            return ans
    else:
        return -1


num = int(input())  # 전구 개수
start = list(map(int, list(input())))  # 초기 상태
end = list(map(int, list(input())))  # 원하는 상태

# 첫 번째 전구를 뒤집었음
start1 = start[:]
ans1 = greedy(start1, num)
# 첫 번째 전구를 안 뒤집었음
if ans1 == -1:
    start[0] = 1 - start[0]
    start[1] = 1 - start[1]
    ans2 = greedy(start, num, 1)
    print(ans2)
else:
    print(ans1)