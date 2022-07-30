'''

아 이거 우선순위 큐구나,,

min-heap 사용하네,,

최소값은 언제나 항상 0번 인덱스에 존재

하하,, 진짜
자료구조가 중요하다 진짜,,,
머리에서 왜 안또르지,,,

또 하나더 중요!
우리는 N번째 큰 숫자를 원하기 때문에

어제 풀었던 다익스트라가 생각나네,,참네,,

아아 주어진 2차원 배열은 1차원 배열씩 힙큐에 넣으면서!
가장 작은수를 계속해서 뺴고! 그 보다 큰수를 계속 넣는다!
그렇게 되면 N번쨰 갓을떄의 0번쨰가 자연스레 N 번쨰 큰수가 된다! 
HEAP의 특성상
'''


import heapq
import sys

N = int(input())

heap = []


#한줄 씩 입력받는 verion => 이걸 기준으로 반복문을 돌려
for _ in range(N):
    #1차원 리스트 한줄 입력받은것! 
    lst = list(map(int, sys.stdin.readline().split()))

    #heap에 아무것도 없ㅇ면!
    if not heap:
        for num in lst: #그 숫자 하나씩 뺴서! 힙에다가 다 넣는다! 
            heapq.heappush(heap, num)
            
    else:
        for num in lst: #그 숫자 하나 뺴서 대소 비교!
            #문제에 주어진 조건 적용
            if heap[0] < num:
                heapq.heappush(heap, num) #최소값보다 큰 녀석 넣기! 
                heapq.heappop(heap) #가장 작은값 삭제

print(heap[0])