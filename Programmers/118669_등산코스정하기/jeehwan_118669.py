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


출발지에서 산봉우리까지 도착할 떄의 최소 intensity(쉽게 생각해 가중치의 합)구하고, 그 이후는 구하지 않아도 된다.



'''

from collections import defaultdict
from heapq import heappush, heappop


'''

n	paths  [start, end, value]	                                                                  gates	    summits	 result
6	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]	  [1, 3]	[5]	     [5, 3]

'''

#n : 노드 수  / gates : 출입구 , summit : 산봉우리

INF = int(1e9)

def solution(n, paths , gates, summits) :


    def dijkstra():
        
        #1. 최소 힙 / visited배열 생성
        q = [] # (intensity, now_position)
        visited = [INF] * (n + 1)

        #2. 모든 출입구들을 heap에다가 넣기
        for gate in gates:
            heappush(q, (0, gate))
            #방문한 곳이니 무한에서 0으로
            visited[gate] = 0


        while q:

            intensity, now_position = heappop(q)


            # 산봉우리를 만나면 끝 혹은 기존에 있는 인텐시티보다 더 길어?! 그럼 굳이 갈 필요가..! 그냥 원래 길로 가자!
            if now_position in summits_Set or intensity > visited[now_position]:
                continue

            for next_node, distance in MAP[now_position]:
                # cost = intensity + distance 해당 노드를 거쳐 갈 떄의 거리 // 알고리즘은 암기가 x , 이렇게 하는건 전체 최단경로를 구하는 것
                new_intensity = max(intensity, distance)
                if new_intensity < visited[next_node] :   #선택된 노드를 거쳐서 가는 것이 현재 가는 거리보다 더 작다면 갱신
                    visited[next_node] = new_intensity
                    heappush(q, (new_intensity, next_node))

        #visted를 함수 안에서 선언했기에, 안에서 값 계산
        answer = [0, INF]
        for summit in summits:
            if visited[summit] < answer[1]:
                answer[0] = summit
                answer[1] = visited[summit]

        return answer

    #이렇게 안하면 시간초과구나
    summits.sort()
    summits_Set = set(summits)
    # 리스트로 만드는 방법
    # MAP = [[] for _ in range(n + 1)]

    # 소율이 생각
    # defaultdict로 만드는 방법, key가 노드 value 가 해당 노드(key)에서 갈 수 있는 노드들

    MAP = defaultdict(list)
    for start, end, value in paths:
        MAP[start].append((end, value))
        MAP[end].append((start, value))

    return dijkstra()



#다른 풀이

from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    answer = []
    graph = defaultdict(list)
    s = []
    INF = float('inf')
    node_intensity_info = [INF]*(n+1)
    # set 을사용하지않으면 list 내의 in 확인은 O(N) 이라 시간초과뜬다
    summits= set(summits)
    # 출발지점 의 (intensitiy는 0 으로 , gate 번호)
    for g in gates:
        heapq.heappush(s,(0,g))
        node_intensity_info[g] = 0
    # 출발지점 -> 도착지점 -> 출발지점
    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
    # 출발지점 돌면서
    while s:
        inten,node = heapq.heappop(s)
        if node in summits or inten > node_intensity_info[node]:
            continue
        # node 의 inten 저장해주고
        for next_node,next_intensity in graph[node]:
            # 현재 intensity 와 다음 노드로가는 next_intensity 와 node_intensity_info 를 비교해야함
            # 즉 intensity 에는 현재와 다음 노드 intensity 를 비교해주고
            intensity = max(inten,next_intensity)
            # 그게 기록일지 (next_node_info) 보다 작다면 갱신해주고 heap 에넣어줌
            if intensity < node_intensity_info[next_node]:
                node_intensity_info[next_node] = intensity
                heapq.heappush(s,(node_intensity_info[next_node],next_node))
    answer = []
    for summit in summits:
        answer.append([summit,node_intensity_info[summit]])
    answer.sort(key = lambda x: (x[1],x[0]))
    return answer[0]

#bfs 풀이
import collections


def makeGraph(paths, n):
    result = collections.defaultdict(list)
    for g1, g2, way in paths:
        result[g1].append([g2, way])
        result[g2].append([g1, way])
    return result


def bfs(n, graph, gates, summits, distance):
    que = collections.deque(gates)
    while que:
        cur_loc = que.popleft()
        if cur_loc in summits: continue
        for next_loc, way in graph[cur_loc]:
            if distance[next_loc] > max(distance[cur_loc], way):
                que.append(next_loc)
                distance[next_loc] = max(distance[cur_loc], way)

    return distance


def solution(n, paths, gates, summits):
    answer = []
    graph = makeGraph(paths, n)
    summits_dict = {}
    min_dis = float('inf')
    min_summit = -1
    for summit in summits:
        summits_dict[summit] = 1

    distance = [10000001 for _ in range(n + 1)]
    for gate in gates:
        distance[gate] = 0

    distance = bfs(n, graph, gates, summits_dict, distance)

    for summit in summits:
        if min_dis > distance[summit]:
            min_dis = distance[summit]
            min_summit = summit
        elif min_dis == distance[summit] and min_summit > summit:
            min_summit = summit

    return [min_summit, min_dis]


