
import heapq

def solution(k, score):
    max_heap = []
    answer = []

    for sc in score:
        heapq.heappush(max_heap, (-sc, sc))
        answer.append(max(heapq.nsmallest(k, max_heap))[1])

    return answer


'''
- 지금까지 출연한 가수들의 점수 중 상위 k 번째 이내이면 => 명예의 전당

- 즉, 프로그램 시작 이후, 초기 k일 까지는 모든 출연 가수의 점수가 명예의 전당으로 

- k일 다음부터는 출연 가수의 점수가 기존의 명예의 전당에 오른 k번째 순위의 가수보다 점수가
높으면, 그 가수가 명예의 전당으로 

- 명예의 전당에 올라간 k개의 내의 점수들 중에서, 최하위 점수를 발표
    * 일자별

'''
import heapq


def solution(k, score):
    answer = []
    lowest = []

    for sc in score:

        if len(lowest) < k:
            lowest.append(sc)

        else:
            if min(lowest) < sc:
                lowest.remove(min(lowest))
                lowest.append(sc)
        answer.append(min(lowest))

    print(lowest)

    return answer