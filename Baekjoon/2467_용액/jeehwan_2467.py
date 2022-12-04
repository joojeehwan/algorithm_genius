'''

이미 입력 자체가 오름차순...

범위가 - 10억 ~ + 10억

이건 이분탐색 하라고 만든 문제..


어떻게 했는지..1년전 내 풀이는?!

'''

#투 포인터 풀이

N = int(input())

#이미 정렬되어 있게 들어온다.
lst = list(map(int, input().split()))

start = 0

end = N - 1

min_value = 1100000000000000000

index_left = 0

index_right = 0

while start < end:

    SUM = lst[start] + lst[end]

    if abs(SUM) < min_value:

        index_left = start

        index_right = end

        min_value = abs(SUM)

    if SUM < 0:
        start += 1

    else:
        end -= 1

'''

가장 작은 0번 인덱스 값과가장 큰 마지막 값을 초기 포인터로 설정해주었다.

이후, 두 포인터가 가르키는 값을 더한 후 해당 값의 절대값이 0과 가장 가까운 것을 각각 저장해준다.

포인터를 이동시킬때는 두 포인터가 가르키는 값을 더한 값이 0보다 크냐 작냐를 기준으로 한다.

만약 해당 값이 0보다 작다는 것은 두 포인터가 더한 값을 증가시켜줘야하기 때문에 왼쪽 포인터를 1 더해주기,
그게 아니라면 값을 감소시켜줘야하기 때문에 오른쪽 포인터에서 1을 빼주기

'''

# print(lst[start], lst[end]) # 아 이러니깐 답이 안나오지,,!
#print(lst[index_left], lst[index_right])


#이진 탐색 풀이

import sys
input = sys.stdin.readline


N = int(input())
lst = list(map(int, input().split()))
ans = int(10e9)

#이게 없어야 되네..
# ans_left = 0
# ans_right = 0

for i in range(N - 1):
    now = lst[i]

    start = i + 1
    end = N - 1

    while start <= end :

        mid = (start + end ) // 2

        # 이 값을 설정한는 것이 중요
        temp = now + lst[mid]

        if abs(temp) < ans:
            ans = abs(temp)
            #밑에 작업을 하는 이유는 인덱스로 해당 값을 출력해야함. 그래서 인덱스를 기록
            # i번째 숫자를 기준으로 mid 값을 이동 시키면서, 언제 가장 작아지는 지를 이분탐색한다.
            ans_left = i
            ans_right = mid

        if temp == 0:
            break

        if temp < 0 :
            #값이 0에 더 가깝게 가기 위해서 시작 범위를 더 높게... 값을 증가 시키기
            start = mid + 1

        else:
            # 0 에 더 가깝게 가기 위해서 한계 범위를 더 작게.. 값을 감소 시키기
            end = mid - 1

print(lst[ans_left], lst[ans_right])


