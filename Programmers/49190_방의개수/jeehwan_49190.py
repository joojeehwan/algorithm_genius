import collections
#bfs
def solution(arrows):
    answer = 0
    #팔방향 이동 위부터 좌대각선위 까지!
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0) #현재 노드
    
    visited = collections.defaultdict(int) # 노드 방문 체크 기본값 0 
    visited_dir = collections.defaultdict(int) # 노드 방문 경로 체크, (A, B)는 A -> B 경로를 의미 (row, col) => (row, col)
    
    q = collections.deque([now]) # 방문을 위한 큐
    
    #초기 세팅과 같은 부분, 내가 이동한 노드들을 큐에다가 담는다. 
    for i in arrows:
        # 모래 시계 방향을 막기 위해 해당 방향으로 2칸 씩 추가
        for _ in range(2):
            next = (now[0] + move[i][0], now[1] + move[i][1])
            q.append(next)
            now = next
            
    now = q.popleft() #현재 노드
    #visted 자체가 key value라서! 그냥 now값 자체가 key가 되어서 노드를 갔는지 안갔는지 여부 확인한다. 
    visited[now] = 1 # 시작 노드는 방문 처리
    #bfs 시작 방의 개수 세기
    while q:
        next = q.popleft() #다음 노드
        # print(next)
        if visited[next] == 1: #이미 방문한 노드인 경우
            if visited_dir[(now, next)] == 0: #해당 경로에 처음 들어온 경우
                answer += 1 #방이 생성 되므로 answer에 + 1
                
        else: #방문한 노드가 아니라면 방문처리
            visited[next] = 1
            
        #해당 노드로 들어온 경로를 방문 처리
        visited_dir[(now, next)] = 1
        visited_dir[(next, now)] = 1
        now = next #다음 next에서 이동해보자! 
    return answer