''''

와 이거 이분 탐색 문제..!


[문제 접근]

left = 1, right = max(stones)로 초기화한 후 이진 탐색을 통해 최대 몇 명까지 징검다리를 건널 수 있는지 구하였습니다.
mid 값((left + right) // 2) 보다 작은 구간이 연속적으로 k개 이상이면 건널 수 없으므로 mid = right - 1로 범위를 좁혀나갔습니다.
마찬가지로 mid 값보다 작은 구간이 연속적으로 k개 미만이면 건널 수 있으므로 left = mid + 1로 범위를 좁혀나갔습니다.



[알고리즘]

1. left = 1, right = max(stones)로 초기화합니다.

2. 이진 탐색을 수행합니다.

mid 값과 stones의 값을 비교해서 mid 값보다 작은 구간이 연속적으로 k개 이상이면 mid = right - 1로 업데이트합니다.
mid 값과 stones의 값을 비교해서 mid 값보다 작은 구간이 연속적으로 k개 미만이면 mid = left + 1로 업데이트합니다.

'''



def solution(stones, k):

    left, right = 1, max(stones)
    answer = 1

    while left <= right:

        mid = (left + right) // 2
        blank = 0
        flag = True

        for stone in stones:
            if stone < mid:
                blank += 1
                if blank == k:  # k개의 공백이 생기면 움직일 수 없다.
                    flag = False
                    break
            else:
                blank = 0

        if flag:  # 움직일 수 있는 값
            answer = max(answer, mid)
            left = mid + 1

        else:
            right = mid - 1

    return answer