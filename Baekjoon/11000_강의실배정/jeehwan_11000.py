'''

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)


강의실이 추가적으로 필요한 경우?!

=> 현재 진행중의 강의가 끝나지 않았는데, 새로운 강의가 시작 될 때

이를 계산하기 위헤, 강의가 끝나는 시간을 우선순위큐를 통해 관리, 끝나는 시간이 빠른 강의부터 관리 가능

'''

import heapq

n = int(input())

# 2차원 배열로 받음.
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key = lambda x : x[0])

print(lst)

q = []

#초기값, 첫번쨰 강의가 끝나는 시간을 우선순위 큐에 추가
heapq.heappush(q, lst[0][1])

for i in range(1, n):
    #우선순위 큐에 첫 번쨰 인덱스에 접근 (항상 끝나는 시간이 가장 빠른 순)
    #만약 강의의 시작 시간이 q에 첫번 쨰 인덱스보다 작다면, 해당 강의가 끝나는 시간을 q에 추가.
    if lst[i][0] < q[0]:
        heapq.heappush(q, lst[i][1])

    #아니라면, q에 첫번쨰 인덱스를 pop하고, 현재 바라바고 있는 강의의 시간의 끝나는 시간을 q에 추가
    else:
        heapq.heappop(q)
        heapq.heappush(q, lst[i][1])

print(len(q))


'''

for i in range(1, n):

    if lst[i][0] >= q[0]:
        heapq.heappop(q)
        
    heapq.heappush(q, lst[i][1])
    
'''