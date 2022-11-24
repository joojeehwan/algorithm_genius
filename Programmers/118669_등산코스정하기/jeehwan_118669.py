'''

등산코스 정하기..

다익스트라 알고리즘 사용



풀이

1. 양방향 그래프

2. 간선간에 가중치 존재

3. 휴식없이 이동해야하 하는 시간 중 가장 긴 시간 => intensity

이 값이 최소가 되도록

4. 한 곳에서 출발 -> 다시 출발한 곳으로 돌아옴

출입구 : "1번 노드", "N번 노드" 에서만! 중복되게 나타면 안된다.
산봉우리 : 2 ~ N - 1 노드 중에서 단 한번


출발지에서 산봉우리까지 도착할 떄의 최소 intensity구하고, 그 이후는 구하지 않아도 된다.


'''

from collections import defaultdict
from heapq import heappush, heappop


'''

n	paths  [start, end, value]	                                                                                    gates	summits	result
6	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]	[1, 3]	[5]	     [5, 3]
'''

#n : 노드 수  / gates : 출입구 , summit : 산봉우리

INF = int(1e9)

def solution(n, paths, gates, summits) :


    def dijkstra():
        
        #1. 최소 힙 / visited배열 생성
        q = [] # (intensity, now_position)
        visited = [INF] * (n + 1)

        #2. 모든 출입구들을 heap에다가 넣기
        for gate in gates:
            # heappush(q, (gate[]))
            pass
    