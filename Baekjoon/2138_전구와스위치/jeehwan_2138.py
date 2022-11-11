'''

전구와 스위치


0은 꺼져있는 상태

1은 켜져있는 상태

와 전혀 생각이 안나네... ㄷㄷㄷ
이런거 참 나 웃기네 정말



1. 첫 번째 전구를 키는 케이스와 키지 않는 케이스 나누기
=> 비교할 이전 전구가 있는 경우 / 아닌 경우 두 가지 경우 모두 확인

2. 한 번 지나간 전구는 건들지 않는다.
=> 한 번 지나간 전구를 다시 건드린다고, 불가능한게 다시 가능해지지도 않고 횟수만 늘어나기 때문

3. 전구의 상태를 바꾸면 양 옆 전구가 바뀌기 때문에 
두 번쨰 전구부터 시작해서 이전 전구의 상태가 희망하는 상태와 같은지 확인하고 
다르다면 스위치를 눌러 상태를 변경 

=> 이전 전구의 상태만 비교?! 
반복문이 진행되면서, 다음 전구는 결국 비교하기 때문



3가지 풀이 다 이해해보고, 내 것으로 만들자.

'''




#초기 입력
N = int(input())

lst = list(map(int, input()))

target = list(map(int, input()))


def change(asIs, toBe):
    
    #얕읕 복사로(1차원 리스트의 경우엔 깊은 복사와 같은 효과), 이전의 전구 상태 기록 / 원본은 그대로 두기
    # 2가지 케이스로 나뉘는데, 그 케이스에 영향을 주지 않기 위함. 원본 lst를 바꿔버리면 안되니깐!
    lights = asIs[:]
    cnt = 0
    for i in range(1, N):

        #이전 전구가 같은 상태!?
        if lights[i-1] == toBe[i-1]:
            continue
        #상태가 다르네?!
        cnt+=1
        #상태 변경하러 가야지!
        for j in range(i-1, i+2):
            #마지막 전구의 범위 생각
            if j < N:
                lights[j] = 1 - lights[j]
    #이런식으로 배열비교 가능하다...!
    if lights == toBe:
        return cnt
    else:
        return 1e9

    #return cnt if lights == toBe else 1e9

#첫 번째 전구를 누르지 않는 경우
res = change(lst, target)

#첫 번째 전구를 누르는 경우, 첫 번째와 두 번째의 전구 불빛이 달라진다.
lst[0] = 1 - lst[0]
lst[1] = 1 - lst[1]


# " +1 "을 하는 이유?! 이미 첫 번째 전구를 눌렀으니깐!! 
res = min(res, change(lst, target) + 1)

if res != 1e9:
    print(res)

else:
    print(-1)




#2


n = int(input())

data = list(map(int, input()))
result = list(map(int, input()))

# 1차원 배열 한정 깊은 복사
temp1 = data[:]
temp2 = data[:]
count = 0

# index 0 부터 시작
def from_zero(temp):
    count = 1
    #이렇게 0 -> 1 / 1 -> 0 바꿀수 도 있구나
    temp[0] = int(not temp[0])
    temp[1] = int(not temp[1])
    for i in range(1, n):
        # 비교해서 바꿔주어야 하면 클릭하기
        if result[i-1] != temp[i-1]:
            count += 1
            temp[i-1] = int(not temp[i-1])
            temp[i] = int(not temp[i])
            if i != n-1:
                temp[i+1] = int(not temp[i+1])
    if temp == result:
        return count
    return -1
# index 1부터 시작
def from_one(temp):
    count = 0
    for i in range(1, n):
        # 비교해서 바꿔주어야 하면 클릭하기
        if result[i-1] != temp[i-1]:
            count += 1
            temp[i-1] = int(not temp[i-1])
            temp[i] = int(not temp[i])
            if i != n-1: # 인덱스 초과 예외처리
                temp[i+1] = int(not temp[i+1])
    if temp == result:
        return count
    return -1

a = from_zero(temp1)
b = from_one(temp2)
if a == -1 and b != -1:
    print(b)
elif a != -1 and b == -1:
    print(a)
else:
    print(min(a, b))




#3

import sys


def make_same(src, dest):
    count = 0
    for i in range(1, len(dest) - 1):
        if src[i - 1] != dest[i - 1]:
            count += 1  # 스위치 횟수 증가
            # 전구 상태 변경
            src[i - 1] = not src[i - 1]
            src[i] = not src[i]
            src[i + 1] = not src[i + 1]
    if src[-2] != dest[-2]:  # 맨 마지막 스위치
        count += 1
        src[-2], src[-1] = not src[-2], not src[-1]

    if src[-1] == dest[-1]:  # 앞(i - 1) 을 기준으로 맞춰 왔으므로 맨 마지막 전구만 확인하면 됨
        return count
    return int(1e9)  # 만들 수 없을 경우 INF 반환


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    src = list(map(lambda x: int(x) == 1, list(sys_input().rstrip())))
    dest = list(map(lambda x: int(x) == 1, list(sys_input().rstrip())))

    answer = int(1e9)

    copy = src.copy()
    copy[0], copy[1] = not copy[0], not copy[1]  # 맨앞 스위치 누르고 시작
    answer = min(answer, make_same(copy, dest) + 1)
    answer = min(answer, make_same(src, dest))  # 아무것도 안 누르고 시작

    print(answer if answer != int(1e9) else -1)


solution()



#4

import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().strip()))
B = list(map(int, input().strip()))

A1 = A[:]
A2 = A[:]


def two_flip(i, j):
    A[i] = 1 - A[i]
    A[j] = 1 - A[j]


def three_flip(i, j, k):
    A[i] = 1 - A[i]
    A[j] = 1 - A[j]
    A[k] = 1 - A[k]


for i in range(2):
    A = A1 if i == 0 else A2

    cnt = 0
    for j in range(n):
        if j == 0:
            if i == 0 and A != B:
                cnt += 1
                two_flip(j, j+1)

        elif 1 <= j <= n-2:
            if A[j-1] != B[j-1]:
                cnt += 1
                three_flip(j-1, j, j+1)

        elif j == n-1:
            if A[j-1] != B[j-1]:
                cnt += 1
                two_flip(j-1, j)

    if A == B:
        print(cnt)
        break

if A != B:
    print(-1)


#5
import copy

N = int(input())
current_status = list(input())
result_status = list(input())

current_status = list(map(int, current_status))
result_status = list(map(int, result_status))
mn_cnt = 1e9

for i in range(2):
    cnt = 0
    data = copy.deepcopy(current_status)

    # 0번 버튼을 누른 경우
    if i == 0:
        data[0] = 1 - data[0]

        if N > 1:
            data[1] = 1 - data[1]
        cnt += 1

    for j in range(1, N):
        if data[j - 1] != result_status[j - 1]:
            cnt += 1
            data[j - 1] = 1 - data[j - 1]
            data[j] = 1 - data[j]

            # j + 1 에 대한 OOB 검증
            if j + 1 < N:
                data[j + 1] = 1 - data[j + 1]

    for j in range(N):
        if data[j] != result_status[j]:
            break
    else:
        mn_cnt = min(mn_cnt, cnt)

if mn_cnt == 1e9:
    print(-1)
else:
    print(mn_cnt)


