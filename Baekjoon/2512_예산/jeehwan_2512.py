#이분탐색이란
'''
2. 이분 탐색 알고리즘
시간복잡도: O(logN)
반복문과 재귀 두 가지 방법을 사용할 수 있다.
자료를 오름차순으로 정렬한다.
자료의 중간값(mid)이 찾고자 하는 값(target)인지 비교한다.
mid 값이 target과 다르다면 대소관계를 비교하여 탐색 범위를 좁히고, target과 mid 값이 같을 때까지 아래 조건에 따라 2번과 3번을 반복한다.
          ⓐ target이 mid 값 보다 작으면 end를 mid 왼쪽 값으로 바꿔준다. (절반의 왼쪽 탐색)
          ⓑ target이 mid 값 보다 크면 start를 mid 오른쪽 값으로 바꿔준다. (절반의 오른쪽 탐색)
'''
#반복문
def binary_serch (target, data):
    data.sort()
    start = 0 #첫 시작 인덱스
    end = len(data) - 1 #마지막 종료 인덱스

    while start <= end:
        mid = (start + end) // 2 #중간값의 인덱스

        if data[mid] == target: #target 인덱스 반환
            return mid

        elif data[mid] > target : #target이 더 작은 경우, 오른쪽 범위(큰 범위)를 조사 하지 않음
            end = mid - 1

        else: #target이 더 큰 경우, 왼쪽 범위(작은 범위)를 조사 하지 않음.
            start = mid + 1
    return

#재귀
data = []
def binary_search(target, start, end):

    if start > end:		 # 범위를 넘어도 못찾는다면 -1을 반환
        return -1

    mid = (start + end) // 2  # 중간값

    if data[mid] == target:	# 중간값의 데이터가 target과 같다면 mid를 반환
        return mid

    elif data[mid] > target: # target이 작으면 왼쪽 탐색
        end = mid - 1
    else:                    # target이 크면 오른쪽 탐색
        start = mid + 1

    return binary_search(target, start, end) # 줄어든 범위를 더 탐색

def solution(target, data):
    data.sort()  # 정렬(필수)
    start = 0
    end = len(data) - 1
    return binary_search(target, start, end)

# ----------------------------------------------------------------------------------------


#3년전 내 풀이
N = int(input())
budgets = list(map(int, input().split()))
total_budgets = int(input())
start, end = 0, max(budgets)

while start <= end:

    mid = (start + end) // 2
    total = 0
    for budget in budgets:
        if budget > mid:
            total += mid
        else:
            total += budget
    if total <= total_budgets:
        start = mid + 1
    else:
        end = mid - 1
print(end)